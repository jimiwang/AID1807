# enumerate.py
# 写一个程序，输入任意行文字，当输入空行时结束输入
#     打印带有行号的输入结果
#     如：
#         请输入： abcd<回车>
#         请输入： hello<回车>
#         请输入： baby<回车>
#         请输入：<回车>
#     输出如下：
#         第1行： abcd
#         第2行： hello
#         第3行： baby
# 
L=[]    
while True:
    n=input("请输入:")
    if n == '':
        break
    L.append(n)
for x,n in enumerate(L,1):
    print('第',x,'行:',n)

