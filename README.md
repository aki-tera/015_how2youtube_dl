# 015_apache_for_win
Create iPhone podcast RSS feed

***
This program can download from Video(can be downloaded  by youtube_dl) by your browser and can create iPhone podcast RSS feed.

function
1. download files from youtube, niconico, etc.
0. login if you have account for each services.

How to use
1. start apache
0. Enter the URL in the browser.  
   ex1)loacalhost:8080 (If "Apache" is running on the same PC)  
   ex2)192.168.1.10:8080(If "Apache" in runnnig on the another PC whchi is 192.168.1.10)  
0. Enter the URL you want to download and click "Get title".  
0. If you can show download's title, click "download".
0. Download complete, click "Return top page".
0. after that, you can download that files.


***
I ran this program with the following execution environment.

Windows10

Python 3.6 + Atom + IDLE

***
Future plan
1. can select youtube option(ex. resolution, voice only, etc.)
0. multi account

***

Python Library
  * youtube_dl
  * cgi
  * cgitb
  * codecs
  * re
  * sys
  * io
  * xml.etree.ElementTree
  * glob
  * os 
  * time
  * email import utils
