from pytube import YouTube
link = input("Please enter video URL:")
video = YouTube(link)
print("The Title is:- \n \t*",video.title)
print("The Views are:- \n \t*", video.views)
print(" The likes are:- \n \t*",video.rating)
print("The duration is:- \n \t*",video.length)
if video.length > 120:
    print("Video is longer than 2 minutes:")
    answer = input("Do you want to download it? Yes or No:")
    if answer == "yes":
        print("downloading..")
        video = video.streams.get_highest_resolution().download()
else:
    print("downloading..")
    video = video.streams.get_highest_resolution().download()
