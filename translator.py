from tkinter import *
from tkinter import ttk, messagebox
from translate import Translator

root = Tk()
root.title("Google ÜBERSETZER")
root.geometry("1080x400")

# Dictionary for language codes
language = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'basque': 'eu',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'cebuano': 'ceb',
    'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
    'esperanto': 'eo',
    'estonian': 'et',
    'filipino': 'tl',
    'finnish': 'fi',
    'french': 'fr',
    'galician': 'gl',
    'georgian': 'ka',
    'german': 'de',
    'greek': 'el',
    'gujarati': 'gu',
    'haitian creole': 'ht',
    'hausa': 'ha',
    'hebrew': 'he',
    'hindi': 'hi',
    'hmong': 'hmn',
    'hungarian': 'hu',
    'icelandic': 'is',
    'igbo': 'ig',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'jw',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'lao': 'lo',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'maori': 'mi',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'odia': 'or',
    'pashto': 'ps',
    'persian': 'fa',
    'polish': 'pl',
    'portuguese': 'pt',
    'punjabi': 'pa',
    'romanian': 'ro',
    'russian': 'ru',
    'samoan': 'sm',
    'scots gaelic': 'gd',
    'serbian': 'sr',
    'sesotho': 'st',
    'shona': 'sn',
    'sindhi': 'sd',
    'sinhala': 'si',
    'slovak': 'sk',
    'slovenian': 'sl',
    'somali': 'so',
    'spanish': 'es',
    'sundanese': 'su',
    'swahili': 'sw',
    'swedish': 'sv',
    'tajik': 'tg',
    'tamil': 'ta',
    'telugu': 'te',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'urdu': 'ur',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'xhosa': 'xh',
    'yiddish': 'yi',
    'yoruba': 'yo',
    'zulu': 'zu'
}

def label_change():
    c = combo1.get()
    c2 = combo2.get()
    label1.configure(text=c)
    label2.configure(text=c2)
    root.after(1000, label_change)

def translate_now():
    try:
        text_ = text1.get(1.0, END).strip()
        c3 = combo1.get()
        c4 = combo2.get()
        
        # Find the language codes
        src_lang = language.get(c3, None)
        dest_lang = language.get(c4, None)
        
        print("Text to translate:", text_)
        print("Source language:", src_lang)
        print("Destination language:", dest_lang)
        
        if text_ and src_lang and dest_lang:
            translator = Translator(from_lang=src_lang, to_lang=dest_lang)
            translated_text = translator.translate(text_)
            
            if translated_text:
                print("Translated text:", translated_text)
                text2.delete(1.0, END)
                text2.insert(END, translated_text)
            else:
                messagebox.showerror("Übersetzungsfehler", "Die Übersetzung konnte nicht durchgeführt werden.")
                print("Translation failed")
        else:
            messagebox.showwarning("Eingabefehler", "Bitte geben Sie Text ein, der übersetzt werden soll und wählen Sie die Sprachen korrekt aus.")
    except Exception as e:
        messagebox.showerror("Übersetzungsfehler", f"Bitte versuche es erneut. Fehler: {e}")
        print("Error occurred:", e)

# Icon
image_icon = PhotoImage(file="img/translate.png")
root.iconphoto(False, image_icon)

# Arrow
arrow_image = PhotoImage(file="img/arrows.png")
image_label = Label(root, image=arrow_image, width=150)
image_label.place(x=460, y=50)

combo1 = ttk.Combobox(root, value=list(language.keys()), font="Roboto 14", state="r")
combo1.place(x=110, y=20)
combo1.set("german")

label1 = Label(root, text="german", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

combo2 = ttk.Combobox(root, value=list(language.keys()), font="Roboto 14", state="r")
combo2.place(x=730, y=20)
combo2.set("english")

label2 = Label(root, text="english", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=620, y=50)

f2 = Frame(root, bg="Black", bd=5)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

root.configure(bg="white")

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 italic", activebackground="purple", cursor="hand2", bd=5, bg="red", fg="white", command=translate_now)
translate.place(x=480, y=250)

label_change()

root.mainloop()
