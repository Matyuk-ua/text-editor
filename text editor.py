from tkinter import *
import tkinter as tk
from tkinter.filedialog import asksaveasfilename
from tkinter import messagebox, filedialog

#вікно редактора
text_editor = Tk()
text_editor.geometry('600x600')
text_editor.title('File editor')

#текстове поле
text_fild = Text(
    bg="white",
    fg="black",
    padx=10,
    pady=10,
    wrap=WORD,
    insertbackground='black',
    selectbackground='blue',
    font="Arial 14 ",
    spacing3=10,
    width=20
)
#глобальна змінна, зберігає стиль
global saved_style
saved_style = ""
global saved_size
saved_size = 14

#поле вводу розміра тексту
entry_widget = tk.Entry(text_editor)
entry_widget.pack(pady=10)

# скролбар
text_fild.pack(expand=1, fill=BOTH, side=LEFT)
scroll = Scrollbar( command=text_fild.yview)
scroll.pack(side=LEFT, fill=Y)
text_fild.config(yscrollcommand=scroll.set)

#функція збереження
def save():
 filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
 text_editor.title(f"Entitled - {filepath}")

#функція відкриття файлу
def Open():
    file_path = filedialog.askopenfilename(title='File select', filetypes=(("Text (*.txt)","*.txt"),("All files","*.*")))
    if file_path:
        text_fild.delete("1.0",END)
        text_fild.insert("1.0",open(file_path, encoding="utf-8").read()) #відкриття нового файлу
        
#функція встановлення розміру
def Font_size():
    size = entry_widget.get() #змінна зберігає розмір введений в поле вводу
    if size.isdigit(): #перевірка на ціле число
        size = int(size) #переведення тексту в число
        global saved_size #глобальна змінна зберігає розмір для використання
        saved_size = size  #в інших функціях, щоб стиль не змінювався
        text_fild.tag_add("all_text", "1.0", "end") #виділення всьго тексту
        text_fild.tag_configure("all_text", font=("Arial", size, saved_style)) #зміна розміру
    else:
        messagebox.showerror("error","Not number")#повідомлення про помилку якщо введене не ціле число

#функція зміни стилю
def apply_style(style):
    global saved_style #глобальна змінна зберігає стиль для використання
    saved_style = style #в інших функціях, щоб стиль не змінювався
    text_fild.tag_add("all_text", "1.0", "end") #виділення всьго тексту
    text_fild.tag_configure("all_text", font=("Arial", saved_size, style)) #зміна стилю

#кнопка зміни тексту
change_button = tk.Button( text="Збільшити текст", command=Font_size)
change_button.pack()
change_button.place(x=5, y=5)

#меню
main_menu = Menu(text_editor)

#меню команд для файлу
file_menu = Menu(main_menu,tearoff=0) 
file_menu.add_command(label='Save',accelerator='Ctrl+S',command=lambda: save()) #меню зберігання файлу
file_menu.add_command(label='Open',accelerator='Ctrl+O',command=lambda: Open()) #меню відкриття файлу

#меню команд для тексту
font_menu = Menu(main_menu,tearoff=0)
style_menu_sub = Menu(font_menu,tearoff=0)
style_menu_sub.add_command(label="italic",command= lambda: apply_style("italic")) #меню курсива
style_menu_sub.add_command(label="bold",command= lambda: apply_style("bold")) #меню жирного тексту
style_menu_sub.add_command(label="underline",command= lambda: apply_style("underline"))#меню підкрисленого тексту
style_menu_sub.add_command(label="clear",command= lambda: apply_style("")) #меню звичайного тексту

#довання меню
font_menu.add_cascade(label="Style", menu=style_menu_sub)
main_menu.add_cascade(label="File", menu=file_menu)
main_menu.add_cascade(label="Font", menu=font_menu)

text_editor.config(menu=main_menu)

text_editor.mainloop()