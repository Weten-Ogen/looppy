utensils = {"forks", "spoon", "knife"}
utensils.add("knapkin")

dishes = {'bowl', 'plate', 'cup'}
utensils.update(dishes)
print(utensils)

nation = { 
    "Russia": "Moscow",
    "USA" : "DC", 
    "China": "Beijing"
    
}

print(nation.values())

for key , val in nation.items():
    print(key, val)