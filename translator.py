from tkinter import *
from tkinter.ttk import Combobox
import googletrans
import textblob
window = Tk()
window.title("Translator")
window.geometry("800x300")

def clear():
    original_textBox.delete(1.0,END)
    translated_textBox.delete(1.0,END)

def translate():
    
    # get key to translate 
    for key,value in languages.items():
        if value == original_combo.get():
            from_language = key

    # get from language key
    
    for key,value in languages.items():
        if value == translated_combo.get():
            to_language = key
    
    words_blob = textblob.TextBlob(original_textBox.get(1.0,END))  
    
    # Translate 
    words = words_blob.translate(from_lang= from_language , to= to_language)  
     
    # add Translated word to text box
    translated_textBox.insert(1.0,words)
languages = googletrans.LANGUAGES

list_languages = list(languages.values())


original_textBox = Text(window,height=10,width=40)
original_textBox.place(x=10,y=10)

translated_textBox = Text(window,height=10,width=40)
translated_textBox.place(x=465,y=10)

original_combo = Combobox(window,width=50,values=list_languages)
original_combo.current(21)
original_combo.place(x=10,y=190)

translated_combo = Combobox(window,width=50,values=list_languages)
translated_combo.current(72)
translated_combo.place(x=465,y=190)

btn_translate = Button(window,text="Translate",font=("Helvetica"),command=translate)
btn_translate.place(x=350,y=60)

btn_clear = Button(window,text="clear",font=("Helvetica"),width=8,command=clear)
btn_clear.place(x=350,y=110)

window.mainloop()