import pytube

url = input("Enter video url: ")

path = "Downloads"
# Location where you want to download the video

pytube.YouTube(url).streams.get_highest_resolution().download(path)
