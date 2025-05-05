import requests
import json

# Define o endpoint correto da API de embeddings
url = "http://localhost:11434/api/embeddings"

# Texto que você quer gerar embeddings
texto = "Olá, mundo! Este é um teste de embeddings com o Ollama."

# Define o payload da requisição
data = {
    "model": "nomic-embed-text",
    "prompt": texto
}

# Faz a requisição POST
response = requests.post(url, json=data)

# Verifica se a resposta foi bem-sucedida
if response.status_code == 200:
    result = response.json()
    embeddings = result["embedding"]
    print(f"Tamanho do vetor de embeddings: {len(embeddings)}")
    print(f"Primeiros 10 valores: {embeddings[:10]}")
else:
    print(f"Erro ao gerar embeddings: {response.status_code} - {response.text}")
