#!/usr/bin/python2.7

import sys

link = raw_input("Video Link: ")
audiow = raw_input("Only audio? [y/n]")
audio = 0
if(audiow == "y"):
	audio = 1
else:
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
