#!python
import tkinter as tk
import random
import webview

def insert_buttons():
    num_buttons = 8
    global buttons
    buttons = []
    correct_index = random.randint(0, num_buttons - 1)
    for i in range(num_buttons):
        if i == correct_index:
            buttons.append(tk.Button(window, text="Click me", command=hit))
        else:
            buttons.append(tk.Button(window, text="Click me", command=miss))
    for button in buttons:
        button.pack(fill=tk.BOTH, expand=tk.YES)

def hit():
    for button in buttons:
        button.destroy()
    global label
    label = tk.Label(window, text="You hit it!")
    label.pack(fill=tk.BOTH, expand=tk.YES)
    window.after(5000, restart)

def restart():
    label.destroy()
    insert_buttons()

def miss():
    for button in buttons:
        button.destroy()
    label = tk.Label(window, text="Missed it!")
    label.pack(fill=tk.BOTH, expand=tk.YES)
    window.after(5000, restart)

if __name__ == '__main__':
    window = tk.Tk()
    window.title("Choose a button")
    window.geometry("300x500")

    insert_buttons()
    
    window.attributes("-topmost", True)  # Keep the window on top
    webview.create_window("My App", window)
    webview.start()
