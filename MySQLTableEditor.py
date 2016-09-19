from tkinter import *
import mysql.connector
# import paramiko

def callRequest():
    print('request')

def callUpdate():
    print('update')

njit_SQLServerConnect = {
    'user': 'ar548',
    'password': 'ZTL17pPIc',
    'host': 'sql.njit.edu',
    'database': 'ar548',
    # 'table': 'Students'
}
"""
set up an ssh connection to the NJIT servers to hopefully get past the fact that access
is denied to off campus computers
"""
# TODO below is not working to get around the need for a VPN
# ssh=paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect('afsconnect1.njit.edu', port=22, username='ar548', password='dragonlance115')

# Open the connection to NJIT's MySQL server
connection=mysql.connector.connect(**njit_SQLServerConnect)
cur = connection.cursor()

# query the table
# query = (
#     'SELECT FirstName, MiddleInitial, LastName, Gender '
#     'FROM Students '
#     'WHERE Gender=\'Male\';'
# )
query='SELECT * FROM Students;'

q = cur.execute(query)
r = cur.rowcount

table = list()
tableRow = list()
while True:
    row = cur.fetchone()
    if not row:
        print('ending')
        break
    for i in row:
        # print(i)
        tableRow.append(str(i))
    table.append(tableRow)
    tableRow = list()
    # print("\n")

for i in table:
    print(i)


root = Tk()
labelTitle = Label(root, text="MySQL Table Editor")
labelTitle.grid(row=0, column=0)

buttonFrame = Frame(root)
buttonFrame.grid(row=1, column=0, padx=10, pady=10)
buttonGet = Button(buttonFrame, text = 'Request Table', command = callRequest )
buttonGet.grid(row = 0, column = 0)
buttonUpdate = Button(buttonFrame, text = 'Update Table', command = callUpdate)
buttonUpdate.grid(row = 0, column = 1)

mainTableFrame = Frame(root)
mainTableFrame.grid(row=2, column=0, padx=10, pady=10)

numCols = len(table[0])
numRows = len(table)

tab=[]
c = [None]*numCols
for i in range(numRows):
    tab.append(c)


for i in range(numRows):
    for j in range(numCols):
        tab[i][j] = Entry(mainTableFrame)
        tab[i][j].grid(row=i, column=j, padx=5, pady=5)
        tab[i][j].insert(0, table[i][j])
        # tab[i][j].setvar(table[i][j])
        # e = Entry(mainTableFrame)
        # e.

mainloop()

# Close the connection to NJIT's MySQL server
connection.close()