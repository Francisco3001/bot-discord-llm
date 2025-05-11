import os
import discord
import requests
from dotenv import load_dotenv

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = discord.Client(intents=intents)

def preguntar_a_ollama(prompt_usuario):
    try:
        
        with open("contexto.txt", "r", encoding="utf-8") as f: #contexto para los mensajes
            contexto = f.read() 

        prompt_completo = contexto.strip() + "\n\nUsuario: " + prompt_usuario

        response = requests.post("http://ollama:11434/api/generate", json={
            "model": "mistral",
            "prompt": prompt_completo,
            "stream": False
        })
        return response.json()["response"]
    except Exception as e:
        print("❌ Error al consultar Ollama:", e)
        return "No pude responder con el modelo local."


@bot.event
async def on_ready():
    print(f"✅ Bot conectado")

@bot.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('!'):
        prompt = message.content[1:].strip()
        await message.channel.send("⌛blud is thinking⌛")
        respuesta = preguntar_a_ollama(prompt)
        await message.channel.send(respuesta)

bot.run(DISCORD_TOKEN)
