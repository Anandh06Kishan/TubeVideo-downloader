from pytube import YouTube
ques = input('Single/Multiple downloads?[S/M]: ')
if ques == 'S':
	st = input('paste the link: ')
	yt = YouTube(st)
	stream = yt.streams.first()
	print("Downloading...")
	stream.download(r'C:\ashok\videos\youtube downloads')
	print('Download completed')
else:
	num = int(input("Total videos to download(2-10):"))
	lis = []
	for i in range(num):
		lis.append(input('paste the link (video {} ):'.format(i+1)))
	print("Downloading..Please wait for sometime..")
	for item in lis:
		yt = YouTube(item)
		stream = yt.streams.first()
		stream.download(r'C:\ashok\videos\youtube downloads')
	print("Download Finished")
