#! /usr/bin/env python3

import os
import sys
import openai

import asyncio
from aiohttp import web

import gradio

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

#async def pushToTalkButtonPushed(request):
    #https://docs.aiohttp.org/en/stable/web_quickstart.html#aiohttp-web-websockets
#    ws = web.WebSocketResponse()
#    await ws.prepare(request)
#    async for audio in transcribe():
#        await ws.send_bytes(audio)

#    return ws

#app = web.Application()
#app.add_routes([
#    web.get('/', pushToTalkButtonPushed)
#])

#if __name__ == '__main__':
#    port = int(sys.argv[1])
#    print( f"Listening on port {port}" )
#    print("what the heck is going on making call to web run app")
#    web.run_app(app, port=port)
#def initWeb():
#    app = web.Application() #https://docs.aiohttp.org/en/stable/web_quickstart.html
#    app.router.add.get("/", )

ui = gradio.Interface(fn=transcribe, inputs=gradio.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()
