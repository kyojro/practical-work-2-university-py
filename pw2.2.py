import sys

say: str = input()
if "Hello, my friend" in say:
    print("good!")
else:
    print("not good")


def func_1():
    print("True1.0")
    if "Hello, my friend" in say:
        return print("good!")
    else:
        return print("not good")


def func_2():
    print("True2.0")
    if "Hello, my friend" in say:
        return print("good!")
    else:
        return print("not good")


def func_3():
    print("True3.0")
    if "Hello, my friend" in say:
        return print("good!")
    else:
        return print("not good")


if sys.argv[1] == "1":
    func_1()
if sys.argv[2] == "2":
    func_2()
if sys.argv[3] == '3':
    func_3()
