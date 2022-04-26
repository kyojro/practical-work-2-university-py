import os
from pathlib import Path
from shutil import rmtree
from tkinter import *
from tkinter import messagebox
import sys

root = Tk()

root["bg"] = "#fafafa"
root.title("tool key")
root.geometry("300x80")
root.resizable(width=True, height=True)

Path_1 = Path("/home/ros/Desktop/lb_copy").glob("**/*")

lb_path = "/home/ros/Desktop/lb_copy/lb2.1.py"

Folder_check: str = "/home/ros/Desktop/lb_copy"
txt_check: str = "/home/ros/Desktop/lb_copy/text.txt"


def clear_folder():
    if not os.listdir(Folder_check):
        messagebox.showinfo(title="info", message="your directory is empty")
    else:
        for path in Path_1:
            print(path.name)
            print(dir(path))
            # combine two lines in a format that is expanded systemically as a path to a file/directory
            print(os.path.join(Folder_check, path.name))
            if os.path.join(Folder_check, path.name) == lb_path:
                print("TEST")

            elif path.is_file():
                path.unlink()

            elif path.is_dir():
                rmtree(path)
        messagebox.showinfo(title="info", message="directory clear. End!")
    r = open("text.txt", "w", encoding="utf-8")
    r.writelines("the program has completed its work!")
    r.close()


def close_prog():
    root.destroy()


def func_1():
    print("True1.0")
    return print("the program has completed its work!")


def func_2():
    print("True2.0")
    return print("the program has completed its work!")


def func_3():
    print("True3.0")
    return print("the program has completed its work!")


if sys.argv[1] == "1":
    func_1()
if sys.argv[2] == "2":
    func_2()
if sys.argv[3] == '3':
    func_3()

lb_1 = Label(root, text=" click the clean button to empty the folder ", bg="#fafafa")

closeButton = Button(root, text="     Cancel     ", command=close_prog)

okButton = Button(root, text="     Clear      ", command=clear_folder)

lb_1.place(x=9, y=0)
okButton.place(x=80, y=23)
closeButton.place(x=162, y=23)

root.mainloop()
