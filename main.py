#to view, use python3 main.py and goto localhost:7860

import os
import openai
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

ui = gradio.Interface(fn=transcribe, inputs=gradio.Audio(source="microphone", type="filepath"), outputs="text").launch()
ui.launch()
