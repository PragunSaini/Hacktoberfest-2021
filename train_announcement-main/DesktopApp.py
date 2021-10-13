from tkinter import *
import PIL.Image,PIL.ImageTk
from functools import partial
import imutils
import cv2
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play


def gTTS_text(text,filename):
    mytext=str(text)
    langunage='hi'
    myobj=gTTS(text=mytext,lang=langunage,slow=False)
    myobj.save(filename)

def combineAudio(audios):
    combined=AudioSegment.empty()

    for audio in audios:
        combined+=AudioSegment.from_wav(audio)

    return combined

def announce(train_no,train_name,fromEnpt,toEnpt,viaEnpt,plateform):
    TrainNum=str(train_no.get())
    TrainName=str(train_name.get())
    From=str(fromEnpt.get())
    To=str(toEnpt.get())
    Via=str(viaEnpt.get())
    Plateform=str(plateform.get())

    Mod_TrainNum=''

    Details=[]

    for char in TrainNum:
        Mod_TrainNum+=(char+' ')

    # print(Mod_TrainNum,TrainName,From,To,Via)

    gTTS_text(From,'./Mp3Files/2_hindi.mp3')
    sound = AudioSegment.from_mp3("./Mp3Files/2_hindi.mp3")
    sound.export("./Anouncements/2_hindi.wav", format="wav")

    # 4 via-city
    gTTS_text(Via,'./Mp3Files/4_hindi.mp3')
    sound = AudioSegment.from_mp3("./Mp3Files/4_hindi.mp3")
    sound.export("./Anouncements/4_hindi.wav", format="wav")

    # 6 to-city
    gTTS_text(To,'./Mp3Files/6_hindi.mp3')
    sound = AudioSegment.from_mp3("./Mp3Files/6_hindi.mp3")
    sound.export("./Anouncements/6_hindi.wav", format="wav")

    # 8 train no and name
    gTTS_text(Mod_TrainNum+' '+TrainName,'./Mp3Files/8_hindi.mp3')
    sound = AudioSegment.from_mp3("./Mp3Files/8_hindi.mp3")
    sound.export("./Anouncements/8_hindi.wav", format="wav")

    # 10 plateform number
    gTTS_text(Plateform,'./Mp3Files/10_hindi.mp3')
    sound = AudioSegment.from_mp3("./Mp3Files/10_hindi.mp3")
    sound.export("./Anouncements/10_hindi.wav", format="wav")

    audios=[f'./Anouncements/{i}_hindi.wav' for i in range(1,12)]

    TrainNo=str(TrainNum)

    announcement=combineAudio(audios) 
    announcement.export(f'./TrainAnouncementS/announcement_{TrainNo}.wav',format='wav')

    audio_file='./TrainAnouncementS/announcement_'+TrainNo+'.wav'

    song = AudioSegment.from_wav(audio_file)
    play(song)


window=Tk()
window.title('Train Announcement System!')
window.geometry('630x650')

cv_img=cv2.cvtColor(cv2.imread('BackgroundImg.jpg'),cv2.COLOR_BGR2RGB)

canvas=Canvas(window,width=630,height=300)
rimage=imutils.resize(cv_img,width=630,height=100)
photo=PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(rimage))
image_on_canvas=canvas.create_image(0,0,ancho=NW,image=photo)
canvas.pack()

train_noIn=Label(window,text='Enter Train No:')
train_noIn.pack(pady=0)

train_no=Entry(window)
train_no.pack(pady=0)

train_nameIn=Label(window,text='Enter Train Name')
train_nameIn.pack(pady=0)

train_name=Entry(window)
train_name.pack(pady=0)

fromIn=Label(window,text='from:')
fromIn.pack(pady=0)

fromEnpt=Entry(window)
fromEnpt.pack(pady=0)

toIn=Label(window,text='to:')
toIn.pack(pady=0)

toEnpt=Entry(window)
toEnpt.pack(pady=0)

viaIn=Label(window,text='via:')
viaIn.pack(pady=0)

viaEnpt=Entry(window)
viaEnpt.pack(pady=0)    

plateformIn=Label(window,text='plateform No:')
plateformIn.pack(pady=0)

plateform=Entry(window,text='plateform No:')
plateform.pack(pady=0)    

btn=Button(window,text='Do Announcement!',
    command=partial(announce,train_no,train_name,fromEnpt,toEnpt,viaEnpt,plateform))
btn.pack(pady=2)

window.mainloop()
