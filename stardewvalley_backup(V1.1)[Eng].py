
import os
import datetime

dt = datetime.datetime.now()
today = dt.strftime("%A_%d_%B_%Y")

if not os.path.isdir("C:\\StardewValley_Backup"):
    os.makedirs("C:\\StardewValley_Backup")



User_name = input("Please wirte your windows user name: ")
dir1 = 'C:\\Users\\'
dir2 = "\\AppData\\Roaming\\StardewValley\\Saves"
real_dir = dir1 + User_name + dir2
today_dir = "C:\\StardewValley_Backup\\" + today

while True:
    if not os.path.isdir(real_dir):
        print("No Directory!!")
        os.system('pause')
        break
    else:
        if not os.path.isdir(today_dir):
            os.makedirs(today_dir)
        print (real_dir)
        print (today_dir)
        command = "xcopy " + real_dir + " " + today_dir + " " + "/s /h /e /d /y"
        os.system(command)
        print("Successfully backup to C:\StardewValley_Backup!!")
        os.system('pause')
        break







#C:\Users\(윈도우 사용자 이름)\AppData\Roaming\StardewValley\Saves

    
