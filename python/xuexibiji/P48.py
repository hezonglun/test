#获取指定列表元素的索引  index()
lst=['hello','world',12,'hello']
print(lst.index('hello'))   #如果列表中有相同的元素只返回列表中相同元素的第一个索引
#print(lst.index('python'))  ValueError: 'python' is not in list        不存在的情况

'''可以指定的start和stop之间进行查找'''
print(lst.index('hello',1,4))   #在1-3之间查找hello的索引


#获取列表中的指定元素
'''
正向索引0到N-1;  lst[0]
逆向索引-N到-1；  lst[-N]
'''
lst2=['hello','world',12,'hello',234]
print(lst2[3])      #正向索引
print(lst2[-3])     #逆向索引
#print(lst2[10])    IndexError: list index out of range


#获取列表中的多个元素-切片操作
#语法格式：列表名[start:stop:step]      start开始；stop结束；step步长   均可保持默认
#切出的是一个新的列表对象
'''
切片范围：(start:stop)
step默认为1：简写[start:stop]
step为正数:[stop:step] 切片第一个元素默认为列表的的第一个元素  从start开始往后计算切片
          [start::step] 切片最后一个元素默认为列表的最后一个元素    从start开始往后计算切片
step为负数:[:stop:step]    切片第一个元素默认为列表的的最后一个元素    从start开始往前计算切片
         :[start::step]     切片最后一个元素默认为列表的第一个元素     从start开始往前计算切片
'''
lst3=[11,22,33,44,55,66,77,88,99]
print(lst3[1:6:1])
list4=lst3[1:6:1]
#切出的是一个新的列表对象
print('原列表',id(3))
print('现列表',id(4))
print(lst3[1:6:])       #step默认为1：简写[start:stop]
print(lst3[1:6:2])      #步长为2

print(lst3[1::3])       #切片最后一个元素默认为列表的最后一个元素
print(lst3[:6:1])       #切片第一个元素默认为列表的的第一个元素

print('-------------step为负数-------------------')
print('原列表',lst3[::1])
print('现列表',lst3[::-1])     #步长为负数是列表逆序输出
print('现列表',lst3[::-2])     ##步长为-2


'''列表元素的判断及遍历'''
#判断指定元素在列表中是否存在
#元素 in 列表名         元素 ont in 列表名
lst=[12,23,34,45,56]
print(22 in lst)            #False
print(22 not in lst)        #True

#列表元素的遍历
#for 迭代对象 in 列表名
print('------------列表元素的遍历----------------')
for item in lst:
    print(item)