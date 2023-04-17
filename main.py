#to view, use python3 main.py and goto localhost:7860

import os
import openai

import asyncio
from aiohttp import web

openai.api_key = os.getenv("OPENAI_API_KEY")

#Drawing from https://github.com/hackingthemarkets/chatgpt-api-whisper-api-voice-assistant/blob/main/therapist.py

def transcribe(audio):

    audioFilenameWithExtension = audio + '.wav';
    os.rename(audio, audioFilenameWithExtension);
    audioFile = open(audioFilenameWithExtension, "rb");
    transcript = openai.Audio.transcribe("whisper-1",audioFile);

    messages = [{"role": "system", "content": 'You are current president joe biden. respond however you see fit in your infinite ai wisdom'}];

    messages.append({"role": "user", "content": transcript["text"]})

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages);
    return response;

#def initWeb():
#    app = web.Application() #https://docs.aiohttp.org/en/stable/web_quickstart.html
#    app.router.add.get("/", )


