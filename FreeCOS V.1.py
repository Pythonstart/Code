import time
import os
#-#-#-#-#-#-#-#- Python Plus! -#-#-#-#-#-#-#-#-#-#-#-#-#-#
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait(text):
    time.sleep(text)

name = "user"
user_choise = "0"

def choise():
    user_choise = input("C://" + name + "/>")

choise()

if user_choise == "ver":
    print("Version 1")
    choise()
elif user_choise == "note":
    note = input("note.txt: ")
    choise()
elif user_choise == "thanks":
    print("Hello! You found that! Makers: CKT, References: MS-DOS, Windows. Thank for using!")
    choise()
elif user_choise == "user":
    user_change = input("Name:")
    choise()
