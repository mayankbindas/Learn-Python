#Booleans

list = ["disco", "classical"]
print(bool(list)) #True
print("disco" in list) #True
print("eating" in list) #False
weird = list[0]
# bool = dance is "disco" # not working for unknown reason
print(weird == "disco")

list = []
print(bool(list)) #False

str = "dsdsad"
print(bool(str)) #True

str = ""
print(bool(str)) #False

num = 34324324
print(bool(num)) #True

num = 0
print(bool(num)) #0 is False, negative numbers result in True

a = 10
b = 10
print(a is b)
print(a == b)
