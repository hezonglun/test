#元组

'''元组的创建方式'''
    #1.直接小括号
t=('python','holle',90)
print(t,type(t))

t2='python','holle',90      #省略小括号
print(t2,type(t2))

    #2.使用内置函数tuple()
t1=tuple(('python','holle',90))
print(t1,type(t1))

    #3.只包含一个元组的元素需要使用逗号和小括号
t3=(10,)

    #空元组的创建
t4=tuple()
print(t4,type(t4))
t5=()
print(t5,type(t5))



'''元组的对象数据更改
a):如果元组中对象本身是不可变对象，则不能在引用其他对象
b):如果元组中对象本身是可变对象，则可变对象的引用不允许改变，但数据可以改变'''
h=(12,[23,45],56)
print(h,type(h))
print(h[0],type(h[0]),id(h[0]))
print(h[1],type(h[1]),id(h[1]))
print(h[2],type(h[2]),id(h[2]))
#尝试将h[1]修改为100
print(id(100))
#h[1]=100        #元组是不允许修改元素的
#由于[23,45]列表，而列表是可变序列，所以可以向列表中添加元素，而列表的内存地址不变
h[1].append(100)        #向列表中添加元素
print(h,id(h[1]))       #列表的内存地址不变




'''元组的遍历    元组是可迭代对象，所以可以使用for...in进行遍历'''
x=('python','world',98)
#1.使用索引
print(x[0])
print(x[1])
print(x[2])
#print(x[3])     IndexError: tuple index out of range
#2.遍历元组
for item in x:
    print(item)