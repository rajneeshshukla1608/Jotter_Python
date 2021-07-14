from tkinter import *
import tkinter.messagebox as box
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)


def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def savefile():
    global file
    if file is None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt",
                                 filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(TextArea.get(.0, END))
            f.close()

            root.title(os.path.basename(file) + "- Notepad")
            print("file saved")
    else:
        f = open(file, "w")
        f.write(TextArea.get(.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate(("<<Cut>>"))


def copy():
    TextArea.event_generate(("<<Copy>>"))


def paste():
    TextArea.event_generate(("<<Paste>>"))


def about():
    box.showinfo("About", "This Notepad by Rajneesh Shukla for more - Help>Devinfo")


def devinfo():
    box.showinfo("Rajneesh Shukla", "Love to devlop new things")


if __name__ == '__main__':
    # Basic Tkinter setup
    root = Tk()
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("notepad.ico")
    root.geometry("644x788")

    # Adding text area
    TextArea = Text(root, font="lucida 12")
    TextArea.pack(expand=True, fill=BOTH)
    file = None
    # let create  a menu bar
    MenuBar = Menu(root)
    # file menu starts here
    fileMenu = Menu(MenuBar, tearoff=0)
    # to open new file
    fileMenu.add_command(label="New", command=newfile)

    # To open already existing file
    fileMenu.add_command(label="Open", command=openfile)

    # To save the current file
    fileMenu.add_command(label="Save", command=savefile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)
    MenuBar.add_cascade(label="File", menu=fileMenu)
    # file menu ends here

    # Edit menu starts here
    EditMenu = Menu(MenuBar, tearoff=0)
    # To give a feature of cut
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # edit menu ends here

    # help menu starts

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    HelpMenu.add_command(label="Dev Info", command=devinfo)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    # help menu ends here

    root.config(menu=MenuBar)

    # Adding Scrollbar
    scroll = Scrollbar(TextArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scroll.set)

    root.mainloop()
