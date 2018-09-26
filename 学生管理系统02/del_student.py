# del_student.py

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
L=[{'age': 20, 'name': 'xiaozhang', 'score': 60}, {'age': 21, 'name': 'xiaowang', 'score': 80}, {'age': 22, 'name': 'xiaoli', 'score': 90}]

del_student(L)