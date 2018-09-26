# student_input.py
import Student
def student_input():
    L=[]
    while True:
        try:
            print("输入开始")

            name=input("请输入学生姓名：")

            if name == '':
                print(L)
                return L
            age=int(input("请输入学生年龄："))
            score=int(input("请输入学生成绩："))
            
            L.append(Student(name,age,score))
        except:
            print("输入有误,请重新输入!")
    return L

def write_file(L):
    try:
        f=open('si.txt','wt')
        for x in L:
            f.write('\n')

            for y in x:
                if x[y]==x['name']:
                    f.writelines('name:')
                    f.write(str(x[y]))
                    f.write(' ')
                if x[y]==x['age']:
                    f.write('age:')
                    f.write(str(x[y]))
                    f.write(' ')

                if x[y] == x['score']:
                    f.write('score:')
                    f.write(str(x[y]))
                    f.write('  ')
        f.close()
        print("存入完成！")
    except OSError:
        print("存入失败！！")
write_file(student_input())
def read_file(filename='si.txt'):
    f=open(filename,'rt')
    s=f.read()
    print(s)
    f.close()
read_file()