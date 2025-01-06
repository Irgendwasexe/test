from config import *
import tkinter as tk


def main():
    root = tk.Tk()
    root.title("Testwindow")
    label = tk.Label(root, text="Hello, world!")
    label.pack()
    root.mainloop()

if __name__ == "__main__":
    main()

test = input("hi")
print(test)