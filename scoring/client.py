import getpass
import models
import os

def clear_screen():
    os.system('clear')

while True:
    try:
        print "Flag Verification Service!\n"
        username = raw_input("Username: ")
        password = getpass.getpass()
        flag = raw_input("Flag: ")
        clear_screen()
        print models.submit_flag(username, password, flag)
        raw_input("> PRESS ENTER TO CONTINUE")
        clear_screen()
    except:
        continue
