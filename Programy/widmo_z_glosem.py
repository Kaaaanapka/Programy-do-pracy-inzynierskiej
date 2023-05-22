import pyaudio
import wave
import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.signal import find_peaks
from scipy import signal
import sounddevice as sd
from playsound import playsound
import multiprocessing
import threading
import time 

user_choice = -1

tasks = []

def show_tasks():
    task_index = 0 
    for task in tasks:
        print(task + " [" + str(task_index) + "]")
        task_index += 1


def nagraj():                           #NAGRYWANIE PIERWSZEJ PRÓBKI

    FRAMES_PER_BUFFER = 3200
    FORMAT = pyaudio.paInt16
    CHANNELS = 1 
    RATE = 16000

    pa = pyaudio.PyAudio()

    stream = pa.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )



    print('Nagrywanie')

    seconds = 3
    frames = []
    second_tracking = 0
    second_count = 0

    for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
        data = stream.read(FRAMES_PER_BUFFER)
        frames.append(data)
        second_tracking += 1
        if second_tracking == RATE/FRAMES_PER_BUFFER:
            second_count += 1
            second_tracking = 0
            print(f'Pozostało: {seconds - second_count}' ' sekund')

    stream.stop_stream()
    stream.close()
    pa.terminate()

    obj = wave.open('probka.wav', 'wb')                 #RB READ ONLY WB WRITE ONLY DO NAGRYWANIA ZMIEŃ
    obj.setnchannels(CHANNELS)
    obj.setsampwidth(pa.get_sample_size(FORMAT))
    obj.setframerate(RATE)
    obj.writeframes(b''.join(frames))
    obj.close()



def odtworz():

    playsound('probka.wav')

def nag_odt():                      #ODTWORZENIE PRÓBKI + NAGRANIE Z ODLEGLOSCI NP. 1 METRA
    


        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1 
        RATE = 16000

        pa = pyaudio.PyAudio()
        
        stream = pa.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=FRAMES_PER_BUFFER
        )
        
        print('Nagrywanie')

        seconds = 3
        frames = []
        second_tracking = 0
        second_count = 0



        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)
            second_tracking += 1
            if second_tracking == RATE/FRAMES_PER_BUFFER:
                second_count += 1
                second_tracking = 0
                print(f'Pozostało: {seconds - second_count}' ' sekund')

        stream.stop_stream()
        stream.close()
        pa.terminate()

        obj = wave.open('probka2.wav', 'wb')
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(pa.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b''.join(frames))
        obj.close()

def nag_odt2():                      #ODTWORZENIE PRÓBKI + NAGRANIE Z ODLEGLOSCI NP. 1 METRA
    


        FRAMES_PER_BUFFER = 3200
        FORMAT = pyaudio.paInt16
        CHANNELS = 1 
        RATE = 16000

        pa = pyaudio.PyAudio()
        
        stream = pa.open(
            format=FORMAT,
            channels=CHANNELS,
            rate=RATE,
            input=True,
            frames_per_buffer=FRAMES_PER_BUFFER
        )
        
        print('Nagrywanie')

        seconds = 3
        frames = []
        second_tracking = 0
        second_count = 0



        for i in range(0, int(RATE/FRAMES_PER_BUFFER*seconds)):
            data = stream.read(FRAMES_PER_BUFFER)
            frames.append(data)
            second_tracking += 1
            if second_tracking == RATE/FRAMES_PER_BUFFER:
                second_count += 1
                second_tracking = 0
                print(f'Pozostało: {seconds - second_count}' ' sekund')

        stream.stop_stream()
        stream.close()
        pa.terminate()

        obj = wave.open('probka3.wav', 'wb')
        obj.setnchannels(CHANNELS)
        obj.setsampwidth(pa.get_sample_size(FORMAT))
        obj.setframerate(RATE)
        obj.writeframes(b''.join(frames))
        obj.close()


def odt_kwa():



    Fs = 16000

    t = np.linspace(0, 3, Fs, endpoint=False)
    x = signal.square(2 * np.pi * 1 * t)

    
    sd.play(x, Fs)


