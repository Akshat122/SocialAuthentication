# SocialAuthentication
The real world does not always include authentic user but also unauthorized user and therefore an approach to building an algorithm that could identify these authentic users from unauthorized ones. The project implemented describes identifying the authorized user of the social networking website. This particular algorithm implemented has a variety of uses in terms of building applications for teaching-learning processes, and can further be developed for implementing high security applications as well. <br><br> Authorized user from real world were also authenticated using the above methods and also with the help of Trusted users method using 6 digit pin . Changes were made to the very first implementation of detecting user so as to differentiate authorized and unauthorized user of that particular account. The changes made were mostly by sending random generated pin of length 6 to the trusted contacts . Some of the part implemented also made use of RSA encryption technology.<br><br> Using RSA, the OSA can generate a random string and encrypt it using the RSA. The private key of the RSA is send to the user and a 6 digit random generated pin is send to the Trusted contacts . The OSN will provide a platform where user have to enter the pin send to the Trusted contact and upload the private key file , only upon successful decryption of the random text the authenticity is proved.
# Screen Shots
![alt text](https://github.com/Akshat122/SocialAuthentication/blob/master/Screen%20shots/1.png)
<br>
![alt text](https://github.com/Akshat122/SocialAuthentication/blob/master/Screen%20shots/2.png)
<br>
![alt text](https://github.com/Akshat122/SocialAuthentication/blob/master/Screen%20shots/3.png)
<br>
![alt text](https://github.com/Akshat122/SocialAuthentication/blob/master/Screen%20shots/4.png)
<br>
![alt text](https://github.com/Akshat122/SocialAuthentication/blob/master/Screen%20shots/5.png)
<br>
# Modules Required
```python
pip install pycrypto
```
# Notes
1. The file RSA.py is coded in python 2 while send_Pin.py and send_Private_key.py is in Python 3.
2. Enter your Email address and password in file send_Pin.py & send_Private_key.py in order to send mail.
3. Don't forget to enter recipient in the same file you entred your password.
4. The module is by default configured to work with gmail.
5. Make sure FTP is enabled in your Gmail account.
6. For any Error/Bugs feel free to create issue or mail me the screenshot at akshat.khanna@st.niituniversity.in.
