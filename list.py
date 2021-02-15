list = [
    "elephant",
    "horse",
    "tiger"
]

print(list[0])
print(list[-1]) #tiger
print(list[-2]) # horse
print(list[-3]) #elephant
# print(list[4]) #error
print(list)

list.append("dinosaur")
print(list)

list.insert(1, "ant")
print(list)

list[0] = "married elephant"
print(list)

del list[0]
print(list)

list2 = ["crocodile", "snake", "lizard"]
print(list + list2)
