import os
import requests # type: ignore
from bs4 import BeautifulSoup # type: ignore
from selenium import webdriver # type: ignore
from selenium.webdriver.chrome.options import Options # type: ignore
from selenium.webdriver.chrome.service import Service # type: ignore
from selenium.webdriver.common.by import By # type: ignore
from selenium.webdriver.support.ui import WebDriverWait # type: ignore
from selenium.webdriver.support import expected_conditions as EC # type: ignore
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from dotenv import load_dotenv # type: ignore

# Carrega variáveis do arquivo .env
load_dotenv()

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
URL_RECLAMEAQUI = os.getenv ("URL_RECLAMEAQUI") # adicione a empresa que deseja verificar. 

if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID or not URL_RECLAMEAQUI:
    raise ValueError("As variáveis de ambiente TELEGRAM_TOKEN, TELEGRAM_CHAT_ID e URL_RECLAMEAQUI devem ser definidas.")


def configurar_driver():
    options = Options()
    options.add_argument("--headless")
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
        WebDriverWait(driver, 20).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, "complaint-title"))
        )

        soup = BeautifulSoup(driver.page_source, "html.parser")
        reclamacoes = soup.find_all("div", class_="complaint-title")

        if reclamacoes:
            mensagem = f"Total de reclamações encontradas: {len(reclamacoes)}\n\n"
            for idx, item in enumerate(reclamacoes, start=1):
                texto = item.get_text(strip=True)
                mensagem += f"{idx}. {texto}\n"

    except Exception as erro:
        mensagem = f"Erro ao capturar reclamações: {str(erro)}"

    finally:
        driver.quit()

    return mensagem

def enviar_mensagem_telegram(token, chat_id, texto):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": chat_id, "text": texto}
    resposta = requests.post(url, data=payload)
    return resposta

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
