import tkinter
from tkinter import ttk

window = tkinter.Tk()
window.title('Hello world app')
window.geometry('200x100')


def say_hello():
    print('Привет!')


hello_button = ttk.Button(window, text='Say hello', command=say_hello)
hello_button.pack()

if __name__ == '__main__':
    window.mainloop()
