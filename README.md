# 015_youtube_dl2podcast
![](https://img.shields.io/badge/type-python3-brightgreen)  ![](https://img.shields.io/badge/windows%20build-passing-brightgreen) ![](https://img.shields.io/badge/license-MIT-brightgreen)   
![](https://img.shields.io/badge/Server-Apache-red) ![](https://img.shields.io/badge/SmartPhone-iPhone-red)  
![](https://img.shields.io/badge/libraly-youtube_dl-blue)  

## DEMO
### This is a program that can create RSS feeds of videos retrieved by youtube_dl. 
<img src="https://user-images.githubusercontent.com/44888139/143341829-57dc7079-a798-492c-a76f-96ef49b6f089.png" height="400px"> <img src="https://user-images.githubusercontent.com/44888139/143342138-591f85c7-9bf1-4447-9a37-56f53cb3c286.png" height="400px">  <img src="https://user-images.githubusercontent.com/44888139/143227894-ce764aa1-0bbb-4dc8-a9a7-00dba2056ff9.png" height="400px">  

### You can watch the videos registered in RSS with the podcast application on your smartphone.  
<img src="https://user-images.githubusercontent.com/44888139/143238309-2bbc38ef-bfcb-4372-a593-83739317b507.png" height="400px"> 

## Features
If you register the url in the podcast app, you can watch the videos you get from youtube_dl on your phone.

### specification
- 

## Requirement 
Python 3
 - I ran this program with the following execution environment.
   - Windows 10
     - Python 3.9
     - Apache HTTP Server 2.4
   - iPhone11
     - ios 14.8
     - Apple Podcast App

Python Library
  - youtube_dl
  - cgi, cgitb
  - codecs
  - re
  - sys, io, os
  - xml.etree.ElementTree
  - glob
  - email import utils
  - json


Podcast software
  - Apple Podcast App




***
This program can download from Video(can be downloaded  by youtube_dl) by your browser and can create iPhone podcast RSS feed.

function
1. download files from youtube, niconico, etc.
0. login if you have account for each services.

How to use
1. start apache
  - warning : you need that you amend line 208 and 209 on yt_download.py
    - 208: http://***192.168.11.15***/podcast/ --> http://***your IP address***/podcast/
    - 209: http://***192.168.11.15***/podcast/ --> http://***your IP address***/podcast/
0. Enter the URL in the browser.  
   ex1)loacalhost (If "Apache" is running on the same PC)  
   ex2)192.168.11.15(If "Apache" in runnnig on the another PC whchi is 192.168.11.15)  
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
