import tkinter as tk
def get_variable_value(inp):
    valueresult.set( inp.get())
student_menu=['1','2','3']
carrier = "a"
window = tk.Tk()
window.geometry('1000x500')
valueresult = tk.StringVar()
user = tk.StringVar()
labell = tk.Label(window, text = 'how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                  '2. I would like to report a problam\n 3. Im having other problams id like to report').pack()
box = tk. Entry(window, justify='left', textvariable = user).pack()
button = tk.Button(window, text='Enter', command= lambda:[get_variable_value(user),window.destroy()]).pack()



window.mainloop()
carrier = user.get()
if carrier in student_menu:
    pass
else:
    while carrier not in student_menu:
        window = tk.Tk()
        window.geometry('1000x500')
        valueresult = tk.StringVar()
        user = tk.StringVar()
        labell = tk.Label(window, text='(you must pick a num between 1-4)\n how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report a problam\n 3. Im having other problams id like to report').pack()
        box = tk.Entry(window, justify='left', textvariable=user).pack()
        button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()


        window.mainloop()
        carrier = user.get()





