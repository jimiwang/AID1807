# Student.py

class Student:
    L=[]    #用来存储学生信息
    count = 0  #用来记录学生数量

    def __init__(self,n,a,s):
        self.name = n
        self.age = a
        self.score = s
        self.__class__.count+=1
        self.__class__.L.append(self)


    @classmethod
    def del_student(cls):
        del cls.L[0]
        cls.count-=1

    @classmethod
    def average_score(cls):
        n=0  #用来记录成绩之和
        for i in cls.L:
            n+=i.score
        average_score = n/len(cls.L)
        return average_score
    @classmethod
    def average_age(cls):
        n=0     #用来记录年龄之和
        for i in cls.L:
            n+=i.age
        average_age=n/len(cls.L)
        return average_age

    @classmethod
    def input_student(cls):
        cls('w',1,1)
        cls('s',2,2)
        cls('d',6,6)
        print(cls.L[1].age)


Student.input_student()

print("学生个数是：",Student.count)
print('学生平均年龄是：',Student.average_age())
print('学生平均成绩是：',Student.average_score())
Student.del_student()
print("学生个数是：",Student.count)
print('学生平均年龄是：',Student.average_age())
print('学生平均成绩是：',Student.average_score())

