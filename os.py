import os

path = "\\wsl.localhost\\Ubuntu-20.04\\home\\marcuoware\\text.txt"

if os.path.exists(path):
    print("That location exists")
else:
    print("that location doesn't exist")