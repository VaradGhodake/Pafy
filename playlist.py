import os

proxy = 'http://111503022:ghodakevv15.comp_111503022@10.1.101.150:3128'
os.environ['http_proxy'] = proxy
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

import pafy
playlist = pafy.get_playlist("https://www.youtube.com/watch?v=9bZkp7q19f0&list=PL15B1E77BB5708555")
print "Saving data to the file"

target = open("data.txt", 'w')

for i in range(0, 25):
	target.write(str(playlist['items'][i]['pafy'].viewcount)+ '\n')
	
target.close()
