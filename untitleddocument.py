#https://www.youtube.com/watch?v=UZzDhV-21NE
#https://www.youtube.com/watch?v=2VmgpHUld8o
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox as mb
from pytube import YouTube

def setURL():
    #Get URL of the Video
    url = getURL.get()

    #Create Object to hold the URL
    global yt
    yt = YouTube(url)
    Label(root,text=yt.title).place(x=0,y=500)

    #Get Quality and display as list in the Listbox
    resolutions = list()  # set that holds the resolutions available

    try:
        yt = YouTube(url)  # creating the object that stores information about the video

        for stream in yt.streams.filter(type="video"):  # Only look for video streams
            resolutions.append(stream.resolution)  # Adding all resolutions available

            resolutions = list(resolutions)  # list containing all resolutions

    except Exception as e:
        mb.showerror('Error', e)
        return

    global res
    res=StringVar()
    # Creating a radio button for each resolution
    R1 = Radiobutton(listbox, text='144p', variable=res, value='144p')
    R1.place(x=80, y=50)
    R1.deselect()
    R2 = Radiobutton(listbox, text='240p', variable=res, value='240p')
    R2.place(x=80, y=80)
    R2.deselect()
    R3 = Radiobutton(listbox, text='360p', variable=res, value='360p')
    R3.place(x=80, y=110)
    R3.deselect()
    R4 = Radiobutton(listbox, text='480p', variable=res, value='480p')
    R4.place(x=80, y=140)
    R4.deselect()
    R5 = Radiobutton(listbox, text='720p', variable=res, value='720p')
    R5.place(x=80, y=170)
    R5.deselect()

    # disabling those radio buttons that are not available in the video
    if ('144p' not in resolutions):
        R1.config(state=DISABLED)
    elif ('240p' not in resolutions):
        R2.config(state=DISABLED)
    elif ('360p' not in resolutions):
        R3.config(state=DISABLED)
    elif ('480p' not in resolutions):
        R4.config(state=DISABLED)
    elif ('720p' not in resolutions):
        R5.config(state=DISABLED)

def clickDownload():
    if(getURL.get() == ""):
        mb.showinfo("ERROR", "ENTER url ")
        return
    elif (getLoc.get() == ""):
        mb.showinfo("ERROR", "ENTER LOCATION ")
        return
    resol = res.get()  # getting resolution based on the radio button selected
    path = getLoc.get()  # getting the location where the video needs to be downloaded

    try:  # downloading the video of selected resolution
        ys = yt.streams.filter(resolution=resol,mime_type='video/mp4',type='video')
        ys.first().download(path)
    except Exception as e:
        mb.showerror('Error', e)

def clickBrowse():
    location_of_download = filedialog.askdirectory()
    getLoc.set(location_of_download)

def clickReset():
    getURL.set("")
    getLoc.set("")

def clickmp3():
    path = getLoc.get()
    yt.streams.filter(only_audio=True).first().download(path)

#Create Root Object
root = Tk()

#Set Title
root.title("YouTube Video Dowloader")

#Set size of window
root.geometry("1000x600")

#Make the Window not Resizeable
#root.resizable(False, False)

#Set Labels
headLabel       = Label(root,   text="YOUTUBE VIDEO DOWNLOADER",  font=("Century Gothic",25)).grid(row=0, column=1, padx=10, pady=10)
urlLabel        = Label(root,   text="URL",                 font=("Century Gothic",15)).grid(row=1, column=0, padx=10, pady=10)
qualityLabel    = Label(root,   text="SELECT QUALITY",      font=("Century Gothic",15)).grid(row=2, column=0, padx=10, pady=10)
locLabel        = Label(root,   text="LOCATION",            font=("Century Gothic",15)).grid(row=3, column=0, padx=10, pady=10)

#Get Input
getURL = StringVar()
getLoc = StringVar()

#Set Entry
urlEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getURL, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=1,column=1, padx=10, pady=10)
locEntry    = Entry(root,   font=("Century Gothic",12), textvariable = getLoc, width = 50, bd=3, relief=SOLID, borderwidth=1).grid(row=3,column=1, padx=10, pady=10)

#List box for video Quality
listbox     = Frame(root, width = 500, height = 200, bd=3, relief=SOLID, borderwidth=1,bg='white')
listbox.grid(row=2,column=1, padx=10, pady=10)

#Set Buttons
urlButton       = Button(root, text = "SET URL",    font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=setURL).grid(row=1, column=2, padx=10, pady=10)
browseButton    = Button(root, text = "BROWSE",     font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickBrowse).grid(row=3, column=2, padx=10, pady=10)
downloadButton  = Button(root, text = "DOWNLOAD",   font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickDownload).grid(row=4, column=1, padx=10, pady=10)
resetButton     = Button(root, text = "CLEAR ALL",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickReset).grid(row=4, column=2, padx=10, pady=10)
mp3Button     = Button(root, text = "DOWNLOAD MP3",  font=("Century Gothic",10), width=15, relief=SOLID, borderwidth=1, command=clickmp3).grid(row=4, column=0, padx=10, pady=10)

#Set an infinite loop so window stays in view
root.mainloop()
