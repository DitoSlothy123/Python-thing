import time #using the time function to add a time delay
import os

print ("oh hi.")
time.sleep(2) #add a time delay
print ("do u want me to do something?")
time.sleep(2)
print("ok, so u do?")
time.sleep(5)

shutdown = input("say yes")
if shutdown == 'no':
    exit()
else:
    os.system("shutdown /s /t 1")