def pokaz_kwa():

    Fs = 16000

    t = np.linspace(0, 3, Fs, endpoint=False)
    x = signal.square(2 * np.pi * 1 * t)

    plt.plot(t, x)
    plt.xlabel("Czas(s)")
    plt.ylabel("Dźwięk")
    plt.title('Wykres prostokątny')
    file = wave.open('probka2.wav', 'rb')

    sample_freq = file.getframerate()
    frames = file.getnframes()
    signal_wave = file.readframes(-1)

    file.close()



    time = frames / sample_freq

    # z zaleznosci od kanału 1 użyj int16 w 2 użyj int32
    audio_array = np.frombuffer(signal_wave, dtype=np.int16)

    times1 = np.linspace(0, time, num=frames)

    plt.figure(figsize=(15, 5))
    plt.plot(times1, audio_array)
    plt.ylabel('Fala dźwieku')
    plt.xlabel('Czas (w s)')
    plt.xlim(0, time)
    plt.title('Wykres prostokatny wygenerowany przy uzyciu funckji nag_odt i odtworz')

    Ymax=np.max(audio_array)
    # log=10*math.log10(Ymax)

    DlaX = np.interp(Ymax, audio_array, times1, period=np.inf) # dodanie period=np.inf wystarczyło


    print('Maksymalna wartość dla (Y) to: '+ str(Ymax))

    # print(s)

    print('Dla x równego ' "%.4f" % + DlaX + ' s' ) # "%.2f" % aby zmniejszyć liczbę miejsc po przecinku do dwóch opcjonalnie możesz dodać "%.3f" % dla dokładniejszych wyników
    # print log


    file = wave.open('probka3.wav', 'rb')

    sample_freq = file.getframerate()
    frames = file.getnframes()
    signal_wave = file.readframes(-1)

    file.close()



    time = frames / sample_freq

    # z zaleznosci od kanału 1 użyj int16 w 2 użyj int32
    audio_array = np.frombuffer(signal_wave, dtype=np.int16)

    times1 = np.linspace(0, time, num=frames)

    plt.figure(figsize=(15, 5))
    plt.plot(times1, audio_array)
    plt.ylabel('Fala dźwieku')
    plt.xlabel('Czas (w s)')
    plt.xlim(0, time)
    plt.title('Wykres prostokatny wygenerowany przy uzyciu funckji nag_odt i odtworz (opozniony o 1m)')

    Ymax=np.max(audio_array)
    # log=10*math.log10(Ymax)

    DlaX1 = np.interp(Ymax, audio_array, times1, period=np.inf) # dodanie period=np.inf wystarczyło


    print('Maksymalna wartość dla (Y) to: '+ str(Ymax))

    # print(s)

    print('Dla x równego ' "%.4f" % + DlaX1 + ' s' ) # "%.2f" % aby zmniejszyć liczbę miejsc po przecinku do dwóch opcjonalnie możesz dodać "%.3f" % dla dokładniejszych wyników
    # print log


    Roznica = DlaX - DlaX1
    if (Roznica < 0 ):
    
        Roznica = Roznica*-1
    
    print('Różnica dla maksymalny amplitud w sekundach wynosi ' "%.4f" % + (Roznica) + ' s')


    plt.show()
    plt.show()
    plt.show()

