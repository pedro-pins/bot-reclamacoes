#!/bin/bash

echo "🚀 Iniciando setup do ambiente para o bot Reclame Aqui..."

# Atualiza pacotes
sudo apt update && sudo apt upgrade -y

# Instala Python e utilitários
sudo apt install -y python3 python3-pip python3-venv git wget unzip nano

# Instala Chrome e ChromeDriver
echo "🔧 Instalando Google Chrome..."
wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | sudo apt-key add -
sudo sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'
sudo apt update
sudo apt install -y google-chrome-stable

echo "🔧 Instalando ChromeDriver..."
CHROME_VERSION=$(google-chrome --version | grep -oP '\d+\.\d+\.\d+' | head -1)
wget -N https://chromedriver.storage.googleapis.com/${CHROME_VERSION}/chromedriver_linux64.zip || {
  echo "⚠️ Versão exata não encontrada. Baixando versão compatível."
  wget -N https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
}
unzip chromedriver_linux64.zip
chmod +x chromedriver
sudo mv chromedriver /usr/bin/chromedriver
rm chromedriver_linux64.zip

# Cria ambiente virtual (opcional)
python3 -m venv venv
source venv/bin/activate

# Instala dependências Python
pip install --upgrade pip
pip install -r requirements.txt

# Gera .env interativamente (opcional)
echo
read -p "Deseja criar o arquivo .env com seu TOKEN e CHAT_ID agora? (s/n): " resp
if [[ "$resp" =~ ^[Ss]$ ]]; then
  read -p "Informe o TELEGRAM_TOKEN: " token
  read -p "Informe o TELEGRAM_CHAT_ID: " chat_id
  echo -e "TELEGRAM_TOKEN=$token\nTELEGRAM_CHAT_ID=$chat_id" > .env
  echo "Arquivo .env criado com sucesso."
fi

echo "✅ Setup finalizado. Execute o bot com: python src/reclameaqui.py"
