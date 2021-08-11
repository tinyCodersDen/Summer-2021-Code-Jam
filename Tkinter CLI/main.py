'''
Tkinter CLI
Author: tinyCodersDen
'''
from tkinter import *
dict1 = {}
def button_clicked():
    print('')
    print('A button got clicked')
while True:
    query = input('$ ')
    if query=='exit':
        break
    else:
        query = query.split(' ')
        if query[0]=='create':
            if query[1]=='window':
                if query[2] not in dict1.keys():
                    root = Tk()
                    root.title(query[2])
                    dict1[query[2]]=root
                else:
                    print('Error: You can\'t keep the same window name twice')
            elif query[1]=='button':
                there = False
                for k,v in dict1.items():
                    if k==query[2]:
                        button1 = Button(v,text = query[3], command=button_clicked)
                        button1.pack()
                        there=True
                if there==False:
                    print('Error: The specified window doesn\'t exist')
            elif query[1]=='text':
                there = False
                for k,v in dict1.items():
                    if k==query[2]:
                        l1 = Label(v,text = query[3])
                        l1.pack()
                        there=True
                if there==False:
                    print('Error: The specified window doesn\'t exist')
        elif query[0]=='rename':
            if query[1] in dict1.keys():
                dict1[query[1]].title(query[2])
            else:
                print('Error: {} doesn\'t exist'.format(query[1]))
