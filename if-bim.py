# -*- coding: utf-8 -*-
h = input('输入你的身高:')
w = input('输入你的体重:')
height =float(h)
weight =float(w)
bmi= (weight/height) **2 *100
if bmi < 18.5:
    print('你的BMI 指数:%.2f,过轻' %bmi)
elif bmi >= 18.5:
    print('你的BMI 指数:%.2f,正常' %bmi)
elif bmi >=25:
    print('你的BMI 指数:%.2f,过胖' %bmi)
elif bmi >28:
    print('你的BMI 指数:%.2f,肥胖' %bmi)
elif bmi >32:
    print ('你的BMI 指数:%.2f,严重肥胖' %bmi)
    
