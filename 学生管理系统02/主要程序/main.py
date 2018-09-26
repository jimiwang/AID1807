# main.py

#学生管理系统的主模块

from menu import *
from student_info import *  
 

def main():
    L=[]
    while True:  
        show_menu()  
        n=input("请选择：")
        if n=='1':
            L+=input_student()
        if n=='2':
            output_student(L)
        if n=='3':
            del_student(L)
        if n=='4':
            amend_student(L)
        if n == '5':
            print_info_by_age_desc(L)
        if n == '6':
            print_info_by_age_asc(L)
        if n == '7':
            print_info_by_score_desc(L)
        if n == '8':
            print_info_by_score_asc(L)
        if n == '9':
            write_file(L)
        if n =='10':
            read_file(filename='si.txt')

        if n=='q':
           break
if __name__=='__main__':

    main()