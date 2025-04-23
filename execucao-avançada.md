
# Atualizações e Melhorias - bot-reclamacoes

Este documento complementa o README principal com informações mais técnicas, voltadas para automação, deploy e futuras extensões do projeto.

---

## Docker - Execução em Container

### Dockerfile sugerido:

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y chromium chromium-driver

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "src/reclameaqui.py"]
```

### Como rodar:

```bash
docker build -t reclameaqui-bot .
docker run --rm --env-file .env reclameaqui-bot
```

---

## Agendamento com `cron` (Linux)

### Editar o crontab:

```bash
crontab -e
```

### Exemplo de execução a cada hora:

```bash
0 * * * * /caminho/para/python /caminho/do/projeto/src/reclameaqui.py >> /tmp/reclameaqui.log 2>&1
```

---

## Geração de Executável (usando `pyinstaller`)

Você pode transformar o bot em um executável para facilitar o deploy em outras máquinas:

### Instale o pyinstaller:

```bash
pip install pyinstaller
```

### Geração:

```bash
pyinstaller --onefile src/reclameaqui.py
```

> O executável será gerado em `dist/reclameaqui`.

---

## Script de Setup Automático

O repositório inclui um script `setup.sh`, que pode ser referenciado no README ou usado em ambientes provisionados automaticamente.

### Exemplo de execução:

```bash
chmod +x setup.sh
./setup.sh
```

---

## Outras Sugestões Futuras

- Log das últimas reclamações enviadas.
- Evitar duplicidade com armazenamento em CSV ou banco local.
- Painel de visualização usando Flask ou Streamlit.
- Webhook opcional em vez de apenas Telegram.

---

Este documento deve ser atualizado conforme o projeto evolui.
