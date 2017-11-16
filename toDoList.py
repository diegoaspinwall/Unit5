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
    else:
        dolist.append(qsearch)
