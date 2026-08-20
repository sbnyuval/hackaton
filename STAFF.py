import tkinter as tk
import dictionary
from menufunc import menu
def enter_new_teachers_to_school_system():
    num_of_School_staff=[]
    for i in range(200):
        num_of_School_staff.append(str(i+1))
    num_staff="Enter number of School staff: "
    num=menu(num_staff)
    if num in num_of_School_staff:
        pass
    else:
        while num not in num_of_School_staff:
            if num == 'exit':
                break
            num = menufunc.menu(num_staff)

    STAFF_NAMES_AND_JOBS={}
    STAFF_GRADES=[]
    STAFF_JOB=[]
    staff_name="Enter STAFF NAME: "
    job_name="Enter JOB NAME: "
    num=int(num)
    for i in range(num):
        user=menu(staff_name)
        STAFF_NAMES_AND_JOBS[i]=user
        STAFF_JOB = []
        JOB=menu(job_name)
        possible_grades_per_teacher=['0','1','2','3']
        num_of_grades_per_teacher="Enter number of Grades: "
        NUM_OF_STAFF_GRADES=menu(num_of_grades_per_teacher)
        grades="Enter Grade: "
        if NUM_OF_STAFF_GRADES in possible_grades_per_teacher:
            pass
        else:
            while NUM_OF_STAFF_GRADES not in possible_grades_per_teacher:
                if NUM_OF_STAFF_GRADES == 'exit':
                    break
                NUM_OF_STAFF_GRADES = menufunc.menu(grades)
        NUM_OF_STAFF_GRADES=int(NUM_OF_STAFF_GRADES)
        if NUM_OF_STAFF_GRADES!=0:
            for j in range(NUM_OF_STAFF_GRADES):
                GRADES=menu(grades)
                if GRADES in dictionary.dic[1]:
                    pass
                else:
                    while GRADES in dictionary.dic[1]:
                        if GRADES== 'exit':
                            break
                        GRADES = menufunc.menu(grades)
                GRADES = int(GRADES)
                STAFF_NAMES_AND_JOBS[i][j]=GRADES
        else:
            continue