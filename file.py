text = "this text has been over written"

with open('text.txt' , 'a') as file:
    file.write(text)


with open("text.txt") as file:
    print(file.read(), end=" ")
