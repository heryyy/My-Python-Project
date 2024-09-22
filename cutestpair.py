import sys
from time import sleep
import time
import tkinter as tk

# Fungsi untuk menampilkan lirik dengan GUI
def display_lyrics_gui():
    # Membuat window
    window = tk.Tk()
    window.title("Lirik Lagu")

    # Mengatur ukuran window (500x300) dan memusatkan posisi window di layar
    window.geometry("500x300")
    window.resizable(False, False)

    # Membuat label untuk menampilkan lirik, dengan teks di tengah
    label = tk.Label(window, text="", font=("Helvetica", 14), anchor="center", justify="center", wraplength=400)
    label.pack(expand=True)

    # Fungsi untuk menampilkan lirik setelah tombol Mulai ditekan
    def start_lyrics():
        # Nonaktifkan tombol setelah ditekan
        start_button.config(state="disabled")

        # Lirik dan delay antar karakter serta antar baris
        lines = [
            ("I know I pop into your head sometimes", 0.08),
            ("Right down the hallway your eyes locked with mine", 0.09),
            ("You saw me coming, saw me coming didn't ya?", 0.08),
            ("But you started running, started running from me", 0.08),
            ("Oh you can keep on running", 0.07),
            ("Running to wherever", 0.08),
            ("Everland and off the shores", 0.09),
            ("Cuz if you don't remember", 0.09),
            ("I'll be here till you recall", 0.10),
            ("No one can love you like I do", 0.10),
            ("So baby think it through", 0.09),
            ("For years and years", 0.08),
            ("I pined for only you my baby", 0.09),
            ("Look at me", 0.07),
            ("I'm still your girl daydreaming", 0.09),
            ("Don't you think we'd be the cutest pair?", 0.10),
            ("The sweetest love out there", 0.08),
            ("I'm just like milk leave me out I'll turn bad", 0.09),
            ("You're just like mocha with that summer tan", 0.09),
            ("You kinda like me, kinda want me don't ya?", 0.08),
            ("You're shooting glances at me way too clearly", 0.09),
            ("Oh you can keep on running", 0.07),
            ("Running to wherever", 0.08),
            ("Everland and off the shores", 0.09),
            ("Cuz if you don't remember, I'll be here till you recall", 0.09),
            ("No one can love you like I do", 0.10),
            ("So baby think it through", 0.09),
            ("For years and years", 0.08),
            ("I pined for only you my baby", 0.09),
            ("Look at me", 0.07),
            ("I'm still your girl daydreaming", 0.09),
            ("Don't you think we'd be the cutest pair?", 0.10),
            ("I know she loves you dearly too", 0.09),
            ("And you want someone new", 0.08),
            ("But 19 years I pined for only you", 0.10),
            ("Baby I'll scream down the hallway", 0.09),
            ("When she is watching", 0.08),
            ("Just so you know how strongly I mean it", 0.09),
            ("No one will love like I do", 0.10),
            ("Yeah", 0.07),
            ("So baby think it through", 0.09),
            ("For years and years", 0.08),
            ("I pined for only you my baby", 0.09),
            ("Take a little chance and see", 0.10),
            ("We were truly meant to be", 0.09),
            ("Yeah I think we'd be the cutest pair", 0.10),
            ("Nobody else compares", 0.09)
        ]

        delays = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.6, 7]

        def show_lyrics(line, char_delay, line_delay, idx):
            if idx >= len(lines):
                return
            text, char_delay = lines[idx]

            # Menampilkan teks karakter demi karakter
            current_text = ""
            for char in text:
                current_text += char
                label.config(text=current_text)
                window.update()
                sleep(char_delay)

            sleep(line_delay)

            window.after(0, lambda: show_lyrics(*lines[idx + 1], delays[idx + 1], idx + 1))

        show_lyrics(*lines[0], delays[0], 0)

    start_button = tk.Button(window, text="Press", font=("Helvetica", 14), command=start_lyrics)
    start_button.pack(pady=10)

    window.mainloop()

display_lyrics_gui()