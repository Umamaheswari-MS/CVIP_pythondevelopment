import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("300x100")

        self.select_button = tk.Button(root, text="Select Music", command=self.open_file)
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)

        self.select_button.pack(pady=10)
        self.play_button.pack(pady=10)
        self.pause_button.pack(pady=10)
        self.stop_button.pack(pady=10)

        self.music_file = None
        pygame.mixer.init()

    def play_music(self):
        if self.music_file:
            pygame.mixer.music.load(self.music_file)
            pygame.mixer.music.play()

    def pause_music(self):
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()

    def stop_music(self):
        pygame.mixer.music.stop()

    def open_file(self):
        self.music_file = filedialog.askopenfilename(defaultextension=".mp3", filetypes=[("MP3 Files", "*.mp3")])

if __name__ == "__main__":
    root = tk.Tk()
    music_player = MusicPlayer(root)
    root.mainloop()
