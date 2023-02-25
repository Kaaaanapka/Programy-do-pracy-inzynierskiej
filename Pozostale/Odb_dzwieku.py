import sounddevice as sd
import soundfile as sf
import speech_recognition as sr_audio 
import os, pyttsx3, pygame, time

def sync_record(filename, duration, fs, channels):
    print('Nagrywanie')
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=channels) 
    sd.wait()
    sf.write(filename, myrecording, fs)
    print('Zakonczono nagrywanie')
    
def sync_playback(filename):
    # takes in a file and plays it back 
    pygame.mixer.init() 
    pygame.mixer.music.load(filename) 
    pygame.mixer.music.play()
    
def speak_text(text): 
    engine=pyttsx3.init() 
    engine.setProperty('voice', 'com.apple.speech.synthesis.voice.Alex')
    engine.say(text) 
    engine.runAndWait()
    
def transcribe_audio_sphinx(filename):
# transcribe the audio (note this is only done if a voice sample) r=sr_audio.Recognizer()
    with sr_audio.AudioFile(filename) as source:
        r=sr_audio.Recognizer()
        audio = r.record(source)
        
    text=r.recognize_sphinx(audio) 
    print('transcript: '+text)
    return text

def fetch_weather():
    os.system('open https://www.yahoo.com/news/weather')
    
speak_text('Co chcesz wyszukać?')
sync_record('response.wav',2,16000,1) 
transcript=transcribe_audio_sphinx('response.wav')

if transcript.lower().find('weather') >= 0:
    fetch_weather()
