from lab6_adt import *
from lab6_util import *

##############################
# -------------------------- #
# Menus                      #
# -------------------------- #
##############################


def show_menu(slist):
    def cls():
        for i in range(100):
            print()

    cls()
    print('+--------------------------------------------------------+')
    print('|           THE UNIVERSITY OF THE WEST INDIES            |')
    print('|                DEPARTMENT OF COMPUTING                 |')
    print('|                                                        |')
    print('|             S T U D E N T   R E C O R D S              |')
    print('|                                                        |')
    print('|    1.     List All Students                            |')
    print('|    2.     List All Courses for a Specific Student      |')
    print('|    3.     Add a Student                                |')
    print('|    4.     Add/Update a Course and Grade for a Student  |')
    print('|    5.     Delete a Student                             |')
    print('|    6.     Delete a Course and Grade for a Student      |')
    print('|    7.     Queries - ID, Name, Birthday and Other       |')
    print('|    Q.     Quit                                         |')
    print('|                                                        |')
    print('+--------------------------------------------------------+')
    option = input("Enter a selection [1-7 or Q] : ")
    if option not in map(str, list(range(8))) and option not in ['Q', 'q']:
        print()
        input("Incorrect selection - " + option +
              " -.  Press any key to continue.")
        show_menu(slist)
    elif option == '1':
        print_all_students()
    elif option == '2':
        print_courses()
    elif option == '3':
        add_student()
    elif option == '4':
        add_course_grade()
    elif option == '5':
        del_student()
    elif option == '6':
        del_course()
    elif option == '7':
        show_queries_menu(slist)
    elif option in ['q', 'Q']:
        print("Good Bye.")
        exit()
    if option in map(str, list(range(8))):
        print()
        input("Press any key to continue...")
        show_menu(slist)


def show_queries_menu(slist):
    def cls():
        for i in range(100):
            print()

    cls()
    print('+--------------------------------------------------------+')
    print('|           THE UNIVERSITY OF THE WEST INDIES            |')
    print('|                DEPARTMENT OF COMPUTING                 |')
    print('|                                                        |')
    print('|             S T U D E N T   R E C O R D S              |')
    print('|         Queries - ID, Name, Birthday and Other         |')
    print('|                                                        |')
    print('|    1.     List All ID Numbers                          |')
    print('|    2.     List All First Names                         |')
    print('|    3.     List All Student with Early Birthdays        |')
    print('|    4.     List All Student with New IDs                |')
    print('|    5.     List the Total Number of Courses             |')
    print('|    6.     Display Largest ID Number                    |')
    print('|    7.     Display Largest Old ID Number                |')
    print('|    8.     Earliest Birthday                            |')
    print('|    R.     Return to previous menu                      |')
    print('|                                                        |')
    print('+--------------------------------------------------------+')
    option2 = input("Enter a selection [1-8 or R] : ")
    if option2 not in map(str, list(range(9))) and option2 not in ['R', 'r']:
        print()
        input("Incorrect selection - " + option2 +
              " -.  Press any key to continue.")
        show_queries_menu(slist)
    elif option2 == '1':
        print('The List of IDs are ', all_ids(slist))
    elif option2 == '2':
        print('The List of Student First Names are ', first_names(slist))
    elif option2 == '3':
        print('The List of Student with Early Birthdays are :')
        for std in early_birthdays(slist):
            print(std)
    elif option2 == '4':
        print('The List of Student with New IDs are :')
        for std in new_ids(slist):
            print(std)
    elif option2 == '5':
        print('The Total Number of Student Courses is ',
              tot_no_of_courses(slist))
    elif option2 == '6':
        print('The Largest Student ID Number on Record is ',
              largest_id_no(slist))
    elif option2 == '7':
        print('The Largest Student ID Number on Record is ',
              largest_old_id_no(slist))
    elif option2 == '8':
        print('The Earliest Birthdate on Record is ', first_birth_date(slist))
    elif option2 in ['r', 'R']:
        show_menu(slist)
    if option2 in map(str, list(range(9))):
        print()
        input("Press any key to continue...")
        show_queries_menu(slist)


