import os
black = "shield_black.bmp"
color = "shield_color.bmp"
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
        pwd = "Champlain"
        print("[+] Encrypted with", x)
        ssl = f"openssl enc -{x} -k {pwd} -in {color1} -out final1"
        os.system(ssl)
        ssl = f"openssl enc -{x} -k {pwd} -in {color2} -out final2"
        os.system(ssl)
        dd = f"dd conv=notrunc if=final1 of=color1.bmp bs=1 count=54"
        os.system(dd)
        dd = f"dd conv=notrunc if=final2 of=color2.bmp bs=1 count=54"
        os.system(dd)
        os.system("cp final1 "/var/www/html/black_enc.html")
        os.system("cp final2 "/var/www/html/color_enc.html")                                                    
        """
        cp bw_html > "/var/www/html/black_enc.html"
        cp color_html > "/var/www/html/color_enc.html"
        #dd conv=notrunc if=/color.bmp of=color2.bmp bs=1 count=54
        #os.system( dd conv=notrunc if=color1 of=color1.bmp bs=1 count=54)
        #os.system( dd conv=notrunc if=color2 of=color2.bmp bs=1 count=54)
        #os.system(openssl enc x -k pwd -in color1 -out color1)
        #os.system(openssl enc  x - k pwd - in color1 - out color1)
        """
        #os.system(openssl x color)
check(black,color)