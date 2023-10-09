from tkinter import *
from Tkinterdnd2 import *

def drop(event):
    var.set(event.data)

ws = Tkinterdnd.Tk()
ws.title('PythonGuides')
ws.geometry('300x200')
ws.config(bg='#fcba03')

var = StringVar()
Label(ws, text='Path of the Folder', bg='#fcba03').pack(anchor=NW, padx=10)
e_box = Entry(ws, textvar=var, width=80)
e_box.pack(fill=X, padx=10)
e_box.drop_target_register(DND_FILES)
e_box.dnd_bind('<<Drop>>', drop)

lframe = LabelFrame(ws, text='Instructions', bg='#fcba03')
Label(
    lframe, 
    bg='#fcba03',
    text='Drag and drop the folder \nof your choice in the above text field.\n You will notice a path over there.'
    ).pack(fill=BOTH, expand=True)
lframe.pack(fill=BOTH, expand=True, padx=10, pady=10)

ws.mainloop()
