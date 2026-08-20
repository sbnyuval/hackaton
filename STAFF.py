import tkinter as tk
import dictionary
from menufunc import menu
JOBS_LIST=['teacher','counselor','maintenance']
# רשימה שמכילה כמות מקסימום של מורים בבית ספר
def max_num_of_new_school_staff():
    num_of_School_staff = []
    for i in range(200):
        num_of_School_staff.append(str(i + 1))
        return num_of_School_staff
def enter_new_teachers_to_school_system():
    num_of_School_staff=max_num_of_new_school_staff()
    # הכנסת מידע על ידי משתמש- בדיקה שהערך הוא בטווח הרצוי והרצת לולאה שרצה לפי מספר המורים שרוצים להוסיף
    num_staff="Enter number of School staff: "
    num=menu(num_staff)
    if num in num_of_School_staff:
        pass
    else:
        while num not in num_of_School_staff:
            if num == 'exit':
                break
            num = menu(num_staff)
    num = int(num)
    STAFF_NAMES_AND_JOBS={}
    staff_name="Enter new staff name: "
    job_name="Enter job name: "
    for i in range(len(STAFF_NAMES_AND_JOBS)+1,num+1):
        staff=menu(staff_name)
        STAFF_NAMES_AND_JOBS[i]=staff
        JOB=menu(job_name)
        if str(JOB) in JOBS_LIST:
            print("as")
            pass
        else:
            while JOB.lower not in JOBS_LIST:
                if JOB.lower == 'exit':
                    break
                JOB = menu(job_name)
        STAFF_NAMES_AND_JOBS[i](staff=JOB)
        if JOB.lower()=='teacher':
            what_grade_do_you_teach='what grade do you teach'
            do_you_teach_more_than_1_grade=menu('do you teach another grade?(if yes-enter the grade number, if not-enter \"no\" ')
            STAFF_TEACHING_GRADE=menu(what_grade_do_you_teach)
            if STAFF_TEACHING_GRADE in dictionary.dic[1]:
                STAFF_NAMES_AND_JOBS[i](staff=STAFF_TEACHING_GRADE)
                pass
            else:
                while STAFF_TEACHING_GRADE in dictionary.dic[1]:
                    if STAFF_TEACHING_GRADE == 'exit':
                        break
            while True:
                STAFF_TEACHING_GRADE = menu(do_you_teach_more_than_1_grade)
                if STAFF_TEACHING_GRADE in dictionary.dic[1]:
                    STAFF_NAMES_AND_JOBS[i](staff=STAFF_TEACHING_GRADE)
                    pass
                elif STAFF_TEACHING_GRADE.lower() == 'no':
                    break
                else:
                    while STAFF_TEACHING_GRADE in dictionary.dic[1]:
                        if STAFF_TEACHING_GRADE == 'exit':
                            break
    print(STAFF_NAMES_AND_JOBS)

enter_new_teachers_to_school_system()
#הבעיה היא בJOB!