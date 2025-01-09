import sounddevice
import numpy as np
import pygame
import time

pygame.init()

pygame.mixer.init()

pygame.mixer.music.load("sfx1.mp3")

def audio_callback(indata, frames, time, status):
    volume_norm = np.linalg.norm(indata) * 10
    print("Volume: ", volume_norm)
    if volume_norm > 100 and not pygame.mixer.get_busy():
        pygame.mixer.music.play()
        time.sleep(2)
        
with sounddevice.InputStream(callback = audio_callback):
    while True:
        pass