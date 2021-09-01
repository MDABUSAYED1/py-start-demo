# data assignment is dynamic in python
name = "abu"

# normal printing
print("My name is", name)

# a representation of lists aka array
names = ["abu", "sayed", "nazim"]
print("my name is ", names)

# normal for loop in python
for name in names:
    print("the current name is", name)

# everything in curly brackets are called list aka object
persons = [{"name": "david", "location": "UK", "handsome": True, "intelligent": "maybe"},
           {"name": "chuck", "location": "California", "handsome": False, "intelligent": "n/a"}]

for person in persons:
    print("the current person is ", person)

# here f indicates a formatted string
for person in persons:
    print(f"the current person is {person}")