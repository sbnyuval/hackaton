import tkinter as tk
import dictionary
from menufunc import menu
STAFF_JOB = []
JOBS_LIST = ['teacher','counselor','maintenance']
num_of_School_staff = ['0','1','2','3']
def enter_new_teachers_to_school_system(STAFF_JOB,num_of_school_staff, JOBS_LIST):
    # רשימה שמכילה כמות מקסימום של מורים בבית ספר
    num_of_School_staff = []
    for i in range(1,201):
        num_of_School_staff.append(str(i))
    # הכנסת מידע על ידי משתמש- בדיקה שהערך הוא בטווח הרצוי והרצת לולאה שרצה לפי מספר המורים שרוצים להוסיף
    num_staff = "Enter number of School staff: "
    num = menu(num_staff)
    if num in num_of_School_staff:
        pass
    else:
        while num not in num_of_School_staff:
            if num == 'exit':
                break
            num = menu(num_staff)

    STAFF_NAMES_AND_JOBS = []
    STAFF_GRADES = []
    STAFF_JOB = []
    staff_name="Enter new staff name: "
    job_name="Enter job name: "
    num=int(num)
    for i in range(num):
        teacher = menu(staff_name)
        JOB = menu(job_name)
        if JOB.lower in JOBS_LIST:
            pass
        else:
            while JOB.lower not in JOBS_LIST:
                if JOB.lower == 'exit':
                    break
                JOB = menu(job_name)
        possible_grades_per_teacher=['10','11','12']
        num_of_grades_per_teacher="Enter number of Grades: "
        NUM_OF_STAFF_GRADES=menu(num_of_grades_per_teacher)
        grades="Enter Grade: "
        if NUM_OF_STAFF_GRADES in possible_grades_per_teacher:
            pass
        else:
            while NUM_OF_STAFF_GRADES not in possible_grades_per_teacher:
                if NUM_OF_STAFF_GRADES == 'exit':
                    break
                NUM_OF_STAFF_GRADES = menu(grades)
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
                        GRADES = menu(grades)
                GRADES = int(GRADES)
                STAFF_NAMES_AND_JOBS[i][j]=GRADES
        else:
            continue
enter_new_teachers_to_school_system(STAFF_JOB,num_of_School_staff,JOBS_LIST)