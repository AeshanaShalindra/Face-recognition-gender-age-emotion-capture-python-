# Face-recognition-gender-age-emotion-capture-python-
A python code that uses Angus.ai to detect human faces, identify the gender, age and emotions of the user in order to customise advertising and gain feedback 

1. install python 2.7.13
https://www.python.org/downloads/release/python-2713/

set the envirnmet path 

thype python.exe to check version on cmd

2. install angus on cmd

python.exe -m pip install angus-sdk-python

3.install open cv on cmd

python.exe -m pip install opencv-python

4.install numpy on cmd

python.exe -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose

5.config the open cv 
 download opencv 2.4.13-vc14.exe
 go to E:\imperz\opencv\build\python\2.7\x86 and copy cv2.pyd
 past it in C:\Python27\Lib\site-packages

6.set angus.ai stream
https://console.angus.ai/accounts/login/
create account and set stream 
get tokens

Input endpoint:	

https://gate.angus.ai
	
SDK credentials:	
Login
288fc934-ab42-11e7-b63b-0242ac140003
	
Password
f984568e-0588-4fab-9308-6c616882d6c2
 
7.set the stream 

go to on cmd
cd C:\Python27
$ python Scripts\angusme
 and set the token

8. now run the program 

E:\imperz\smart-billboards-master-b7af701fce8891f46f2c5e335e851ef4d9ce809a>face_analysis.py

