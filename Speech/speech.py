import io
import os
import json

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

# Instantiates a client
client = speech.SpeechClient()

# The name of the audio file to transcribe
file_name = os.path.join(
    os.path.dirname(__file__),
    'resources',
    'french.wav')

# Loads audio into memory
with io.open(file_name, 'rb') as audio_file:
    content = audio_file.read()
    audio = types.RecognitionAudio(content=content)

config = types.RecognitionConfig(
    encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
    sample_rate_hertz=44100,
    language_code='en-US')
#language code for NL = nl-NL for EN = en-US

# Detects speech in the audio file
response = client.recognize(config, audio)

# Print out transcript and store it in a json file named result.json
for result in response.results:
	data = {'Transcript': format(result.alternatives[0].transcript)} 
	with open('result.json', 'w') as json_file:
		result = json.dump(data, json_file)
	print(data)
