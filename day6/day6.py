with open("inputDay6.txt") as f:
    data = f.read()

# Part 1

for i in range(len(data)):
    checkMarkerList = data[i:i+4]
    checkMarkerSet = set(checkMarkerList)
    if len(checkMarkerList) == len(checkMarkerSet):
        print(i+4)
        break
