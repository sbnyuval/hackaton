import tkinter as tk
root = tk.Tk()
root.geometry('1000x500')
tk.Label(root,text="Enter number of School staff: ").grid(row=0,column=0)
num_of_School_staff=tk.Entry(root)
num_of_School_staff.grid(row=0,column=1)
root.mainloop()

STAFF_NAMES_AND_JOBS={}
STAFF_GRADES=[]
STAFF_JOB=[]

# for i in range(num_of_School_staff):
#     STAFF_NAMES_AND_JOBS[i]=input("Enter STAFF NAME: ")
#     STAFF_JOB = []
#     STAFF_JOB.append(input("Enter JOB NAME: "))
#     NUM_OF_STAFF_GRADES=int(input("Enter number of Grades: "))
#     if NUM_OF_STAFF_GRADES!=0:
#         for j in range(NUM_OF_STAFF_GRADES):
#             STAFF_NAMES_AND_JOBS[i][j]=int(input("Enter Grade: "))
#     else:
#         continue