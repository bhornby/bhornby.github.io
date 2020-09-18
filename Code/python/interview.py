#Toms interview ;)
import time
name=input("enter name ")
print(name)
if name=="tom":
    print("my lunch was nicer than yours ")
else:
    hay=input("how are you, good or bad? ")
    print(hay)
print("ok")
age=input("how old are you? ")
print(age)
if str(age)>14:
    print("sorry")
    time.sleep(2)
    print("you must be old")
else:
    print("wow! you must be young! ")
time.sleep(2)
print("thanks")
time.sleep(5)
print(name, age)
