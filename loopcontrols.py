import time
# loop control statements
# break , continue, pass

while True:
    name = input("Enter your Name: ")
    if name != "":
        break

phone_number = "123-4560-4784-54"

for i in phone_number:
    if i == "-":
        continue
    print(i, end="")
    time.sleep(0.5)

for i in range(1,21):
    if i == 13:
        pass
    else:
        print(i)
        time.sleep(1.5)
        