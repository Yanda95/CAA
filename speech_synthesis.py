import os
import azure.cognitiveservices.speech as speechsdk
import json


# This example requires environment variables named "SPEECH_KEY" and "SPEECH_REGION"
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('SPEECH_KEY'), region=os.environ.get('SPEECH_REGION'))
audio_config = speechsdk.audio.AudioOutputConfig(filename="xxx.wav")

# Set the voice to a neural one that supports emotions
speech_config.speech_synthesis_voice_name = 'en-US-JennyNeural'

speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

# SSML with emotion control
ssml_text = """
<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='https://www.w3.org/2001/mstts' xml:lang='en-US'>
    <voice name='en-US-JennyNeural'>
        <mstts:express-as style='angry'>
            <prosody rate='-10.00%' pitch='-5.00%'>
                They didn't take any of my recommendations!
            </prosody>
        </mstts:express-as>


    </voice>
</speak>
"""

# Synthesize the SSML to the default speaker
speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml_text).get()

if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
    print("Speech synthesized successfully.")
elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = speech_synthesis_result.cancellation_details
    print("Speech synthesis canceled: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        if cancellation_details.error_details:
            print("Error details: {}".format(cancellation_details.error_details))