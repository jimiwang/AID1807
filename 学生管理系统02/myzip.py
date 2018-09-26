# myzip.py

def myzip(iter1,iter2):
    it1=iter(iter1)
    it2=iter(iter2)
    while True:
        t = (next(it1),next(it2))
        yield t



numbers = [10086,10000,10010,95588]
names = ['中国移动','中国电信','中国联通']
for t in myzip(names,numbers):
    print(t)    