def pokaz():

    file = wave.open('probka.wav', 'rb')

    sample_freq = file.getframerate()
    frames = file.getnframes()
    signal_wave = file.readframes(-1)



    file.close()



    time = frames / sample_freq

    # z zaleznosci od kanału 1 użyj int16 w 2 użyj int32
    audio_array = np.frombuffer(signal_wave, dtype=np.int16)

    times = np.linspace(0, time, num=frames)

    plt.figure(figsize=(15, 5))
    plt.plot(times, audio_array)
    plt.ylabel('Fala dźwieku')
    plt.xlabel('Czas (w s)')
    plt.xlim(0, time)
    plt.title('Próbka którą nagrałem z otoczenia')

    file = wave.open('probka2.wav', 'rb')

    sample_freq = file.getframerate()
    frames = file.getnframes()
    signal_wave = file.readframes(-1)



    file.close()



    time = frames / sample_freq

    # z zaleznosci od kanału 1 użyj int16 w 2 użyj int32
    audio_array = np.frombuffer(signal_wave, dtype=np.int16)

    times = np.linspace(0, time, num=frames)

    plt.figure(figsize=(15, 5))
    plt.plot(times, audio_array)
    plt.ylabel('Fala dźwieku')
    plt.xlabel('Czas (w s)')
    plt.xlim(0, time)
    plt.title('Próbka którą nagrałem z użyciem funkcji nag_odt, odtworz')

    Ymax1=np.max(audio_array)
    # log=10*math.log10(Ymax)

    DlaX1 = np.interp(Ymax1, audio_array, times, period=np.inf) # dodanie period=np.inf wystarczyło


    print('Maksymalna wartość dla (Y) to: '+ str(Ymax1))

    # print(s)

    print('Dla x równego ' "%.4f" % + DlaX1 + ' s' ) # "%.2f" % aby zmniejszyć liczbę miejsc po przecinku do dwóch opcjonalnie możesz dodać "%.3f" % dla dokładniejszych wyników
    # print log




    file = wave.open('probka3.wav', 'rb')

    sample_freq = file.getframerate()
    frames = file.getnframes()
    signal_wave = file.readframes(-1)



    file.close()



    time = frames / sample_freq

    # z zaleznosci od kanału 1 użyj int16 w 2 użyj int32
    audio_array = np.frombuffer(signal_wave, dtype=np.int16)

    times1 = np.linspace(0, time, num=frames)

    plt.figure(figsize=(15, 5))
    plt.plot(times1, audio_array)
    plt.ylabel('Fala dźwieku')
    plt.xlabel('Czas (w s)')
    plt.xlim(0, time)
    plt.title('Próbka opóźniona o odległość 1m którą nagrałem z użyciem funkcji nag_odt, odtworz')

    Ymax=np.max(audio_array)
    # log=10*math.log10(Ymax)

    DlaX = np.interp(Ymax, audio_array, times, period=np.inf) # dodanie period=np.inf wystarczyło


    print('Maksymalna wartość dla (Y) to: '+ str(Ymax))

    # print(s)

    print('Dla x równego ' "%.4f" % + DlaX + ' s' ) # "%.2f" % aby zmniejszyć liczbę miejsc po przecinku do dwóch opcjonalnie możesz dodać "%.3f" % dla dokładniejszych wyników
    # print log


    Roznica = DlaX - DlaX1
    if (Roznica < 0 ):
    
        Roznica = Roznica*-1
    
    print('Różnica dla maksymalny amplitud w sekundach wynosi ' "%.4f" % + (Roznica) + ' s')

    plt.show()
    plt.show()




while user_choice != 9:
    if user_choice == 1:
        nagraj()

    if user_choice ==2:    
        odtworz()

    if user_choice == 3:
        threading.Thread(target=nag_odt).start()   
        threading.Thread(target=odtworz).start()

        time.sleep(4)

    if user_choice == 4:
        threading.Thread(target=nag_odt2).start()   
        threading.Thread(target=odtworz).start()

        time.sleep(4)

    if user_choice == 5:
        pokaz()

    if user_choice == 6:
        threading.Thread(target=nag_odt).start()   
        threading.Thread(target=odt_kwa).start()
        
        time.sleep(4)

    if user_choice == 7:
        threading.Thread(target=nag_odt2).start()   
        threading.Thread(target=odt_kwa).start()

        time.sleep(4)

    if user_choice == 8:
        pokaz_kwa()   
    
    print()
    print("1. Nagraj własną próbkę dźwięku")
    print("2. Odtwórz własną próbke")
    print("3. Nagraj i odtwórz własną próbke")
    print("4. Nagraj i odtwórz własną próbke z opóźnieniem")
    print("5. Pokaż wykres własnych próbek")
    print("6. Nagraj i odtworz (próbka z wykresu prostokątnego)")
    print("7. Nagraj i odtworz z opóźnieniem (próbka z wykresu prostokątnego)")
    print("8. Pokaż wykres (dla próbek z wykresu prostokątnego)")                   
    print("9. Wyjdz")   

    user_choice = int(input("Wybierz liczbę: "))
    print()


    