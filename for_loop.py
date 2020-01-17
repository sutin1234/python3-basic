def testLoop():
    for i in range(101):
        f = (i * 9 / 5) + 32
        print("{}C = {:.2f}F".format(i, f))


def for_index():
    myList = ['Python3', 'Go', 'Assambly']
    for i, listData in enumerate(myList):
        print("{}. {}".format(i + 1, listData))


def normal_loop():
    myList = ['Python3', 'Go', 'Assambly']
    for listData in myList:
        print(format(listData))


def normal_loop2():
    myList = [
        ('TH', 'Thailand', 'ไทย'),
        ('US', 'USA', 'สหรัฐ')
    ]
    for listData in myList:
        print(listData)


# testLoop()
# for_index()
# normal_loop()
normal_loop2()
