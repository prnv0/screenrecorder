import tkinter
from tkinter import *
import pyscreenrec
from PIL import Image, ImageTk

root=tkinter.Tk()
# root.wm_attributes("-transparentcolor", 'grey')
root.geometry("400x600")
root.title("Screen Recorder")
root.config(bg="#fff")
root.resizable(False,False)
rec=pyscreenrec.ScreenRecorder()


def start_rec():
    file=filename.get()
    filenamed=str(file +".mp4")
    filenamed="Python\screenrecorder\\"+filenamed
    print(filenamed)
    rec.start_recording(filenamed,10)
    print("Recording")
def resume_rec():
    rec.resume_recording()
    print("Resumed")
def pause_rec():
    rec.pause_recording()
    print("Paused")
def stop_rec():
    rec.stop_recording()
    print("Recording Stopped")

#background image
image1 = Image.open("Python\screenrecorder\\background.png")
test = ImageTk.PhotoImage(image1)
label1 = Label(root,image=test)
label1.image = test
label1.place(x=-2, y=0)

#title
title=Label(root,text="Screen Recorder",bg="#cdfede",font=("Arial Bold",10))
title.pack(pady=15)

#body
imagerecording=PhotoImage(file="Python\screenrecorder\\recording.png")
Label(root,image=imagerecording,bd=0).pack(pady=85)

start=Button(root,text="Start",font="arial-22",bd=0,command=start_rec)
start.place(x=178,y=290)
filename=StringVar()
input=Entry(root,textvariable=filename,width=20,font="arial-15")
input.place(x=100,y=350)
filename.set("recording")

imagestart=PhotoImage(file="Python\screenrecorder\play.png")
play=Button(root,image=imagestart,bd=0,bg="#fff",command=resume_rec)
play.place(x=85,y=450)


imagepause=PhotoImage(file="Python\screenrecorder\pause.png")
pause=Button(root,image=imagepause,bd=0,bg="#fff",command=pause_rec)
pause.place(x=170,y=453)

imagestop=PhotoImage(file="Python\screenrecorder\stop.png")
stop=Button(root,image=imagestop,bd=0,bg="#fff",command=stop_rec)
stop.place(x=255,y=453)

root.mainloop()