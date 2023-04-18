def createMap(str) :
    map = dict()
    for char in str:
        if char in map.keys() :
            map[char] = map[char] + 1
        else:
            map[char] = 1
    return map

str = input("Enter your string : ")
print("The generated map is : ")
map = createMap(str)
print(map)
