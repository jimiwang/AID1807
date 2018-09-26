# project.py
def input_student():
    L=[]
    while True:
        name=input("请输入学生姓名：")

        if name == '':
            print(L)
            return L
        try:    
            age=int(input("请输入学生年龄："))
            score=int(input("请输入学生成绩："))
        except:
            print("输入错误,请重新输入!")
            continue
        d={}
        d['name']=name
        d['age']=age
        d['score']=score
        L.append(d)
    return L
def get_chinese_char_count(x):
    count = 0  # 先假设个数为0
    for ch in x:
        # 如果ch为中文字典,则count 做加一操作
        if ord(ch) > 127:
            count += 1
    return count        
    
    
    
def output_student(L):
    print('+','-'*30,'+','-'*30,'+','-'*30,'+')
    print('|','name'.center(30),'|','age'.center(30),'|',
        'score'.center(30),'|')
    print('+','-'*30,'+','-'*30,'+','-'*30,'+')
    
    for i in L:
        print('|',i['name'].center(30),'|',
            str(i['age']).center(30),'|',
            str(i['score']).center(30),'|')
        print('+','-'*30,'+','-'*30,'+','-'*30,'+')



def del_student(L):
    print(L)
    n=input("请输入您要删除的学生的姓名：")
    s={}
    s['name']=n
    for x in range(len(L)):
        
        if s['name']==L[x]['name']:
            del L[x]
            break
    print(L)
    return L 
def amend_student(L):
    n=input("请输入您要修改的学生的姓名：")
    if n=='':
        return L
    s={}
    s['name']=n
    for x in range(len(L)):
        if s['name']==L[x]['name']:
            age=int(input("请输入修改后的年龄：") )
            score=int(input("请输入修改后的成绩：" ))
            L[x]['age']=age
            L[x]['score']=score
    print(L) 

def print_info_by_score_desc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)


def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d['score']

    L2 = sorted(L, key=get_score)
    output_student(L2)


def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d['age'], reverse=True)
    output_student(L2)


def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d['age'])
    output_student(L2)


def show_menu():
        print("~~~~~~~~~这是分割线~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print('+-----------------------------+')
        print('| 1) 输入学生信息             |')
        print('| 2) 显示学生信息             |')
        print('| 3) 删除学生信息             |')
        print('| 4) 修改学生信息             |')
        print('| 5) 根据学生年龄由高-低排序  |')
        print('| 6) 根据学生年龄由低-高排序  |')
        print('| 7) 根据学生成绩由高-低排序  |')
        print('| 8) 根据学生成绩由低-高排序  |')
        print('| q) 输入q键退出              |')  
        print('+-----------------------------+')
     
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
            


        if n=='q':
           break
main()

    