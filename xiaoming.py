# -*- coding: utf-8 -*-

s1 = 72
s2 = 85

s3= (s2-s1)/s2*100
print ('%.1f%%' %s3)


ss='中文'.encode('utf-8')
print (ss)

s4=ss.decode('utf-8')
print (s4)
print (len(ss))
print  (len(s4))


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print('使用负数',L[-3][-3])
print(L[1][1])
print('使用负数',L[-2][-3])
print(L[2][2])
print('使用负数',L[-1][-1])


classmates = ['Michael', 'Bob', 'Tracy']
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])
print('使用classmates.pop()删除',classmates.pop())
print('classmates =', classmates)


classm  = ('Michael', 'Bob', 'Tracy')
print('classm =', classm)
#定义成tuple,无法更新属性classm[0] = 'Adam'


age = 3
if age >= 18:
    print('adult')
elif  age >= 10:
    print('teenager')
else:
    print ('kid')

