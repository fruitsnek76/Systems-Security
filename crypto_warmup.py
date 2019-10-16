import os
black = 1
color = ""
ciphers = ["aes-128-cbc",
"aes-256-cbc",
"des",
"des-ede",
"des-ede3",
"des-ofb",
"aes-128-ecb",
"aes-256-ecb",
"des-cbc",
"des-ede-cbc",
"des-ede3-cbc",
"des3",
"aes-192-cbc",
"des-cfb",
"des-ede-cfb",
"des-ede3-cfb",
"aes-192-ecb",
"des-ede-ofb",
"des-ecb",
"des-ede3-ofb",]
#Iterate through the list
def check(color1,color2):
    for x in ciphers:
        #os.system(openssl x black)
        #dd conv=notrunc if=/color.bmp of=color2.bmp bs=1 count=54
        print("[+]", x)
        os.system(openssl dd conv=notrunc if=color1 of=color1.bmp bs=1 count=54)
        os.system(openssl dd conv=notrunc if=color2 of=color2.bmp bs=1 count=54)
        #os.system(openssl x color)