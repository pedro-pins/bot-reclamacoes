# Reclame Aqui Bot - Monitoramento de Reclamações

Este projeto é um bot desenvolvido em Python que realiza o monitoramento automático de reclamações no site [Reclame Aqui](https://www.reclameaqui.com.br), focando em empresas específicas, e envia as informações via Telegram.

---

## Funcionalidades

- Captura os títulos das últimas reclamações públicas.
- Envia notificações para o Telegram com links diretos.
- Utiliza scraping com Selenium + BeautifulSoup para maior confiabilidade.
- Pode ser configurado facilmente via `.env`.

---

## Tecnologias Utilizadas

- **Python 3.12+**
- **Selenium** (automação de navegador)
- **BeautifulSoup4** (parser HTML)
- **Requests** (requisições para API Telegram)
- **python-dotenv** (carregamento de variáveis de ambiente)
- **webdriver-manager** (instalação automática do driver)

---

## Instalação

1. Clone o repositório:

```bash
git clone https://github.com/pedro-pins/bot-reclamacoes.git
cd bot-reclamacoes
```

2. Crie e ative um ambiente virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Configuração

Crie um arquivo `.env` na raiz do projeto com o seguinte conteúdo:

```
TELEGRAM_TOKEN=seu_token_do_bot
TELEGRAM_CHAT_ID=seu_chat_id
URL_RECLAMEAQUI=https://www.reclameaqui.com.br/empresa/claro/
```

Você pode usar o arquivo `.env.example` como base.

---

## Execução

Execute o bot com:

```bash
python src/reclameaqui.py
```

O bot acessará a página da empresa, extrairá as reclamações mais recentes e enviará as informações formatadas para o Telegram.

---

## Exemplo de Saída

```
Total de reclamações encontradas: 3

1. Cobrança indevida de serviço cancelado
https://www.reclameaqui.com.br/claro/cobranca-indesejada...

2. Atendimento ineficiente
https://www.reclameaqui.com.br/claro/atendimento-pessimo...
```

---

## Estrutura do Projeto

```
bot-reclamacoes/
├── src/
│   └── reclameaqui.py
├── .env.example
├── requirements.txt
├── README.md
```

---

## Conclusão

- Implementar cache ou log para evitar mensagens duplicadas.
- Adicionar agendamento com cron ou schedule.
- Armazenar histórico das reclamações em arquivo ou banco de dados.
- Criar testes automatizados.
- Publicar via Docker com container leve.

---

## Licença

Para sugestões ou dúvidas, sinta-se à vontade para abrir uma Issue.

---

## Contato

Pedro Pins: [Linkedin](https://www.linkedin.com/in/pedro-pins-0a859b193/)

