# Healthy Programmer
# Water - water.mp3 - every 35 min - Drank - log
# Eyes - eyes.mp3 - every 30 min - Done - log
# Exercise - exercise.mp3 -  every 45 min - Done - log
from pygame import mixer
from time import time, asctime

#play sound
def musicplay(file,stopper):
    mixer.init()
    mixer.music.load(file)
    #infinite loop
    mixer.music.play(loops=-1)
    while True:
        userip= input()
        if userip == stopper:
            mixer.music.stop()
            break

#log into a file
def log(name ,msg):
    with open(name,"a+") as f:
        f.write(f"{asctime()}- {msg}\n")

#drinking water
def water():
    print("Time to drink water. Enter drank to stop: ")
    musicplay('water.mp3', "drank")
    log("water.txt", "Drank water")

#relax eyes
def eyes():
    print("Time to let your eyes relax. Enter done to stop: ")
    musicplay("eyes.mp3", "done")
    log("eyes.txt", "Eye Relaxing break")

#stay active
def exercise():
    print("Time to exercise. Enter done to stop")
    musicplay("exercise.mp3", "done")
    log("exercise.txt", "Physical Activity")


if __name__ == '__main__':
    #time at the ime of execution stored in var
    watertime = time()
    eyestime = time()
    exercistime = time()
    #intervals for sctivities
    waterinterval = 35*60
    eyesinterval = 30*60
    exerinterval = 45*60
    #endless loop
    while True:
        #current time - time stored in var
        if time()-watertime > waterinterval:
            water()
            #again set time in var to measure diff
            watertime = time()
        if time()-eyestime > eyesinterval:
            eyes()
            eyestime = time()
        if time()-exercistime > exerinterval:
            exercise()
            exercistime = time()
