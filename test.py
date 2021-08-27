import requests, uuid, json
from azure.cognitiveservices.speech import AudioDataStream, SpeechConfig, SpeechSynthesizer, SpeechSynthesisOutputFormat
from azure.cognitiveservices.speech.audio import AudioOutputConfig
import tkinter as tk

gui = tk.Tk()
gui.geometry("500x200")

def getEntry():
    speech_config = SpeechConfig(subscription="c138fb721a42436caa2709a946f19b7d", region="francecentral")
    audio_config = AudioOutputConfig(filename="FranceInter.wav")
    synthesizer = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer.speak_text_async(myEntry.get())

    subscription_key = "8460cf8fbcd642d898f99e3c78207689"
    endpoint = "https://api.cognitive.microsofttranslator.com/"

    location = "francecentral"

    path = '/translate'
    constructed_url = endpoint + path

    params = {
        'api-version': '3.0',
        'from': 'fr',
        'to': ['en']
    }
    constructed_url = endpoint + path

    headers = {
        'Ocp-Apim-Subscription-Key': subscription_key,
        'Ocp-Apim-Subscription-Region': location,
        'Content-type': 'application/json',
        'X-ClientTraceId': str(uuid.uuid4())
    }

    body = [{
        'text': ' '
    }]

    body[0]['text'] = myEntry.get()

    request = requests.post(constructed_url, params=params, headers=headers, json=body)
    response = request.json()
    text_trad = response[0]['translations'][0]['text']

    audio_config = AudioOutputConfig(filename="Traduction.wav")
    synthesizer_traduction = SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
    synthesizer_traduction.speak_text_async(text_trad)
    print(text_trad)

myEntry = tk.Entry(gui, width=40)
myEntry.pack(pady=20)

btn = tk.Button(gui, height=1, width=10, text="Traduire", bg="red", command=getEntry)
btn.pack()

gui.mainloop()