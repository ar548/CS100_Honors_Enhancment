#import tkinter
from tkinter import *

# root = Tk()
# mainTableFrame = Frame(root)
# mainTableFrame.grid(row = 2, column = 2)
# # root.title = "Project 1 for CS100 Enhancement"
# labelTitle = Label(root, text = "MySQL Table Editor")
# label2 = Label(mainTableFrame, text = "Label 2")
# label3 = Label(mainTableFrame, text = "Label 3")
#
# labelTitle.grid(row = 0,column = 0, columnspan = root.grid_size()[0])
# label2.grid(row = 0,column = 0, columnspan = 2)
# label3.grid(row = 1,column = 1, columnspan = 1)
# mainloop()

'''
root = Tk()
labelTitle = Label(root, text = "MySQL Table Editor")
labelTitle.grid(row = 1, column = 0)
mainTableFrame = Frame(root)
mainTableFrame.grid(row = 2, column = 0, padx=20, pady=20)

numCols = 10    # will be attained through code later
numRows = 4     # again will be attained through code later
tab = []
c = [None]*numCols
for i in range(numRows):
    tab.append(c)

for i in tab:
    print(i)

n = 0
for i in range(numRows):
    for j in range(numCols):
        n = n + 1
        tab[i][j] = Entry(mainTableFrame, textvariable = str(n), text = str(i*j))
        tab[i][j].grid(row = i, column = j, padx=5, pady=5)

mainloop()
'''

'''
############################################################################################
# this will turn into a parser for the update statement
q = [1, 2, 3, 'adfa', 'werq', 'asdf', 5]
slist = list()
for i in q:
    slist.append(str(i))

print(slist)

plist = list()
for i in slist:
    n = ''
    try:
        n = int(i)
        plist.append(n)
        print('int added')
    except ValueError:
        plist.append(i)
print(plist)


###########################################################################################
'''

from tkinter import *

master = Tk()

var = StringVar(master)
var.set("one") # initial value

option = OptionMenu(master, var, "one", "two", "three", "four")
option.pack()

#
# test stuff

def ok():
    print("value is", var.get())
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()