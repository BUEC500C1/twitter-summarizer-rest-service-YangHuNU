import os
import subprocess

def generate_video():
    filename = "./images/img_" +"%d" + ".png"
    output = './static/output.mp4'
    subprocess.call(['ffmpeg', '-framerate', '0.33', '-i', filename, output])

if __name__ == "__main__":
	generate_video()