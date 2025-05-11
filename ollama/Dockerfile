FROM ollama/ollama
WORKDIR /app

ENTRYPOINT ["sh", "-c", "ollama serve & sleep 5 && ollama run mistral && sleep infinity"]