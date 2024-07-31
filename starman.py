import tkinter as tk
from tkinter import PhotoImage
import time

class LyricsApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Lyrics")
        self.geometry("720x364")
        
        self.canvas = tk.Canvas(self, width=800, height=600)
        self.canvas.pack()

        self.bg_image = PhotoImage(file="langit.gif")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        self.lyrics = [
            "There's a starman waiting in the sky",
            "He'd like to come and meet us",
            "But he thinks he'd blow our minds",
            "There's a starman waiting in the sky",
            "He's told us not to blow it",
            "'Cause he knows it's all worthwhile",
            "He told me",
            "Let the children lose it",
            "Let the children use it",
            "Let all the children boogie"
        ]

        self.delays = [700, 700, 700, 700, 700, 700, 700, 700, 700, 700]

        self.current_index = 0
        self.current_line = ""
        self.current_char_index = 0

        self.update_lyrics()

    def update_lyrics(self):
        if self.current_index < len(self.lyrics):
            if self.current_char_index < len(self.lyrics[self.current_index]):
                self.current_line += self.lyrics[self.current_index][self.current_char_index]
                self.current_char_index += 1
                self.draw_lyrics()
                self.after(150, self.update_lyrics)
            else:
                self.after(self.delays[self.current_index], self.clear_lyrics)

    def clear_lyrics(self):
        self.current_index += 1
        self.current_line = ""
        self.current_char_index = 0
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)
        self.after(400, self.update_lyrics)

    def draw_lyrics(self):
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.bg_image)

        y = self.winfo_height() // 2
        x = self.winfo_width() // 2

        self.canvas.create_text(x, y, text=self.current_line, fill="white", font=("Serif", 24), anchor="center")


if __name__ == "__main__":
    app = LyricsApp()
    app.mainloop()