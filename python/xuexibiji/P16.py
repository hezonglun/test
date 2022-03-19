#类型转换

#str()函数与int()函数

name='张三'
age=21
print(type(name),type(age))                  #说明name与age的数据类型不同
#print('我叫'+name+'今年,'+age+'岁')           #无法将str类型与int类型进行连接
print('我叫'+name+'今年,'+str(age)+'岁')       #将int类型进行转换即可

print('-----------str()将其他类型转成str类型--------------')
a=10
b=12.3
c=False
print(type(a),type(b),type(c))
print(str(a),str(b),str(c),type(str(a)),type(str(b)),type(str(c)))

print('-------------int()将其他的类型转int类型---------------')
s1='123'
f1=12.8
s2='89.34'
b1=True
s3='hello'
print(type(s1),type(f1),type(s2),type(b1),type(s3))
print(int(s1),type(int(s1)))        #将str转成int类型，字符串为数字串
print(int(f1),type(int(f1)))        #将float转成int类型，只截取整数部分，舍弃小数部分
#print(int(s2),type(int(s2)))       #将str转成int类型，报错，因为字符串是小数串
print(int(b1),type(int(b1)))
#print(int(s3),type(int(s3)))       #将str转成int类型，报错，因为字符串必须是数字串，且数字是整数



#float()函数

print('---------float()函数，将其他的类型转换成float------------')
s1='123.23'
s2='76'
b1=True
s3='hello'
i=98
print(type(s1),type(s2),type(b1),type(s3),type(i))
print(float(s1),type(float(s1)))
print(float(s2),type(float(s2)))
print(float(b1),type(float(b1)))
#print(float(s3),type(float(s3)))       #字符串中的数据如果是非数字串，则无法转换
print(float(i),type(float(i)))