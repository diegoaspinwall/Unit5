#Diego Aspinwall
#10-16-17
#toDoList.py

dolist = []

print('Valid commands: add, delete, print, quit')
while True:
    qsearch = input('>')
    if 'quit' in qsearch:
        break
    elif qsearch == 'print':
        for w in dolist:
            print(w)
    elif qsearch[:4] == 'add ':
        dolist.append(qsearch[4:])
    elif qsearch[:7] == 'delete ':
        if qsearch[7:] in dolist:
            dolist.remove(qsearch[7:])
        else:
            print('"'+qsearch[7:]+'"','not in List')
    else:
        print('Invalid command')
