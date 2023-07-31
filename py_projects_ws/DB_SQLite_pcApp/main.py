# Imports =====================================================================
import json
import logging
import random
import time
import threading
import tkinter as tk


# Class - App_MQTT_Cli ========================================================
class App_SQLite:
    def __init__(self, window):
        self.window = window
        
        self.create_widgets()

    def create_widgets(self):
        
        self.window.configure(padx=20, pady=20)
        
        txt_firstName = tk.Label(self.window, text="First name:", foreground="black")
        in_firstName = tk.Entry(self.window)
        txt_lastName = tk.Label(self.window, text="Last name:", foreground="black")
        in_lastName = tk.Entry(self.window)
        txt_email = tk.Label(self.window, text="Email:", foreground="black")
        in_email = tk.Entry(self.window)
        btn_saveToDb = tk.Button(self.window, text="Save to DB", width=15, height=1, command=self.on_btn_saveToDb_clicked)
        
        txt_firstName.grid(row=0, column=0, sticky=tk.W)
        in_firstName.grid(row=0, column=1)
        txt_lastName.grid(row=1, column=0, sticky=tk.W)
        in_lastName.grid(row=1, column=1)
        txt_email.grid(row=2, column=0, sticky=tk.W)
        in_email.grid(row=2, column=1)
        btn_saveToDb.grid(row=3, column=1)
        
        self.window.grid_columnconfigure(0, minsize=50, pad=20)
        self.window.grid_rowconfigure(0, minsize=20, pad=10)
        self.window.grid_rowconfigure(1, minsize=20, pad=10)
        self.window.grid_rowconfigure(2, minsize=20, pad=10)
        self.window.grid_rowconfigure(3, minsize=20, pad=10)
        
    def on_btn_saveToDb_clicked(self):
        print('---')

if __name__ == '__main__':
    #run()
    window = tk.Tk()
    app = App_SQLite(window)
    window.mainloop()


# ##### END OF FILE ###########################################################
