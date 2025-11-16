 # 🤖 Bot de Discord + LLM Local con Ollama

Este proyecto implementa un bot de Discord que responde preguntas usando un modelo de lenguaje **Mistral** corriendo **localmente con Ollama**. Todo está dockerizado para facilitar la ejecución y portabilidad.


---

## 🚀 ¿Qué hace?

- Escucha mensajes de Discord que comienzan con `!`
- Envía el mensaje (con un contexto predefinido) al modelo `mistral`
- Responde en el canal de Discord con la respuesta generada localmente

---

## 🛠 Requisitos

- [Docker](https://www.docker.com/)
- [Ollama](https://ollama.com/) si querés probarlo fuera de Docker

---

## 🐳 Cómo correr el proyecto

### 1. Clonar y entrar en el repositorio

```git clone https://github.com/Francisco3001/bot-discord-llm.git```

```cd bot-discord-llm```

###  2. Construir e iniciar todo
```docker compose up --build```

## ⚙️ Variables de entorno

Crear un archivo `.env` en la raíz con tu token de Discord:

```DISCORD_TOKEN=TU_TOKEN```


## 🧠 ¿Cómo funciona el contexto?
El archivo `bot/contexto.txt` se envía en cada mensaje al modelo, antes de la pregunta del usuario. Esto permite personalizar el comportamiento general (por ejemplo: tono técnico, estilo simple, etc.).

## 📌 Modelos soportados
Podés reemplazar mistral por cualquier modelo compatible con Ollama, como:
- llama2
- gemma
- codellama
- mixtral
- tinyllama
  
Para eso, cambia la configuracione en el Dockerfile y el campo "model" de la peticion http en run.py