##############################
# -------------------------- #
# Valid Courses and Grades   #
# -------------------------- #
##############################
course_list = {
    'COMP1126': 3,
    'COMP1127': 3,
    'COMP1161': 3,
    'COMP1210': 3,
    'COMP1220': 3,
    'MATH1142': 3,
    'MATH1152': 3,
    'PHYS1411': 3,
    'PHYS1412': 3,
    'PHYS1421': 3
}
grade_list = {
    "A+": 4.3,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "F1": 1.7,
    "F2": 1.3,
    "F3": 0.0
}

############################################
# ---------------------------------------- #
# Additional Student and Course Procedures #
# ---------------------------------------- #
############################################


def is_valid_student_id(slist, sid):
    return sid in map(student_id, slist)


def student_direct_pos(slist, sid):
    for spos in range(len(slist)):
        if student_id(slist[spos]) == sid:
            return spos


def is_valid_course(ccode):
    return ccode in list(course_list)


def is_valid_grade(cgrade):
    return cgrade in list(grade_list)


##############################
# -------------------------- #
# MAIN MENU Procedures       #
# -------------------------- #
##############################


def print_all_students():
    print('The List of All Students is :')
    for std in slist:
        print_students(std)


def print_students(std):
    """Prints the students details"""
    print("Student Id: ", student_id(std))
    print("Name: ", student_fname(student_name(std)),
          student_lname(student_name(std)))
    print("Date of Birth [yyyy-mm-dd]: ", date_yyyy(student_dob(std)), '-',
          date_mm(student_dob(std)), '-', date_dd(student_dob(std)))


def print_courses():
    sid = int(input("Enter Student ID No to Display Student Courses: "))
    if is_valid_student_id(slist, sid):
        spos = student_direct_pos(slist, sid)
        stud_courses = student_courses(slist[spos])
    print("Student ID:", sid)
    for x in stud_courses:
        print("   Course:", x)

def is_valid_grade(cgrade):
    return cgrade in list(grade_list)


def add_student():
    """Adds a student record"""
    sid = int(input("Enter New Student ID No to Add Student : "))
    if not is_valid_student_id(slist, sid):
        fname = input("Enter Student First Name        : ")
        lname = input("Enter Student Last Name         : ")
        dob_yy = int(input("Enter Student Birth Year [yyyy] : "))
        dob_mm = int(input("Enter Student Birth Month  [mm] : "))
        dob_dd = int(input("Enter Student Birth Day    [dd] : "))
        std = make_student(sid, fname, lname, dob_yy, dob_mm, dob_dd)
        slist.append(std)
        print("Student Id: ", sid, ", - ", fname, " ", lname, " Added.")
    else:
        print("Student Id - ", sid, " Already Added...")


def add_course_grade():
    """Adds a student course and grade"""
    sid = int(input("Enter Student ID No to Add Course Grade : "))
    if is_valid_student_id(slist, sid):
        ccode = input("Enter Course Code  : ")
        if is_valid_course(ccode):
            cgrade = input("Enter Course Grade : ")
            if is_valid_grade(cgrade):
                add_course(slist, sid, ccode, cgrade)
                print("Student Id: ", sid, ", - ", ccode, " ", cgrade,
                      " Added.")
            else:
                print("Invalid Course Grade - ", cgrade, " ...")
                print("Valid Course Grades are : ", list(grade_list))
        else:
            print("Invalid Course Code - ", ccode, " ...")
            print("Valid Courses are : ", list(course_list))
    else:
        print("Invalid Student Id - ", sid, " ...")


