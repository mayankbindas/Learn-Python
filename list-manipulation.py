foosballers = [
  "Mia",
  "Retta",
  "Augustine",
  "Jin",
  "Waylon",
  "Alphonso",
  "Sage",
  "Hubert",
  "Raymon",
  "Rebecca",
  "Monty",
  "Glen",
  "Christi",
  "Patrice",
  "Craig",
  "Dexter",
  "Wally",
  "Ian",
  "Pat"
]

median = round(len(foosballers)/2)
print("median player: " + foosballers[median])
print(foosballers[median-2], foosballers[median-1], foosballers[median], foosballers[median+1], foosballers[median+2])
foosballers.insert(median, "Average Player")
foosballers[median] = "AVERAGE PLAYER."
foosballers.append("lousy1")
foosballers.append("lousy2")
foosballers.append("lousy3")
foosballers.append("lousy4")
foosballers.append("lousy5")
# print(foosballers)

newMedian = round(len(foosballers)/2)
swapPlayer = foosballers[newMedian]
foosballers[newMedian] = foosballers[median]
foosballers[median] = swapPlayer
print(foosballers)

foosballers.insert(7, "Lacy")
print(foosballers)
foosballers.insert(11, "Omar")
print(foosballers)
foosballers.insert(7, "Otto")
print(foosballers)
print(len(foosballers))
foosballers.insert(-10, "Chauncey")
print(foosballers)

