import os
black = ""
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

for x in ciphers:
    os.system(openssl x black)
    os.system(openssl x color)