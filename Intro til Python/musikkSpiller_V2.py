from pygame import mixer 

# Starting the mixer 
mixer.init() 

# Loading the song 
mixer.music.load("sang1.mp3") 

# Setting the volume 
mixer.music.set_volume(0.7) 

# Start playing the song 
mixer.music.play() 

while mixer.music.get_busy():
    print("e for å stoppe\nr for å resume\np for å pause")
    key = input("")
    
    if key == 'p': 
        # Pausing the music 
        mixer.music.pause()      
    elif key == 'r': 
        # Resuming the music 
        mixer.music.unpause() 
    elif key == 'e': 
        # Stop the mixer 
        mixer.music.stop() 
        break
    
