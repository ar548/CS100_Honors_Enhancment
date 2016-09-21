from tkinter import *
import mysql.connector
# import paramiko

"""
TODO add an add row functionality (button)
TODO complete the update table button
TODO (LATER) add functionality to narrow down the table before displaying it
    this should prevent updating so that it is ensured that all fields are filled out

"""


tab = list()
numRows = 0
numCols = 0
sv = list()

def callRequest():
    global tab
    global numRows
    global numCols
    global sv
    print('requesting table')

    query = 'SHOW COLUMNS FROM ' + tableRequested.get() + ';'

    table = list()
    tableRow = list()
    q = cur.execute(query)
    r = cur.rowcount
    while True:
        row = cur.fetchone()
        if not row:
            print('ending SHOW COLUMNS')
            break
        for i in row:
            tableRow.append(str(i))
            break
    table.append(tableRow)
    tableRow = list()

    query = 'SELECT * FROM ' + tableRequested.get() + ';'

    q = cur.execute(query)
    r = cur.rowcount
    while True:
        row = cur.fetchone()
        if not row:
            print('ending SELECT')
            break
        for i in row:
            # print(i)
            tableRow.append(str(i))
        table.append(tableRow)
        tableRow = list()
        # print("\n")

    for i in table:
        print(i)

    numCols = len(table[0])
    numRows = len(table)

    tab = []
    c = [None] * numCols
    for i in range(numRows):
        tab.append(c)

    #sv = [[None]*numCols]*numRows
    svr = list()
    for i in range(numRows):
        for j in range(numCols):
            svr.append(StringVar())
        sv.append(svr)
        svr = list()

    for i in sv:
        print(i)

    for i in range(numRows):
        for j in range(numCols):
            # yes I know that doing it this way is bad practice but I just wanted to make
            # it work.  ill make it better later
            if i == 0:
                tab[i][j] = Label(mainTableFrame, text = table[i][j])
                tab[i][j].grid(row=i, column=j, padx=5, pady=5)
            else:
                sv[i][j].set(table[i][j])
                tab[i][j] = Entry(mainTableFrame, textvariable = sv[i][j])
                tab[i][j].grid(row=i, column=j, padx=5, pady=5)


def callUpdate():
    global tab
    global numRows
    global numCols
    global sv
    updatedTable = list()
    updatedTableRow = list()
    print('update')
    for i in range(numRows):
        for j in range(numCols):
            print(sv[i][j].get())
            updatedTableRow.append(sv[i][j].get())
        updatedTable.append(updatedTableRow)
        updatedTableRow = list()

    for i in updatedTable:
        print(i)



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

root = Tk()
labelTitle = Label(root, text="MySQL Table Editor")
labelTitle.grid(row=0, column=0)

buttonFrame = Frame(root)
buttonFrame.grid(row=1, column=0, padx=10, pady=10)
buttonGet = Button(buttonFrame, text = 'Request Table', command = callRequest )
buttonGet.grid(row = 0, column = 0)
buttonUpdate = Button(buttonFrame, text = 'Update Table', command = callUpdate)
buttonUpdate.grid(row = 0, column = 1)

tableRequested = StringVar(root)
tableRequested.set('Students')
entryFrame = Frame(root)
entryFrame.grid(row = 2, column = 0)
labelRequest = Label(entryFrame, text = 'Table Requested')
labelRequest.grid(row = 0, column = 0)
entryRequest = Entry(entryFrame, textvariable = tableRequested)
entryRequest.grid( row = 0, column = 1)

mainTableFrame = Frame(root)
mainTableFrame.grid(row=3, column=0, padx=10, pady=10)

mainloop()

# Close the connection to NJIT's MySQL server
connection.close()