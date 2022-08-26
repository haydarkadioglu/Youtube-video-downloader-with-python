import os
import pytube as yt


url = input("input url: ")

while True:
    try:
        yt.YouTube(url)
        break
    except Exception as e:
        print(e)
        url = input("try again: ")

vid = yt.YouTube(url)


oldna = vid.title + ".mp4"
newna = vid.title + ".mp3"

print("video title: ", vid.title)

cho1 = int(input("for music 1, for video 2: "))

if cho1 == 1:
    down = vid.streams.filter(progressive=False ,file_extension="mp4", type="audio")
elif cho1 == 2:
    down = vid.streams.filter(progressive=True, file_extension="mp4", type="video")

for i,a in enumerate(down):
    print(i+1, a)

cho = int(input("choose one: "))

try:
    down[cho-1].download()
except Exception as erro:
    print(erro)
finally:
    print("create new file")

print("dowmloading...")

if cho1 == 1:
    try:
        os.rename(oldna, newna)
    except Exception as er:
        print("ERROR: ", er)


print("done")

