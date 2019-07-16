import io
import os
import subprocess

def mergeAudioVideo(frameSize):
    file = open("videos/videosList.txt", "w+")

    for num in range(frameSize):
        file.write("file 'video" + str(num+1) + ".mp4'\n")

        command = "ffmpeg -loop 1 -y -i images/frame{frame}.png -i audios/frame{frame}.wav -shortest videos/video{frame}.mp4".format(frame=num+1)
        subprocess.call(command,shell=True)
    
    file.close()

def mergeVideos(frameSize, title):
    command = "ffmpeg -f concat -safe 0 -i videos/videosList.txt -c copy done/done.mp4"
    subprocess.call(command, shell=True)

def createVideo(frameSize, title):
    mergeAudioVideo(frameSize)
    mergeVideos(frameSize, title)