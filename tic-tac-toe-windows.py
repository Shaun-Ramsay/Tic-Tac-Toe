import tkinter as tk
import tkinter.font as font

window = tk.Tk()
window.geometry('190x270')
window.resizable(False, False)
window.title('Tic-Tac-Toe')
window.iconbitmap(r"C:\Users\ramsa\Downloads\tic-tac-toe.ico")

frame = tk.Frame(window)
frame.pack()
frame2 = tk.Frame(window)
frame2.pack()

Text = ''
Title = tk.Label(frame, text = 'Tic-Tac-Toe')
Title.grid(row = 0, column = 0, columnspan = 3, pady = 1)

def disable(a):

    try:
        a['state'] = 'disabled'
    except tk.TclError:
        pass

tie = ''
def clear():
    global tie
    global Event
    global Turn
    global event
    #global turn
    Turn = ''
    Event = ''
    tie = ''
    event.destroy()
    #turn.destroy()

def game():

    global Move
    global event
    global Event
    #global turn
    global Turn
    global tie
    global text1
    global text2
    global text3
    global text4
    global text5
    global text6
    global text7
    global text8
    global text9

    Turn = ''
    text1 = '1'
    text2 = '2'
    text3 = '3'
    text4 = '4'
    text5 = '5'
    text6 = '6'
    text7 = '7'
    text8 = '8'
    text9 = '9'

    Move = 1

    event = tk.Label (frame)
    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
    turn = tk.Label(frame, text = "Player X's turn")
    turn.grid(row = 4, column = 0, columnspan = 3, pady = 1)

    
    box1 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box1))
    box1.grid(row = 1, column = 0, padx = 1, pady = 1)

    box2 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box2))
    box2.grid(row = 1, column = 1, padx = 1, pady = 1)

    box3 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box3))
    box3.grid(row = 1, column = 2, padx = 1, pady = 1)

    box4 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box4))
    box4.grid(row = 2, column = 0, padx = 1, pady = 1)

    box5 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box5))
    box5.grid(row = 2, column = 1, padx = 1, pady = 1)

    box6 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box6))
    box6.grid(row = 2, column = 2, padx = 1, pady = 1)

    box7 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box7))
    box7.grid(row = 3, column = 0, padx = 1, pady = 1)

    box8 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box8))
    box8.grid(row = 3, column = 1, padx = 1, pady = 1)

    box9 = tk.Button(frame, text = Text, bg = 'black', fg = 'white', width = 5, height = 3, command=lambda: info(box9))
    box9.grid(row = 3, column = 2, padx = 1, pady = 1)

    def info(box):

        global Move
        global event
        global Event
        global Turn
        #global turn
        global tie
        global new_box1
        global new_box2
        global new_box3
        global new_box4
        global new_box5
        global new_box6
        global new_box7
        global new_box8
        global new_box9
        global text1
        global text2
        global text3
        global text4
        global text5
        global text6
        global text7
        global text8
        global text9

        if Move == 1:
            Row = box.grid_info()['row']
            Column = box.grid_info()['column']
            box.destroy()

            if Row == 1 and Column == 0:
                new_box1 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box1.grid(row = Row, column = Column, padx = 1, pady = 1)
                text1 = new_box1['text']
            elif Row == 1 and Column == 1:
                new_box2 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box2.grid(row = Row, column = Column, padx = 1, pady = 1)
                text2 = new_box2['text']
            elif Row == 1 and Column == 2:
                new_box3 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box3.grid(row = Row, column = Column, padx = 1, pady = 1)
                text3 = new_box3['text']
            elif Row == 2 and Column == 0:
                new_box4 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box4.grid(row = Row, column = Column, padx = 1, pady = 1)
                text4 = new_box4['text']
            elif Row == 2 and Column == 1:
                new_box5 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box5.grid(row = Row, column = Column, padx = 1, pady = 1)
                text5 = new_box5['text']
            elif Row == 2 and Column == 2:
                new_box6 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box6.grid(row = Row, column = Column, padx = 1, pady = 1)
                text6 = new_box6['text']
            elif Row == 3 and Column == 0:
                new_box7 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box7.grid(row = Row, column = Column, padx = 1, pady = 1)
                text7 = new_box7['text']
            elif Row == 3 and Column == 1:
                new_box8 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box8.grid(row = Row, column = Column, padx = 1, pady = 1)
                text8 = new_box8['text']
            elif Row == 3 and Column == 2:
                new_box9 = tk.Button(frame, text = 'X', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box9.grid(row = Row, column = Column, padx = 1, pady = 1)
                text9 = new_box9['text']
        else:
            Row = box.grid_info()['row']
            Column = box.grid_info()['column']
            box.destroy()

            if Row == 1 and Column == 0:
                new_box1 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box1.grid(row = Row, column = Column, padx = 1, pady = 1)
                text1 = new_box1['text']
            elif Row == 1 and Column == 1:
                new_box2 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box2.grid(row = Row, column = Column, padx = 1, pady = 1)
                text2 = new_box2['text']
            elif Row == 1 and Column == 2:
                new_box3 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box3.grid(row = Row, column = Column, padx = 1, pady = 1)
                text3 = new_box3['text']
            elif Row == 2 and Column == 0:
                new_box4 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box4.grid(row = Row, column = Column, padx = 1, pady = 1)
                text4 = new_box4['text']
            elif Row == 2 and Column == 1:
                new_box5 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box5.grid(row = Row, column = Column, padx = 1, pady = 1)
                text5 = new_box5['text']
            elif Row == 2 and Column == 2:
                new_box6 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box6.grid(row = Row, column = Column, padx = 1, pady = 1)
                text6 = new_box6['text']
            elif Row == 3 and Column == 0:
                new_box7 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box7.grid(row = Row, column = Column, padx = 1, pady = 1)
                text7 = new_box7['text']
            elif Row == 3 and Column == 1:
                new_box8 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box8.grid(row = Row, column = Column, padx = 1, pady = 1)
                text8 = new_box8['text']
            elif Row == 3 and Column == 2:
                new_box9 = tk.Button(frame, text = 'O', bg = 'black', fg = 'white', width = 5, height = 3)
                new_box9.grid(row = Row, column = Column, padx = 1, pady = 1)
                text9 = new_box9['text']

        Move *= -1
        if Move == 1 and tie == '':
            Turn = "Player X's turn"
            event.destroy()
            #turn.destroy()
            event = tk.Label(frame, text = Turn)
            event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
        elif Move == -1 and tie == '':
            Turn = "Player O's turn"
            event.destroy()
            #turn.destroy()
            event = tk.Label(frame, text = Turn)
            event.grid(row = 4, column = 0, columnspan = 3, pady = 1)

        try:
            t = ('X','O')
            if text1 == text4 and text1 == text7 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box4['bg'] = 'green'
                    new_box7['bg'] = 'green'
            elif text1 == text4 and text1 == text7:
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box4['bg'] = 'green'
                    new_box7['bg'] = 'green'
            
            elif text2 == text5 and text2 == text8 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text2} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box2['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box8['bg'] = 'green'        
            elif text2 == text5 and text2 == text8:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text2} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box2['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box8['bg'] = 'green'
            
            elif text3 == text6 and text3 == text9 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text3} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box3['bg'] = 'green'
                    new_box6['bg'] = 'green'
                    new_box9['bg'] = 'green'        
            elif text3 == text6 and text3 == text9:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text3} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box3['bg'] = 'green'
                    new_box6['bg'] = 'green'
                    new_box9['bg'] = 'green'
            
            elif text1 == text2 and text1 == text3 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box2['bg'] = 'green'
                    new_box3['bg'] = 'green'        
            elif text1 == text2 and text1 == text3:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box2['bg'] = 'green'
                    new_box3['bg'] = 'green'
            
            elif text4 == text5 and text4 == text6 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text4} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box4['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box6['bg'] = 'green'        
            elif text4 == text5 and text4 == text6:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text4} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box4['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box6['bg'] = 'green'
            
            elif text7 == text8 and text7 == text9 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text7} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box7['bg'] = 'green'
                    new_box8['bg'] = 'green'
                    new_box9['bg'] = 'green'
            elif text7 == text8 and text7 == text9:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text7} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box7['bg'] = 'green'
                    new_box8['bg'] = 'green'
                    new_box9['bg'] = 'green'
            
            elif text1 == text5 and text1 == text9 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box9['bg'] = 'green'
            elif text1 == text5 and text1 == text9:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text1} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box1['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box9['bg'] = 'green'
            
            elif text3 == text5 and text3 == text7 and text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                                event.destroy()
                                #turn.destroy()
                                Event = f"Player {text3} wins!"  
                                event = tk.Label(frame, text = Event)
                                event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                                Event = ''
                                disable(box1)
                                disable(box2)
                                disable(box3)
                                disable(box4)
                                disable(box5)
                                disable(box6)
                                disable(box7)
                                disable(box8)
                                disable(box9)
                                new_box3['bg'] = 'green'
                                new_box5['bg'] = 'green'
                                new_box7['bg'] = 'green'
            elif text3 == text5 and text3 == text7:
                    event.destroy()
                    #turn.destroy()
                    Event = f"Player {text3} wins!"  
                    event = tk.Label(frame, text = Event)
                    event.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                    Event = ''
                    disable(box1)
                    disable(box2)
                    disable(box3)
                    disable(box4)
                    disable(box5)
                    disable(box6)
                    disable(box7)
                    disable(box8)
                    disable(box9)
                    new_box3['bg'] = 'green'
                    new_box5['bg'] = 'green'
                    new_box7['bg'] = 'green'
            
            elif text1 in t and text2 in t and text3 in t and text4 in t and text5 in t and text6 in t and text7 in t and text8 in t and text9 in t:
                #turn.destroy()
                tie = 'Tie!'
                Event = 'Tie!'
                Tie = tk.Label(frame, text = '          Draw!          ')
                frame.columnconfigure(4, weight = 3)
                Tie.grid(row = 4, column = 0, columnspan = 3, pady = 1)
                event.destroy()
                        
        except NameError:
            pass

game()

reset = tk.Button(frame, text = 'Reset', command = lambda: [game(),clear()])
reset.grid(row = 5, column = 1, pady = 1)

watermark = tk.Label(frame, text = 'Made By Shaun Ramsay')
watermark['font'] = font.Font(size = 8)
watermark.grid(row = 6, column = 0, columnspan = 3, pady = 1)

window.mainloop()
