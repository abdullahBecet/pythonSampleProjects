import feedparser
from tkinter import *
import webview

# url = "https://www.cnnturk.com/feed/rss/all/news"

def clear_frame():
    # for widget in fr_haberler.winfo_children:
    #     widget.destroy()
    None

def default_color_button():
    btn_son_dakika.configure(bg="lightblue")
    btn_dunya.configure(bg="lightblue")
    btn_ekonomi.configure(bg="lightblue")
    btn_saglik.configure(bg="lightblue")

def open_url(event):
    webview.create_window( event.widget.cget("text"), event.widget.cget("text"))
    webview.start()

def dongu(haberler):
    for haber in haberler.entries:
        Label(fr_haberler,text=haber.title, anchor ='w', font=('Helveticabold',14)).pack(side=TOP, fill = "x" )
        lnk_lbl = Label(fr_haberler,text=haber.link, anchor ='w', font=('Helveticabold',14), fg="blue",cursor="hand2")
        lnk_lbl.pack(side=TOP, fill = "x" )
        lnk_lbl.bind("<Button-1>",open_url)
        Label(fr_haberler,text="-", anchor ='c', bg="pink").pack(side=TOP, fill = "x" )

def son_dakika_command():
    clear_frame()
    default_color_button()
    btn_son_dakika.configure(bg="blue")
    url = "https://www.cnnturk.com/feed/rss/all/news"
    haberler = feedparser.parse(url)
    dongu(haberler)

def dunya_command():
    clear_frame()
    default_color_button()
    btn_dunya.configure(bg="blue")
    url = "https://www.cnnturk.com/feed/rss/all/news"
    haberler = feedparser.parse(url)
    dongu(haberler)

def ekonomi_command():
    clear_frame()
    default_color_button()
    btn_ekonomi.configure(bg="blue")
    url = "https://www.cnnturk.com/feed/rss/all/news"
    haberler = feedparser.parse(url)
    dongu(haberler)

def saglik_command():
    clear_frame()
    default_color_button()
    btn_saglik.configure(bg="blue")
    url = "https://www.cnnturk.com/feed/rss/all/news"
    haberler = feedparser.parse(url)
    dongu(haberler)


window = Tk()
window.title("Haberler bot Programs")
window.geometry("1000x600")

fr_haberler = Frame(window, height=600)
fr_buttons = Frame(window, relief= RAISED , bg="pink", bd=2)

btn_son_dakika = Button(fr_buttons, text="Son Dakika", font=('Helveticabold',14), bg="lightblue",command= son_dakika_command)
btn_dunya = Button(fr_buttons, text="Dünya", font=('Helveticabold',14), bg="lightblue",command= dunya_command)
btn_ekonomi = Button(fr_buttons, text="Ekonomi", font=('Helveticabold',14), bg="lightblue",command= ekonomi_command)
btn_saglik = Button(fr_buttons, text="Sağlık", font=('Helveticabold',14), bg="lightblue",command= saglik_command)

btn_son_dakika.grid(row=0,column=0,sticky="ew",padx=5,pady=5)
btn_dunya.grid(row=1,column=0,sticky="ew",padx=5,pady=5)
btn_ekonomi.grid(row=2,column=0,sticky="ew",padx=5,pady=5)
btn_saglik.grid(row=3,column=0,sticky="ew",padx=5,pady=5)

fr_buttons.grid(row=0,column=0,sticky="ns")
fr_haberler.grid(row=0,column=1,sticky="nsew")

window.mainloop()