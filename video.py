import sys
from sys import argv
from gtts import gTTS

link = argv[1]
audio = 0

try:
	Wantaudio = argv[2]
	audio = 1
except IndexError:
	audio = 0

import os
proxy = 'http://111503022:ghodakevv15.comp_111503022@10.1.101.150:3128'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

import pafy
video = pafy.new(link)

print '\n'
print 'Video Author: ' + video.author
print 'View Count  : ' + str(video.viewcount)
print 'Video Rating: ' + str(video.rating)
print '\n'

if(audio):
	download = video.getbestaudio()	
else:
	download = video.getbest()

print("Size        : %s" % download.get_filesize())
filename = download.download()

print '\n'
print "File successfully downloaded"

ans = raw_input("Do you want to play the downloaded file?[y/n]:")

if(ans == "y"or ans == "Y"):
	import subprocess
	if(audio):
		subprocess.call(["audacious", video.title + ".webm"])
	else:
		subprocess.call(["mpv", video.title + ".mp4"])
	sys.exit()
else:
	sys.exit()
