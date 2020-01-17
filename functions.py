def rectangle(w, h):
    return w * h


def func_void(a):
    print(a)


def func_return_multi(a, b):
    return a, b


print(rectangle(70, 30))
a, b = func_return_multi(20, 45)
print(a, b)

func_void(30)
