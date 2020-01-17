# ListData Array
listData = ["Code", "Thinnycode", "Python3"]
print(listData)

# ListData with index
print(listData[2])

# ListData is All
for data in listData:
    print(data)

# Append to List
listData.append("AI Language")
print(listData)

# Insert at index of ListData
listData.insert(2, "Computer")
print(listData)

# Remove with text
listData.remove("Computer")
print(listData)

# Remove last index of array
listData.pop()
print(listData)

myList = [0, 2, 0, 3, 4]

# get count dupplicate
print("get dupplicate of 0 is", myList.count(0))

# get index of list
print("index of 4 is ", myList.index(4))

# sort listData ACS
myList.sort()
print(myList)

# sort listData DESC
myList.sort(reverse=True)
print(myList)
