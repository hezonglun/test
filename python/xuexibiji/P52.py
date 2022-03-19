#列表元素的增删改操作

'''列表元素的增加
append()    在列表末尾添加一个元素（常用）
extend()    在列表末尾至少添加一个元素
insert()    在列表的任意位置添加一个元素
切片         在列表的任意位置至少添加一个元素'''
print('------------append() 在列表末尾添加一个元素--------------')
lst=[11,22,33,44,55,66,77,88]
print('添加元素之前',lst,id(lst))
lst.append(99)
print('添加元素之后',lst,id(lst))     #添加元素之后并没有创建新的列表对象


print('------------extend() 在列表末尾至少添加一个元素--------------')
lst2=['holle','world']
lst.append(lst2)        #将lst2作为一个元素添加到了列表的末尾
print(lst)
lst.extend(lst2)        #向列表的末尾一次添加多个元素
print(lst)


print('------------insert() 在列表的任意位置添加一个元素--------------')
lst.insert(1,68)    #在索引为一的位置上添加一个68
print(lst)


print('------------切片 在列表的任意位置至少添加一个元素--------------')
lst3=[True,False,'holle']
lst[1:]=lst3
print(lst)





print('----------列表元素的删除--------------')
'''列表元素的删除
remove()    一次删除一个元素；重复元素只删除第一个；元素不存在抛出valueerror
pop()       删除一个指定索引位置上的元素；指定索引不存在抛出valueerror；不指定索引就删除列表中的最后一个元素
切片         一次至少删除一个元素;会产生一个新的列表对象
clear()     清空列表
del         删除列表'''


print('----------------remove()一次删除一个元素；重复元素只删除第一个；元素不存在抛出valueerror--------------------')
he=[10,20,30,40,50,60,30]
he.remove(30)       #一次删除一个元素；重复元素只删除第一个
print(he)
#he.remove(80)       #元素不存在抛出ValueError


print('--------------pop() 删除一个指定索引位置上的元素；指定索引不存在抛出valueerror；不指定索引就删除列表中的最后一个元素-----------------')
he.pop(1)       #移除索引为一的元素
print(he)
#he.pop(6)       #指定索引不存在抛出valueerror
he.pop()         #不指定索引就删除列表中的最后一个元素
print(he)


print('--------------切片    一次至少删除一个元素;会产生一个新的列表对象----------------')
he2=he[1:3]
print(he2)

he[1:3]=[]      #不产生新的列表对象，只是单纯的切片删除
print(he)


print('-----------------clear()  清空列表----------------')
he2.clear()
print(he2)


print('-----------del 删除列表对象-------------')
del he2
#print(he2)      #NameError: name 'he2' is not defined



print('-------------列表元素的修改---------------')

print('---------为指定索引的元素赋予一个新值----------')
he3=[10,20,30,40,50]
he3[2]=100      #一次修改一个值
print(he3)

print('----------为指定的切片赋予一个新值-----------')
he3[1:4]=808,909,999
print(he3)



print('-----------列表元素的排序操作---------------')
'''常见的两种方法
1.调用sort()方法，列表中的所有元素默认按照从大到小的顺序进行排列，可以指定reverse=True，进行降序排序
2.调用内置函数sorted()，可以指定reverse=True，进行降序排序，原列表不会发生改变'''
'''sort()方法是对原列表进行排序操作而内置函数sorted()是产生一个新的列表对象而原列表不发生任何改变'''

zhaoshoqiang=[22,3,40,55,6,77,30]
print('排序前的列表序列',zhaoshoqiang,id(zhaoshoqiang))
zhaoshoqiang.sort()     #调用sort()方法，列表中的所有元素默认按照从大到小的顺序进行排列
print('排序后的列表序列',zhaoshoqiang,id(zhaoshoqiang))

#通过指定关键字参数，将列表中的元素进行降序排序
zhaoshoqiang.sort(reverse=True)     #指定reverse=True，进行降序排序
print('指定reverse=True，进行降序排序后的列表序列',zhaoshoqiang)
zhaoshoqiang.sort(reverse=False)    #也可以指定reverse=False，进行升序排序
print('指定reverse=False，进行升序排序后的列表序列',zhaoshoqiang)

#调用内置函数sorted()进行排序     但是调用内置函数sorted()创建了新的列表
print('---------------调用内置函数sorted()进行排序----------------')
zhaoshoqiang=[22,3,40,55,6,77,30]
print('原列表',zhaoshoqiang)
now_zhaoshoqiang=sorted(zhaoshoqiang)
print('排序后的列表序列',now_zhaoshoqiang)

'''指定reverse=True，进行降序排序'''
now_zhaoshoqiang=sorted(zhaoshoqiang,reverse=True)
now2_zhaoshoqiang=sorted(zhaoshoqiang,reverse=False)     #也可以指定reverse=False，进行升序排序
print('内置函数sorted()，指定reverse=True后的列表',now_zhaoshoqiang)
print('内置函数sorted()，指定reverse=False后的列表',now2_zhaoshoqiang)