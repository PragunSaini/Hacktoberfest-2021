import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS
from DesktopApp import *

def textToSpeech(text,filename):
    mytext=str(text)
    langunage='hi'
    myobj=gTTS(text=mytext,lang=langunage,slow=False)
    myobj.save(filename)

def mergeAudios(audios):
    combined=AudioSegment.empty()

    for audio in audios:
        combined+=AudioSegment.from_wav(audio)

    return combined

def genrateSkeleton():
    audio=AudioSegment.from_wav('railway.wav')

    #1. Kripys dyan dijiya.....
    start=87200  # starting timein milli second
    finish=90000
    audioProcessed=audio[start:finish]
    audioProcessed.export('./Anouncements/1_hindi.wav',format='wav')

    #2. From city 

    #3. sai chalkar.....
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export('./Anouncements/3_hindi.wav', format="wav")

    #4. is via-city
     
    #5. ke rastai
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("./Anouncements/5_hindi.wav", format="wav")

    #6. to-city
     
    #7. Generate ko jaane wali gaadi sakhya
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("./Anouncements/7_hindi.wav", format="wav")

    #8. is train no and name
     
    #9. kuch hi samay mei platform sankhya
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("./Anouncements/9_hindi.wav", format="wav")

    # 10 is platform number

    # 11 - par aa rahi hai
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("./Anouncements/11_hindi.wav", format="wav")


def genrateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)

    for index,item in df.iterrows():
        # 2 from City
        textToSpeech(item['from'],'./Mp3Files/2_hindi.mp3')
        sound = AudioSegment.from_mp3("./Mp3Files/2_hindi.mp3")
        sound.export("./Anouncements/2_hindi.wav", format="wav")

        # 4 via-city
        textToSpeech(item['via'],'./Mp3Files/4_hindi.mp3')
        sound = AudioSegment.from_mp3("./Mp3Files/4_hindi.mp3")
        sound.export("./Anouncements/4_hindi.wav", format="wav")

        # 6 to-city
        textToSpeech(item['to'],'./Mp3Files/6_hindi.mp3')
        sound = AudioSegment.from_mp3("./Mp3Files/6_hindi.mp3")
        sound.export("./Anouncements/6_hindi.wav", format="wav")

        # 8 train no and name
        textToSpeech(item['train_no']+' '+item['train_name'],'./Mp3Files/8_hindi.mp3')
        sound = AudioSegment.from_mp3("./Mp3Files/8_hindi.mp3")
        sound.export("./Anouncements/8_hindi.wav", format="wav")

        # 10 plateform number
        textToSpeech(item['plateform'],'./Mp3Files/10_hindi.mp3')
        sound = AudioSegment.from_mp3("./Mp3Files/10_hindi.mp3")
        sound.export("./Anouncements/10_hindi.wav", format="wav")


        audios=[f'./Anouncements/{i}_hindi.wav' for i in range(1,12)]

        TrainNo=str(item['train_no'])

        announcement=mergeAudios(audios) 
        announcement.export(f'./TrainAnouncementS/announcement_{TrainNo}_{index+1}.wav',format='wav')


if __name__=='__main__':
    print('Genrating Skeleton...')
    genrateSkeleton()
    genrateAnnouncement('announce_hindi.xlsx')
