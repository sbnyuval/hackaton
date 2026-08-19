import tkinter as tk
import consts
import menufunc
def get_variable_value(inp):
    valueresult = tk.StringVar()
    valueresult.set( inp.get())
student_menu=['1','2','3']
open_menu_txt = ('how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problams id like to report')
user = menufunc.menu(open_menu_txt)

open_menu_if_error_txt = ('you must pick a num between 1-4)\n how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problams id like to report')



if user in student_menu:
    pass
else:
    while user not in student_menu:
        if user == 'exit':
            break
        user = menufunc.menu(open_menu_if_error_txt)


#if firstcarrier == '1':
 #   firstcarrier = consts.restcarrier
  #  window = tk.Tk()
   # window.geometry('1000x500')
   # valueresult = tk.StringVar()
   # user = tk.StringVar()
   # labell = tk.Label(window,
    #                  text='what subject do you need help with? \n(choose number)\n1.English\n2.Math\n3.citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History ').pack()
    #box = tk.Entry(window, justify='left', textvariable=user).pack()
    #button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()
    #window.mainloop()
#if firstcarrier == '2':
 #   window = tk.Tk()
    #window.geometry('1000x500')
    #valueresult = tk.StringVar()
    #user = tk.StringVar()
    #labell = tk.Label(window,
     #                 text='What Issues whould you like to report?\n Issues with teachers\nissues with school programs\nissues with the timetable of the school\nissues with school products.').pack()
    #box = tk.Entry(window, justify='left', textvariable=user).pack()
    #button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()
    #window.mainloop()





