import tkinter as tk
import consts
def get_variable_value(inp):
    valueresult.set( inp.get())
student_menu=['1','2','3']
firstcarrier = consts.restcarrier
subjectcarrier = consts.restcarrier
window = tk.Tk()
window.geometry('1000x500')
valueresult = tk.StringVar()
user = tk.StringVar()
labell = tk.Label(window, text = 'how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                  '2. I would like to report an issue to do with the school\n 3. Im having other problams id like to report').pack()
box = tk. Entry(window, justify='left', textvariable = user).pack()
button = tk.Button(window, text='Enter', command= lambda:[get_variable_value(user),window.destroy()]).pack()



window.mainloop()
firstcarrier = user.get()
if firstcarrier in student_menu:
    pass
else:
    while firstcarrier not in student_menu:
        if firstcarrier == 'exit':
            window.destroy
            break
        window = tk.Tk()
        window.geometry('1000x500')
        valueresult = tk.StringVar()
        user = tk.StringVar()
        labell = tk.Label(window, text='(you must pick a num between 1-4)\n how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problams id like to report').pack()
        box = tk.Entry(window, justify='left', textvariable=user).pack()
        button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()


        window.mainloop()
        firstcarrier = user.get()
if firstcarrier == '1':
    firstcarrier = consts.restcarrier
    window = tk.Tk()
    window.geometry('1000x500')
    valueresult = tk.StringVar()
    user = tk.StringVar()
    labell = tk.Label(window,
                      text='what subject do you need help with? \n(choose number)\n1.English\n2.Math\n3.citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History ').pack()
    box = tk.Entry(window, justify='left', textvariable=user).pack()
    button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()
    window.mainloop()
if firstcarrier == '2':
    window = tk.Tk()
    window.geometry('1000x500')
    valueresult = tk.StringVar()
    user = tk.StringVar()
    labell = tk.Label(window,
                      text='What Issues whould you like to report?\n Issues with teachers\nissues with school programs\nissues with the timetable of the school\nissues with school products.').pack()
    box = tk.Entry(window, justify='left', textvariable=user).pack()
    button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()
    window.mainloop()





