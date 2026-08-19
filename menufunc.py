import tkinter as tk
text_menu1= ('how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problams id like to report')

def get_variable_value(inp):
    valueresult = tk.StringVar()
    valueresult.set( inp.get())
def menu(txt):
    window = tk.Tk()
    window.geometry('1000x500')
    user = tk.StringVar()
    labell = tk.Label(window, text=txt).pack()
    box = tk.Entry(window, justify='left', textvariable=user).pack()
    button = tk.Button(window, text='Enter', command=lambda: [get_variable_value(user), window.destroy()]).pack()
    window.mainloop()
    user = user.get()
    return user


