# -*- coding: utf-8 -*-
"""project2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gmJRcsQVui9cv430fl5GLeRKShrt5MTK
"""

import os

import math

import random

import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP + " is your OTP to verify your Email address. "
msg = otp

s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()
s.login("tashuazmi786@gmail.com", "dswzykdvfbopivla")
emailid = input("Enter your email-> ")
s.sendmail('&',emailid,msg)
a = input("Enter Your OTP-> ")
if a == OTP:
    print("Your Email is Verified.")
else:
    print("Please Check your OTP again")