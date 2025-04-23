import os
import requests  # type: ignore
from bs4 import BeautifulSoup  # type: ignore
from selenium import webdriver  # type: ignore
from selenium.webdriver.chrome.options import Options  # type: ignore
from selenium.webdriver.chrome.service import Service  # type: ignore
from selenium.webdriver.common.by import By  # type: ignore
from selenium.webdriver.support.ui import WebDriverWait  # type: ignore
from selenium.webdriver.support import expected_conditions as EC  # type: ignore
from webdriver_manager.chrome import ChromeDriverManager  # type: ignore
from dotenv import load_dotenv  # type: ignore

# Carrega variáveis do arquivo .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
URL_RECLAMEAQUI = os.getenv("URL_RECLAMEAQUI")

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID or not URL_RECLAMEAQUI:
    raise ValueError("As variáveis de ambiente devem estar definidas no .env")


def configurar_driver():
    options = Options()
    options.add_argument("--headless")  # Ative para execução invisível
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("user-agent=Mozilla/5.0")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def capturar_reclamacoes():
    driver = configurar_driver()
    mensagem = "Nenhuma reclamação encontrada ou erro ao carregar a página."

    try:
        driver.get(URL_RECLAMEAQUI)

        # Aguarda qualquer item da lista principal aparecer
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a#site_bp_home_ler_reclamacao"))
        )

        # Scroll leve para carregar todos os elementos visíveis
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.implicitly_wait(3)

        soup = BeautifulSoup(driver.page_source, "html.parser")

        # Captura os links com título da reclamação
        links = soup.select("a#site_bp_home_ler_reclamacao")

        if links:
            mensagem = f"Total de reclamações encontradas: {len(links)}\n\n"
            for idx, link in enumerate(links, start=1):
                titulo_tag = link.select_one("h4")
                titulo = titulo_tag.get_text(strip=True) if titulo_tag else "Título não encontrado"
                href = link.get("href", "#")
                url = f"https://www.reclameaqui.com.br{href}"
                mensagem += f"{idx}. {titulo}\n{url}\n\n"
        else:
            mensagem = "Nenhuma reclamação encontrada."

    except Exception:
        import traceback
        mensagem = f"Erro ao capturar reclamações:\n{traceback.format_exc()}"

    finally:
        driver.quit()

    return mensagem


def enviar_mensagem_telegram(token, chat_id, texto):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": texto}
    return requests.post(url, data=payload)


def main():
    print("Executando bot de monitoramento do Reclame Aqui...")
    texto = capturar_reclamacoes()
    resposta = enviar_mensagem_telegram(TELEGRAM_TOKEN, TELEGRAM_CHAT_ID, texto)

    if resposta.status_code == 200:
        print("Mensagem enviada com sucesso para o Telegram.")
    else:
        print(f"Erro ao enviar mensagem: {resposta.status_code} - {resposta.text}")


if __name__ == "__main__":
    main()
