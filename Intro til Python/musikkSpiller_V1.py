from pygame import mixer 

# Starting the mixer 
mixer.init() 

# Loading the song 
mixer.music.load("sfx1.mp3") 

# Setting the volume 
mixer.music.set_volume(0.7) 

# Start playing the song 
mixer.music.play() 

while mixer.music.get_busy():
    pass