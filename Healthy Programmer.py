"""Exercise 7: Healthy Programmer"""

# 9am - 5pm
# Water - water.mp3 (3.5 litres) - Drank - log
# Eyes - eyes.mp3 - every 30 min - EyDone - log
# Physical activity - physical.mp3 every - 45 min - ExDone - log

# Rules
# Pygame module to play audio

from pygame import mixer
from datetime import datetime
from  time import  time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open("mylogs.txt","a") as f:
        f.write(f"{msg} {datetime.now()}\n")


if __name__ == '__main__':
    # musiconloop("water.mp3","stop")
    init_water = time()
    init_eyes = time()
    init_exercise = time()
    watersecs = 30
    eyessecs = 50
    exsecs = 70

    while True:
        if time() - init_water > watersecs:
            print("Water drinking time.Enter 'drank' to stop the alarm" )
            musiconloop('water.mp3','drank')
            init_water = time()
            log_now("Drank Water at")

        if time() - init_eyes > eyessecs:
            print("Eye exercise time.Enter 'doneeye' to stop the alarm")
            musiconloop('water.mp3', 'doneeye')
            init_eyes = time()
            log_now("Eye Relaxed at")

        if time() - init_exercise > exsecs:
            print("Physical activity time.Enter 'donephy' to stop the alarm")
            musiconloop('water.mp3', 'donephy')
            init_exercise = time()
            log_now("Physical activity done at")