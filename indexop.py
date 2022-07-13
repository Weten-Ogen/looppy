name = "ambiguous"

if(name[0].islower()):
    name = name.capitalize()

print(name)

print(name[:3].upper())
last_name = name[4:].lower()

print(last_name)
print(name[-1:3])