def add_course(slist, sid, ccode, cgrade):
    entered = False
    if is_valid_course(ccode):
        spos = student_direct_pos(slist, sid)
        if student_no_of_courses(slist[spos]) == 0:
            student_courses(slist[spos]).insert(0, make_course(ccode, cgrade))
            tmp = student_no_of_courses(slist[spos]) + 1
            update_no_of_courses(slist[spos], tmp)
        else:
            for cpos in range(student_no_of_courses(slist[spos])):
                if get_ccode(student_courses(slist[spos])[cpos]) == ccode:
                    student_courses(slist[spos]).pop(cpos)
                    student_courses(slist[spos]).insert(
                        cpos, make_course(ccode, cgrade))
                    entered = True
                    break
                elif get_ccode(student_courses(slist[spos])[cpos]) > ccode:
                    student_courses(slist[spos]).insert(
                        cpos, make_course(ccode, cgrade))
                    tmp = student_no_of_courses(slist[spos]) + 1
                    update_no_of_courses(slist[spos], tmp)
                    entered = True
                    break
            if not entered:
                student_courses(slist[spos]).insert(cpos + 1,
                                                    make_course(ccode, cgrade))
                tmp = student_no_of_courses(slist[spos]) + 1
                update_no_of_courses(slist[spos], tmp)
    else:
        print("Invalid Course Code - ", ccode, " ...")


def del_student():
    """Deletes a student record"""
    sid = int(input("Enter Student ID No to be Deleted : "))
    if is_valid_student_id(slist, sid):
        yn = input("Are You Sure [y/n] : ")
        if yn == 'y':
            remove_student(slist, sid)
            print("Student Id - ", sid, " Deleted...")
    else:
        print("Invalid Student Id - ", sid, " ...")


def remove_student(slist, sid):
    if is_valid_student_id(slist, sid):
        for spos in range(len(slist)):
            if student_id(slist[spos]) == sid:
                slist.pop(spos)
                break
    else:
        print("Invalid Student Id - ", sid, " ...")


def del_course():
    """Deletes a student course record"""
    sid = int(input("Enter Student ID No to be Deleted : "))
    if is_valid_student_id(slist, sid):
        ccode = input("Enter Course Code  : ")
        if is_valid_course(ccode):
            yn = input("Are You Sure [y/n] : ")
            if yn == 'y':
                remove_course(slist, sid, ccode)
        else:
            print("Invalid Course Code - ", ccode, " ...")
    else:
        print("Invalid Student Id - ", sid, " ...")


def remove_course(slist, sid, ccode):
    deleted = False
    spos = student_direct_pos(slist, sid)
    for cpos in range(student_no_of_courses(slist[spos])):
        if get_ccode(student_courses(slist[spos])[cpos]) == ccode:
            student_courses(slist[spos]).pop(cpos)
            tmp = student_no_of_courses(slist[spos]) - 1
            update_no_of_courses(slist[spos], tmp)
            print("Student Id: ", sid, ", - ", ccode, " Deleted.")
            deleted = True
            break
    if not deleted:
        print("Student Id: ", sid, ", - ", ccode, " Not Found.")


##############################
# -------------------------- #
# QUERIES MENU Procedures    #
# -------------------------- #
##############################


def all_ids(std_lst):
    return list(map(student_id, std_lst))


def first_names(std_lst):
    return list(map(student_fname, map(student_name, std_lst)))


def early_birthdays(std_lst):
    return list(
        map(stud_data,
            list(filter(lambda std: date_mm(student_dob(std)) <= 6, std_lst))))


def new_ids(std_lst):
    return list(
        map(stud_data,
            filter(lambda std: str(student_id(std))[0:2] == "62", std_lst)))


def tot_no_of_courses(std_lst):
    stud_no_crs_lst = list(map(student_no_of_courses, std_lst))
    return foldr(lambda x, y: x + y, 0, stud_no_crs_lst)


def largest_id_no(std_lst):
    return foldr(max, 0, all_ids(std_lst))


def largest_id_no2(std_lst):
    all_id_lst = list(map(student_id, std_lst))
    return foldr(max, 0, all_id_lst)


