# Reclame Aqui Bot - Monitoramento de Reclamações

Este projeto utiliza **Selenium** e **BeautifulSoup** para monitorar reclamações no site **Reclame Aqui** e envia notificações automáticas via **Telegram**.

## **1. Requisitos**
Antes de iniciar, certifique-se de ter instalado:
- **Python 3.12+**
- **Google Chrome e ChromeDriver**
- **Bibliotecas Python:** `selenium`, `webdriver-manager`, `beautifulsoup4`, `requests`

Para instalar as dependências:
```bash
pip install selenium webdriver-manager beautifulsoup4 requests
```

## **2. Configuração do Bot no Telegram**
1. No Telegram, inicie uma conversa com **@BotFather**.
2. Envie o comando `/newbot` e siga as instruções para criar um bot.
3. Copie o **Token** fornecido pelo BotFather.
4. Inicie uma conversa com o bot e envie `/start`.
5. Para obter o **CHAT_ID**, acesse no navegador:
   ```
   https://api.telegram.org/bot<TOKEN>/getUpdates
   ```
   Substitua `<TOKEN>` pelo seu token e copie o valor de `chat.id`.

## **3. Desenvolvimento da Aplicação**
Criamos um script Python que:
1. Usa o **Selenium** para acessar o site do Reclame Aqui.
2. Role a página para garantir que todas as reclamações sejam carregadas.
3. Captura os títulos das reclamações e formata uma mensagem.
4. Envia a mensagem ao Telegram.

### **3.1. Estrutura do Projeto**
```
reclameaqui-bot/
│── reclameaqui.py  # Script principal
│── requirements.txt # Dependências do projeto
│── Dockerfile      # Configuração para Docker
│── README.md       # Documentação
```

### **3.2. Executar o Script**
Para rodar manualmente:
```bash
python reclameaqui.py
```

## **4. Criando um Executável com PyInstaller**
Se quiser rodar como um executável:
```bash
pip install pyinstaller
pyinstaller --onefile --name reclameaqui_bot reclameaqui.py
```
O executável será gerado na pasta `dist/`.

## **5. Rodando com Docker**
Criamos um `Dockerfile` para rodar a aplicação em qualquer ambiente:

### **5.1. Criar o Arquivo `Dockerfile`**
```dockerfile
FROM python:3.12-slim
RUN apt-get update && apt-get install -y chromium chromium-driver
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "reclameaqui.py"]
```

### **5.2. Construir e Rodar o Container**
```bash
docker build -t reclameaqui-bot .
docker run --rm reclameaqui-bot
```

## **6. Automatizando com Systemd (Linux)**
Se quiser rodar automaticamente no Linux:

### **6.1. Criar o Arquivo de Serviço**
```bash
sudo nano /etc/systemd/system/reclameaqui.service
```
Adicione:
```ini
[Unit]
Description=Reclame Aqui Bot
After=network.target

[Service]
ExecStart=/usr/bin/python3 /home/user/bot-teste/reclameaqui.py
WorkingDirectory=/home/user/bot-teste
Restart=always
User=user

[Install]
WantedBy=multi-user.target
```

### **6.2. Ativar e Iniciar o Serviço**
```bash
sudo systemctl daemon-reload
sudo systemctl enable reclameaqui
sudo systemctl start reclameaqui
```
Para verificar os logs:
```bash
sudo journalctl -u reclameaqui -f
```

## **7. Conclusão**
Agora a  aplicação está pronta para monitorar reclamações no Reclame Aqui e enviá-las para o Telegram automaticamente! 🚀

