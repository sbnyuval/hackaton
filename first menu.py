import tkinter as tk
import consts
import menufunc
def get_variable_value(inp):
    valueresult = tk.StringVar()
    valueresult.set( inp.get())
#תפריט ראשי תלמידים
student_menu=['1','2','3']
open_menu_txt = ('how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problems id like to report')

user = menufunc.menu(open_menu_txt)

open_menu_if_error_txt = ('you must pick a num between 1-4)\n how can we help you today(pick a number)?\n 1.I need help with school?\n'
                                   '2. I would like to report an issue to do with the school\n 3. Im having other problems id like to report')


#לפי הבחירה של התלמיד הוא יופנה לכאן במידה והוכנס מספר שגוי ימשיך לבקש ממנו מחדש עד שיכניס מספר תקין או exit
if user in student_menu:
    pass
else:
    while user not in student_menu:
        if user == 'exit':
            break
        user = menufunc.menu(open_menu_if_error_txt)
# כאן אני מפנה אותו לפי בחירה
user_name = 'Amitai'
num_of_sub =['1','2']
garde_list = ['10','11','12']
subject_list = ['1','2','3','4','5','6','7']
what_garde_txt = 'what garde are you in?(10-12)'
what_garde_error_txt = '(you must choose a grade between 10-12)what garde are you in?'
option_1_txt = 'in what subject can we help you today?\n 1.English\n2.Math\n3.Citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History'
option_1_error_txt = '(you must choose a num in the range:1-7)\n in what subject can we help you today?\n 1.English\n2.Math\n3.Citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History'
option_2_txt =  'what issue whould you like to report?'
option_3_txt = 'what other problems whould you like to report?\n In an urgent situation, you can contact ERAN (Mental Health First Aid) anonymously at any time by calling 1201 or via the ERAN Association website.'
subenglish =  "1.the wave \n 2.the enemy"
subenglishdict ={'1':'the wave','2':'the enemy'}
subenglish_error =  "(you must pick the num of the option you want)\n1.the wave \n 2.the enemy"
submath =  "1.algebra\n 2.geometry"
submath_error =  "(you must pick the num of the option you want)\n1.algebra\n 2.geometry"
subcitizenship = "1.legal rights \n 2.the three authorities"
subcitizenship_error = "(you must pick the num of the option you want)\n1.legal rights \n 2.the three authorities"
subliterature = "1.tehila \n2.the lady and the peddler"
subliterature_error= "you must pick the num of the option you want)\n1.tehila \n2.the lady and the peddler"
subbible = "1.tora \n 2. nevim"
subbible_error = "(you must pick the num of the option you want)\n1.tora \n 2. nevim"
subhebrew = "1. number name \n 2. reading comprehension"
subhebrew_error = "(you must pick the num of the option you want)\n1. number name \n 2. reading comprehension"
subhistory = "1.World War I\n2.World War II"
subhistory_error = "(you must pick the num of the option you want)\n1.World War I\n2.World War II"
if user == '1':
    grade = menufunc.menu(what_garde_txt)
    if grade == 'exit':
        pass
    else:
        while grade not in garde_list:
            grade = menufunc.menu(what_garde_error_txt)
            if grade == 'exit':
                break
        if grade in garde_list:
            pass
            subject = menufunc.menu(option_1_txt)
            if subject == 'exit':
                pass
            else:
                while subject not in subject_list:
                    subject = menufunc.menu(option_1_error_txt)
                    if subject == 'exit':
                        break
                if subject == '1':
                    sub = menufunc.menu(subenglish)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subenglish_error)





                elif subject == '2':
                    sub = menufunc.menu(submath)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(submath_error)

                elif subject == '3':
                    sub = menufunc.menu(subcitizenship)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subcitizenship_error)
                elif subject == '4':
                    sub = menufunc.menu(subliterature)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subliterature_error)
                elif subject == '5':
                    sub = menufunc.menu(subbible)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subbible_error)
                elif subject == '6':
                    sub = menufunc.menu(subhebrew)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subhebrew_error)
                elif subject == '7':
                    sub = menufunc.menu(subhistory)
                    if sub in num_of_sub:
                        pass
                    else:
                        while sub not in num_of_sub:
                            if sub == 'exit':
                                break
                            sub = menufunc.menu(subhistory_error)
                    with open(f"I need help with school{grade}.txt", "a") as file:  # פתיחת קובץ טקסט
                        file.write(f"name:{user_name}\nsubject:History:{sub}")


elif user == '2':
    grade = menufunc.menu(what_garde_txt)
    if grade == 'exit':
        pass
    else:
        while grade not in garde_list:
            grade = menufunc.menu(what_garde_error_txt)
            if grade == 'exit':
                break
        if grade in garde_list:
            issue = menufunc.menu(option_2_txt)

            if issue == 'exit':
                pass
            else:
                for g in garde_list:
                    if grade == g:
                        with open(f"problam_with_school{grade}.txt", "a") as file:  # פתיחת קובץ טקסט
                            file.write(f"The issue: {issue}\n")  # הוספה לקובץ טקסט
                #האישו מוגדר אפשר להעביר אותו
elif user == '3':
    grade = menufunc.menu(what_garde_txt)
    if grade == 'exit':
        pass
    else:
        while grade not in garde_list:
            grade = menufunc.menu(what_garde_error_txt)
            if grade == 'exit':
                break
        if grade in garde_list:
            problem = menufunc.menu(option_3_txt)
            if problem == 'exit':
                pass
            else:
                for g in garde_list:
                    if grade == g:
                        with open(f"problam_with_school{grade}.txt", "a") as file:  # פתיחת קובץ טקסט
                            file.write(f"The problem: {problem}\n")  # הוספה לקובץ טקסט


  #  user = menufunc.menu(option_1_txt)
#elif user == '2':
 #   user = menufunc.menu(option_2_txt)
#elif user == '3':


