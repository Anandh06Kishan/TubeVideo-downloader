from pytube import YouTube
ques = input('Single/Multiple downloads?[S/M]: ')
if ques == 'S':
	stt = input("Enter the path of the download: ")
	st = input('paste the link: ')
	yt = YouTube(st)
	stream = yt.streams.first()
	print("Downloading...")
	stream.download(stt)
	print('Download completed')
else:
	stt = input("Enter the path of the download: ")
	num = int(input("Total videos to download(2-10):"))
	lis = []
	for i in range(num):
		lis.append(input('paste the link (video {} ):'.format(i+1)))
	print("Downloading..Please wait for sometime..")
	for item in lis:
		yt = YouTube(item)
		stream = yt.streams.first()
		stream.download(stt)
	print("Download Finished")
