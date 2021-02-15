name = input("Please type in your name and press Enter ->")
subtotal = float(input("What's your subtotal?"))
taxRate = 0.25
print("Tax owed: " + str(subtotal*taxRate))
print("Total owed: " + str(subtotal + subtotal*taxRate))

name = "John"
print("\nHello " + name + ", it's nice to meet you!\n")

destinations = ["Agra", "Jaipur", "Alwar"]
for city in destinations:
    print(city + " seems like a cool place to go.")
    
weirdString = """Whats is this syntax?

Weird, right?
Even I think so!"""

print(weirdString[2:7])
