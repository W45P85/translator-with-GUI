# pip install googletrans
# pip install textblob

from tkinter import *
from tkinter import ttk,messagebox
import googletrans
import textblob


root=Tk()
root.title("Google ÜBERSETZER")
root.geometry("1080x400")

def label_change():
    c=combo1.get()
    c2=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c2)
    root.after(1000,label_change)

def translate_now():
    global language
    try:
        text_=text1.get(1.0,END)
        c3=combo1.get()
        c4=combo2.get()
        if(text_):
            words=textblob.TextBlob(text)
            lan=words.detect_language()
            for i,j in language.items():
                if(j==c4):
                    lan_=i
                words=words.translate(from_lang=lan,to=str(lan_))
                text2.delete(1.0,END)
                text2.insert(END,words)
    except Exception as e:
        messagebox.showerror("googletrans","please try again")


#icon
image_icon=PhotoImage(file="translate.png")
root.iconphoto(False,image_icon)

#arrow
arrow_image=PhotoImage(file="5631.jpg")
image_label=Label(root,image=arrow_image,width=150)
image_label.place(x=460,y=50)


language=googletrans.LANGUAGES
languageV=list(language.values())
lang1=language.keys()


combo1=ttk.Combobox(root,value=languageV,font="Roboto 14",state="r")
combo1.place(x=110,y=20)
combo1.set("DEUTSCH")

label1=Label(root,text="DEUTSCH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1=Text(f,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1=Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)


combo2=ttk.Combobox(root,value=languageV,font="RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("WÄHLE DIE SPRACHE AUS")

label2=Label(root,text="DEUTSCH",font="segoe 30 bold",bg="white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f2=Frame(root,bg="Black",bd=5)
f2.place(x=620,y=118,width=440,height=210)

text2=Text(f2,font="Robote 20",bg="white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2=Scrollbar(f2)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text1.yview)
text2.configure(yscrollcommand=scrollbar2.set)



root.configure(bg="white")

#translate button
translate=Button(root,text="Translate",font="Roboto 15 italic",activebackground="purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)



label_change()

root.mainloop()
