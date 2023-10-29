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
    font="Arial 14 bold",
    spacing3=10,
    width=20
)

#поле вводу розміра тексту
entry_widget = tk.Entry(text_editor)
entry_widget.pack()

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
        text_fild.insert("1.0",open(file_path, encoding="utf-8").read())
        
#функція встановлення розміру
def Font_size():
    size = entry_widget.get()
    if size.isdigit():
        size = int(size)
        current_font = text_fild.tag_configure("selected", font=("Arial", size))
        text_fild.tag_add("selected", tk.SEL_FIRST, tk.SEL_LAST)
    else:
        messagebox.showerror("error","Not")


#кнопка зміни тексту
increase_button = tk.Button(text_fild, text="Збільшити текст", command=Font_size)
increase_button.pack()

#меню
main_menu = Menu(text_editor)

file_menu = Menu(main_menu,tearoff=0)
file_menu.add_command(label='Save',accelerator='Ctrl+S',command=lambda: save())
file_menu.add_command(label='Open',accelerator='Ctrl+O',command=lambda: Open())

font_menu = Menu(main_menu,tearoff=0)
font_menu.add_command(label="change size",command=lambda: Font_size())

main_menu.add_cascade(label="File", menu=file_menu)

text_editor.config(menu=main_menu)

text_editor.mainloop()