from tkinter import *
from tkinter import ttk, messagebox
from translate import Translator
from PIL import Image, ImageTk

root = Tk()
root.title("Übersetzer")
root.geometry("1080x360")

# Dictionary for language codes and images
language = {
    'afrikaans': 'af',
    'albanian': 'sq',
    'arabic': 'ar',
    'armenian': 'hy',
    'azerbaijani': 'az',
    'belarusian': 'be',
    'bengali': 'bn',
    'bosnian': 'bs',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW',
    'croatian': 'hr',
    'czech': 'cs',
    'danish': 'da',
    'dutch': 'nl',
    'english': 'en',
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
    'hebrew': 'he',
    'hindi': 'hi',
    'hungarian': 'hu',
    'icelandic': 'is',
    'indonesian': 'id',
    'irish': 'ga',
    'italian': 'it',
    'japanese': 'ja',
    'javanese': 'id',
    'kannada': 'kn',
    'kazakh': 'kk',
    'khmer': 'km',
    'korean': 'ko',
    'kurdish (kurmanji)': 'ku',
    'kyrgyz': 'ky',
    'latin': 'la',
    'latvian': 'lv',
    'lithuanian': 'lt',
    'luxembourgish': 'lb',
    'macedonian': 'mk',
    'malagasy': 'mg',
    'malay': 'ms',
    'malayalam': 'ml',
    'maltese': 'mt',
    'marathi': 'mr',
    'mongolian': 'mn',
    'myanmar (burmese)': 'my',
    'nepali': 'ne',
    'norwegian': 'no',
    'pashto': 'ps',
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
    'swedish': 'sv',
    'tajik': 'tg',
    'thai': 'th',
    'turkish': 'tr',
    'ukrainian': 'uk',
    'uzbek': 'uz',
    'vietnamese': 'vi',
    'welsh': 'cy',
    'yiddish': 'he',
}

# Function to load flag images
def load_flag_image(lang_code):
    path = f'img/flags/{lang_code}.png'
    image = Image.open(path)
    image = image.resize((20, 15), Image.BICUBIC)
    return ImageTk.PhotoImage(image)

flag_images = {lang: load_flag_image(code) for lang, code in language.items()}

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

# Custom Combobox with images
class ImageCombobox(ttk.Combobox):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.bind("<<ComboboxSelected>>", self.on_select)
        self.popup = None

    def on_select(self, event):
        value = self.get()
        if value in flag_images:
            self.icon_label.config(image=flag_images[value])

    def set_icon_label(self, label):
        self.icon_label = label

# Combobox 1
combo1 = ImageCombobox(root, value=list(language.keys()), font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("german")

icon_label1 = Label(root, image=flag_images['german'])
icon_label1.place(x=80, y=23)
combo1.set_icon_label(icon_label1)

# Combobox 2
combo2 = ImageCombobox(root, value=list(language.keys()), font="Roboto 14", state="readonly")
combo2.place(x=730, y=20)
combo2.set("english")

icon_label2 = Label(root, image=flag_images['english'])
icon_label2.place(x=700, y=23)
combo2.set_icon_label(icon_label2)

label1 = Label(root, text="FROM", font="segoe 20", bg="orange", height=2, width=27, bd=4, relief=FLAT)
label1.place(x=10, y=50)

f = Frame(root, bg="orange", bd=1)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Roboto 14", bg="white", relief=FLAT, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

label2 = Label(root, text="TO", font="segoe 20", bg="light blue", height=2, width=27, bd=1, relief=FLAT)
label2.place(x=620, y=50)

f2 = Frame(root, bg="light blue", bd=1)
f2.place(x=620, y=118, width=440, height=210)

text2 = Text(f2, font="Roboto 14", bg="white", relief=FLAT, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

root.configure(bg="#F2F2F2")

# Translate button
translate = Button(root, text="Translate", font="Roboto 15 bold italic", bg="light green", command=translate_now)
translate.place(x=480, y=200)

root.mainloop()
