# Map and str.capitalize
def demo1():
    flowers = ["lily", "rose", "tulip", "jusmine"]
    flower_maps = mapFlower(flowers)
    print("before map {} ".format(flowers))
    print("after map {}".format(flower_maps))


def mapFlower(flowers):
    return list(map(str.capitalize, flowers))


if __name__ == '__main__':
    print(__name__)
    demo1()
