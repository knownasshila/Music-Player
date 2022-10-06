from tkinter import*
from pygame import mixer
from tkinter import filedialog
import tkinter.messagebox
import os

def play_btn():
    try:
        paused
    except NameError:
        try:
            song=lab.curselection()
            song=int(song[0])
            playthis=playlist[song]
            mixer.music.load(playthis)
            mixer.music.play()
            statubar['text']='Playing music'+'-'+os.path .basename(playthis)
            show_detail(playthis)
        except:
            tkinter.messagebox.showerror('Error','Please open a file first!')
        
    else:
        mixer.music.unpause()
        statubar['text']=' Music Resumed '


def stop_btn():

    mixer.music.stop()
    statubar['text']='Music Stopped'

def pause_btn():
    global paused
    paused=TRUE

    mixer.music.pause()
    statubar['text']='Music Paused'

def rewind_btn():
    play_btn()
    statubar['text']='Music Rewinded'


def set_volume(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)

def about():
    tkinter.messagebox.showinfo('MELODY','This is a music player by Shila')
    
def browse_file():
    global filename
    filename=filedialog.askopenfilename()
    add(filename)

playlist=[]

def add(c):
    c=os.path .basename(filename)
    index=0
    lab.insert(index,c)
    playlist.insert(index,filename)
    index+=1

def delete():

    song=lab.curselection()
    song=int(song[0])
    lab.delete(song)
    playlist.pop(song)
    

def show_detail(play_song):
    filetext['text']='Playing music'+'-'+os.path .basename(play_song)
    a=mixer.Sound(play_song)
    total=a.get_length()
    mins,secs=divmod(total,60)
    mins=round(mins)
    secs=round(secs)
    timeformat='{:02d}:{:02d}'.format(mins,secs)
    lengthtext['text']='Total length'+'-'+timeformat

    

def main():

    global statubar
    global filetext
    global lengthtext
    global lab 
    root=Tk()
    mixer.init()
    root.title('MELODY')
    root.geometry('500x280')
    
    root.iconbitmap(r'musicplayer.ico')
    statubar=Label(root,text='Welcome to Melody player',relief=SUNKEN,anchor='w')
    statubar.pack(side=BOTTOM,fill=X)

    left=Frame(root)
    left.pack(side=LEFT,padx=30)
    lab=Listbox(left)
    lab.pack()

    
    Button(left,text='+Add',bg='gray',command=browse_file).pack(side=LEFT)
    Button(left,text='-Del',bg='gray',command=delete).pack(side=LEFT)


    right=Frame(root)
    right.pack()
    top=Frame(right)
    top.pack()


    Label(root,text='').pack()
    filetext=Label(top,text='Play your Music',fg='red',font=('calibri'))
    filetext.pack()
    lengthtext=Label(top,text='Total length : 00:00',fg='green',font=('calibri'))
    lengthtext.pack()

    Label(top,text='').pack()


    middleframe=Frame(right)
    middleframe.pack()
    photo1=PhotoImage(file='play.png')
    Button(middleframe,image=photo1,command=play_btn).pack(side=LEFT,padx=10)

    photo3=PhotoImage(file='stop.png')
    Button(middleframe,image=photo3,command=stop_btn).pack(side=LEFT,padx=10)

    photo2=PhotoImage(file='pause.png')
    Button(middleframe,image=photo2,command=pause_btn).pack(side=LEFT,padx=10)
    Label(root,text='').pack()
    


    bottomframe=Frame(right)
    bottomframe.pack()

    Label(bottomframe,text='').pack()

    photo4=PhotoImage(file='rewind.png')
    Button(bottomframe,image=photo4,command=rewind_btn).pack(side=LEFT,padx=10,pady=10)


    scale=Scale(bottomframe, from_=0,to=100,orient=HORIZONTAL,command=set_volume)
    scale.set(40)
    mixer.music.set_volume(0.4)
    scale.pack()
    

    menubar=Menu(root)
    root.config(menu=menubar)

    subMenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='File',menu=subMenu)
    subMenu.add_command(label='open', command=browse_file)
    subMenu.add_command(label='exit',command=root.destroy)

    subMenu=Menu(menubar,tearoff=0)
    menubar.add_cascade(label='Help',menu=subMenu)
    subMenu.add_command(label='About us',command=about)
    
    root.mainloop()
main()







