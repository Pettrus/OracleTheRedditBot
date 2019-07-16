import os, requests, time
from xml.etree import ElementTree
from dotenv import load_dotenv
import os

load_dotenv()

# This code is required for Python 2.7
try: input = raw_input
except NameError: pass

def get_token():
    fetch_token_url = "https://southcentralus.api.cognitive.microsoft.com/sts/v1.0/issueToken"
    headers = {
        'Ocp-Apim-Subscription-Key': os.getenv("KEY_AZURE")
    }
    response = requests.post(fetch_token_url, headers=headers)

    return str(response.text)

def save_audio(tts, frame, access_token):
    constructed_url = 'https://southcentralus.tts.speech.microsoft.com/cognitiveservices/v1'
    headers = {
        'Authorization': 'Bearer ' + access_token,
        'Content-Type': 'application/ssml+xml',
        'X-Microsoft-OutputFormat': 'riff-24khz-16bit-mono-pcm',
        'User-Agent': os.getenv("AGENT_AZURE")
    }
    xml_body = ElementTree.Element('speak', version='1.0')
    xml_body.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-us')
    voice = ElementTree.SubElement(xml_body, 'voice')
    voice.set('{http://www.w3.org/XML/1998/namespace}lang', 'en-US')
    voice.set('name', 'en-US-Jessa24kRUS') # Short name for 'Microsoft Server Speech Text to Speech Voice (en-US, Guy24KRUS)'
    voice.text = tts
    body = ElementTree.tostring(xml_body)

    response = requests.post(constructed_url, headers=headers, data=body)

    if response.status_code == 200:
        with open('audios/' + str(frame) + '.wav', 'wb') as audio:
            audio.write(response.content)
            print(str(frame) + " AUDIO completed")
    else:
        print("\nStatus code: " + str(response.status_code) + "\nSomething went wrong. Check your subscription key and headers.\n")