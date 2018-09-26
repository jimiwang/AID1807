# s.py
class Student:
    L=[]    #用来存储学生信息
    count = 0  #用来记录学生数量

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
        self.__class__.count+=1
        self.__class__.L.append(self)
    @staticmethod
    def input_student():
        while True:
            n=input("请输入学生姓名：")
            if n=='':
                break
            try:
                a=int(input("请输入年龄："))
                s=int(input('请输入成绩：'))
            except ValueError:
                print("输入有误，请重新输入！")
            Student(n,a,s)

Student.input_student()
print(Student.L,Student.count)
print(Student.L[1].name)