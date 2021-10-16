from pytube import YouTube

url = input('Type youtube url : ')
yt = YouTube(url)
print(yt.title)