def largest_id_no3(std_lst):
    return foldr(max, 0, list(map(student_id, std_lst)))


def largest_id_no4(std_lst):
    return foldr(lambda x, y: max(x, y), 0, list(map(student_id, std_lst)))


def largest_old_id_no(std_lst):
    return foldr(max, \
                 0, \
                 list(map(student_id, \
                  filter(lambda std: str(student_id(std))[0:2] != "62", \
                  std_lst))))


def first_birth_date(std_lst):
    def smaller_dob(dob1, dob2):
        if date_yyyy(dob1) < date_yyyy(dob2):
            return dob1
        elif (date_yyyy(dob1) == date_yyyy(dob2)) and \
             (date_mm(dob1) < date_mm(dob2)):
            return dob1
        elif (date_yyyy(dob1) == date_yyyy(dob2)) and \
             (date_mm(dob1) == date_mm(dob2)) and \
             (date_dd(dob1) < date_dd(dob2)):
            return dob1
        return dob2

    return foldr(smaller_dob, make_date(9999, 12, 31),
                 list(map(student_dob, std_lst)))


##############################
# -------------------------- #
# Initial Student Data Added #
# -------------------------- #
##############################

st1 = make_student(62000050, "Jane", "Doe", 1995, 12, 25)
st2 = make_student(62000001, "John", "Brown", 1990, 7, 6)
st3 = make_student(62000035, "Jack", "Green", 1999, 1, 3)
st4 = make_student(62000021, "Chris", "Brown", 1992, 7, 10)
st5 = make_student(62000034, "Joe", "White", 2000, 4, 20)
st6 = make_student(85000050, "Janet", "Dopa", 1965, 12, 25)
st7 = make_student(90000001, "Johnathan", "Browning", 1970, 7, 6)
st8 = make_student(95000035, "Jackie", "Greene", 1979, 1, 3)
st9 = make_student(99000021, "Christine", "Black", 1982, 7, 10)
st10 = make_student(92000034, "Joette", "Whiteley", 2000, 4, 20)
slist = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10]
add_course(slist, 62000050, 'COMP1126', 'B+')
add_course(slist, 62000050, 'COMP1127', 'A')
add_course(slist, 62000050, 'COMP1210', 'C+')
add_course(slist, 62000050, 'COMP1220', 'A-')
add_course(slist, 62000001, 'COMP1126', 'B')
add_course(slist, 62000001, 'COMP1127', 'A+')
add_course(slist, 62000001, 'COMP1210', 'C')
add_course(slist, 62000001, 'COMP1220', 'B-')
add_course(slist, 62000001, 'MATH1142', 'A-')
add_course(slist, 62000035, 'COMP1126', 'A+')
add_course(slist, 62000035, 'COMP1127', 'A')
add_course(slist, 62000035, 'MATH1142', 'C+')
add_course(slist, 62000035, 'MATH1152', 'F3')
add_course(slist, 62000021, 'PHYS1421', 'F1')
add_course(slist, 62000021, 'COMP1127', 'A-')
add_course(slist, 62000021, 'COMP1210', 'C')
add_course(slist, 62000021, 'COMP1220', 'B+')
add_course(slist, 62000021, 'MATH1142', 'A-')
add_course(slist, 62000034, 'COMP1126', 'A-')
add_course(slist, 62000034, 'COMP1127', 'C')
add_course(slist, 62000034, 'COMP1220', 'B+')
add_course(slist, 90000001, 'COMP1126', 'B')
add_course(slist, 90000001, 'COMP1127', 'A+')
add_course(slist, 95000035, 'COMP1210', 'C')
add_course(slist, 92000034, 'COMP1220', 'B-')
add_course(slist, 92000034, 'MATH1142', 'F2')
add_course(slist, 92000034, 'COMP1127', 'F3')

##############################
# -------------------------- #
# LAUNCH PROGRAM             #
# -------------------------- #
##############################
#show_menu(slist)
