from Student import Student
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
            print("输入有错,请重新输入!")
            continue
        
        L.append(Student(name,age,score))
    return L
       
    
    
    
def output_student(L):
    print('+','-'*30,'+','-'*30,'+','-'*30,'+')
    print('|','name'.center(30),'|','age'.center(30),'|',
        'score'.center(30),'|')
    print('+','-'*30,'+','-'*30,'+','-'*30,'+')
    
    for i in L:
        print('|',i.name.center(30),'|',
            str(i.age).center(30),'|',
            str(i.score).center(30),'|')
        print('+','-'*30,'+','-'*30,'+','-'*30,'+')



def del_student(L):
    print(L)
    n=input("请输入您要删除的学生的姓名：")
    for x in range(len(L)):
        if L[x].name==n:
            del L[x]
            break
    
    return L 
def amend_student(L):
    n=input("请输入您要修改的学生的姓名：")
    if n=='':
        return L
   
    for x in range(len(L)):
        if L[x].name==n:
            age=int(input("请输入修改后的年龄：") )
            score=int(input("请输入修改后的成绩：" ))
            L[x].age=age
            L[x].score=score
    print(L) 

def print_info_by_score_desc(L):
    def get_score(d):  
        return d.score

    L2 = sorted(L, key=get_score, reverse=True)
    output_student(L2)


def print_info_by_score_asc(L):
    def get_score(d):  # d是字典
        return d.score

    L2 = sorted(L, key=get_score)
    output_student(L2)


def print_info_by_age_desc(L):
    L2 = sorted(L, key=lambda d: d.age, reverse=True)
    output_student(L2)


def print_info_by_age_asc(L):
    L2 = sorted(L, key=lambda d: d.age)
    output_student(L2)

def write_file(L):
    try:
        f=open('si.txt','wt')
        for x in L:
            f.write('\n')

            for y in x:
                print(x[y])
                if x[y]==x['name']:
                    f.write('name:')
                    f.write(str(x[y]))
                    f.write('  ')
                if x[y]==x['age']:
                    f.write('age:')
                    f.write(str(x[y]))
                    f.write('  ')
                    

                if x[y] == x['score']:
                    f.write('score:')
                    f.write(str(x[y]))
                    
        f.close()
        print("存入完成！")
    except OSError:
        print("存入失败！！")

def read_file(filename='si.txt'):
    f=open(filename,'rt')
    s=f.read()
    print(s)
    f.close()

