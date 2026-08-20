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
garde_list = ['10','11','12']
subject_list = ['1','2','3','4','5','6','7']
what_garde_txt = 'what garde are you in?(10-12)'
what_garde_error_txt = '(you must choose a grade between 10-12)what garde are you in?'
option_1_txt = 'in what subject can we help you today?\n 1.English\n2.Math\n3.Citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History'
option_1_error_txt = '(you must choose a num in the range:1-7)\n in what subject can we help you today?\n 1.English\n2.Math\n3.Citizenship\n4.Literature\n5.Bible\n6.Hebrew\n7.History'
option_2_txt =  'what issue whould you like to report?'
option_3_txt = 'what other problems whould you like to report?\n In an urgent situation, you can contact ERAN (Mental Health First Aid) anonymously at any time by calling 1201 or via the ERAN Association website.'
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
            subject = menufunc.menu(option_1_txt)
            if subject == 'exit':
                pass
            else:
                while subject not in subject_list:
                    subject = menufunc.menu(option_1_error_txt)
                    if subject == 'exit':
                        break
                if subject == '1':
                    pass
                elif subject == '2':
                    pass
                elif subject == '3':
                    pass
                elif subject == '4':
                    pass
                elif subject == '5':
                    pass
                elif subject == '6':
                    pass
                elif subject == '7':
                    pass



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
                pass
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
            pass



  #  user = menufunc.menu(option_1_txt)
#elif user == '2':
 #   user = menufunc.menu(option_2_txt)
#elif user == '3':








