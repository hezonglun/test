#列表
'''
列表元素按顺序有序排列；可以通过索引找到（1-0；n--n)
通过索引可以确定唯一的数据
可以存储重复数据
任意数据类型混存
根据需要动态分配和回收内存
'''
a=10        #变量存储的是一个对象的引用
lst=['hello','world',123]   #任意数据类型混存
print(id(lst))
print(type(lst))
print(lst)

'''第一种列表创建方式，使用[]'''
lst2=['hello','world',123]
print(lst2)

'''第二种列表创建方式，使用内置函数list()'''
lst3=list(['hello','world',123,'world'])       #可以存储重复数据
print(lst3)
print(lst3[0])  #通过索引可以确定唯一的数据


'''列表生成式'''
lst=[i for i in range(1,10)]        #第一个i表示列表元素的表达式
print(lst)

'''列表中的元素的值为2，4，6，8，10'''
lst2=[i*2 for i in range(1,6)]
print(lst2)