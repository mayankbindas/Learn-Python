import time

clothing = [
    "shirt",
    "pant",
    "socks"
]

for item in clothing:
    foldedItem = "Folded " + item
    print(foldedItem)
    
for index, item in enumerate(clothing):
    foldedItem = "Folded " + item
    print(foldedItem)
    print("Total folded: " + str(index+1))
    
print(list(enumerate(clothing)))
    
print(item) #socks

bacteria = "🌭"
generation = 10
for generation in range(0,generation):
    bacteria = bacteria * 2
    print(bacteria)
    time.sleep(0.5)
    
# list of lists
actorRoles = [
    ["Chirs Hemsworth", "Thor"],
    ["Scarlet Johnson", "Black Widow"],
    ["Chris", "Captain America"],
    ["Robert Downey Jr.", "Iron Man"],
    ["Tom", "Spiderman"]
]

print("Featuring:\n=-=-=-=-=-=-=-=-=-=")
for actorRole in actorRoles:
    print(actorRole[0] + " as " + actorRole[1])

print("\nFeaturing:\n=-=-=-=-=-=-=-=-=-=")    
for actor, role in actorRoles:
    print(actor + " as " + role)
