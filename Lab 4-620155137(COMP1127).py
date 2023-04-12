def my_map(f,lst):
    if lst == []:
        return []
    else:
        return [f(lst[0])] + my_map(f, lst[1:])

def myzip(lst1,lst2):
    if lst1 ==[] or lst2 == []:
        return []
    else:
        return [(lst1[0],lst2[0])] + myzip(lst1[1:],lst2[1:])

def student(sid,fname,lname, crses):
    """Constructor for student"""
    courses = []
    while crses != []:
        courses += [(crses[0],crses[1])]
        crses = crses[2:]
    return [sid,[fname,lname],courses]

def get_id(std):
    """Returns students ID"""
    return std[0]

def get_name(std):
    """Returns students Name"""
    return std[1]

def get_courses(std):
    """Returns a list of tuples of course codes and grade"""
    return std[2]

def get_fname(name):
    """Returns first name"""
    return name[0]

def get_lname(name):
    """Returns last name"""
    return name[1]

def get_ccode(course_det):
    """Returns course code part of the tuple"""
    return course_det[0]

def get_grade(course_det):
    """Returns grade part of the tuple"""
    return course_det[1]



def compute_letter_grade(num_grade):

    if num_grade > 89:
        return 'A+'

    elif num_grade in range(80,90):
        return 'A'
    elif num_grade in range (75,80):
        return 'A-'

    elif num_grade in range (70,75):
        return 'B+'
    elif num_grade in range (65,70):
        return 'B'
    elif num_grade in range (60,65):
        return 'B-'

    elif num_grade in range (55,60):
        return 'C+'
    elif num_grade in range (50,55):
        return 'C'

    elif num_grade in range (45,50):
        return 'F1'
    
    elif num_grade in range(40,45):
        return 'F2'

    elif num_grade in range (0,40):
        return 'F3'
def calc_letter_grade(std):#extract 
    number_grades_list = my_map(get_grade,get_courses(std))#numbered gradeslist is a list of the numbered grades 
    letter_grades_list= my_map(compute_letter_grade, number_grades_list)#converts letter using the compute letter grade to make a list by using my_map turns into leter format
    course_code_list = my_map(get_ccode,get_courses(std))# a is the list of the coursecodes of the student info
    w = list(zip(course_code_list,letter_grades_list))#add cclist and letter together in a list and return i
    return w #takes a student and returns a list of tuples first part coursecode and second lett grade

    #zip takes two elements and creates two tuples
 #Problem3   
def lookup(dict1, key): #searches the particular dictionary for a key and returns the respective value
    for a in dict1:
        if a == key:
            return dict1[key]

def convert_to_wtqp(c_pair): #creates a list of tuples that contains the course credit and quality point of letter grade in each 
    lst_of_ccode = my_map(get_ccode,c_pair) #getc_code the course code from the pair
    lst_of_ccode_credit = []
    for a in lst_of_ccode: #stores each course code credit in a list
        lst_of_ccode_credit.append(lookup(credit_list, a))
   #     
        
        
    lst_letter_grade = my_map(get_grade,c_pair) #pulls the letter grade from the pair
    
    lst_letter_grade_qp = []
    
    for a in lst_letter_grade: #stores each quality point of each letter grade in a list
        lst_letter_grade_qp.append(lookup(qp_list, a))
        
        
        
    return myzip(lst_of_ccode_credit, lst_letter_grade_qp)

def calc_gpa(std): #calculates the GPA of the particular student 
    
    cw_qp_pair_list = convert_to_wtqp(calc_letter_grade(std)) 
    #produces a list of tuples containing pairs of course credit and quality point
    
    gp_sum_lst = 0
    for a in cw_qp_pair_list:
        gp_sum_lst += get_ccode(a) * get_grade(a)
    #produces the sum of grade points
    
    credit_sum_lst = 0
    for a in cw_qp_pair_list:
        credit_sum_lst += get_ccode(a) 
    #produces the sum of credit hours
   
    
    return gp_sum_lst / credit_sum_lst
    
    
    


def calc_gpa(std): #calculates the GPA of the particular student 
    
    cw_qp_pair_list = convert_to_wtqp(calc_letter_grade(std)) 
    #produces a list of tuples containing pairs of course credit and quality point
    
    gp_sum_lst = 0
    for a in cw_qp_pair_list:
        gp_sum_lst += get_ccode(a) * get_grade(a)
    #produces the sum of grade points
    
    credit_sum_lst = 0
    for a in cw_qp_pair_list:
        credit_sum_lst += get_ccode(a) 
    #produces the sum of credit hours
   
    
    return gp_sum_lst / credit_sum_lst
    
