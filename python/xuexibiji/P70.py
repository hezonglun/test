'''集合'''

'''集合的创建方式'''
#1.直接{}
s={'python','world',23,45,23}       #集合中的元素不允许重复
print(s)

#2.使用内置函数set()
s1=set(range(6))                 #range(6)会产生0-5的整数序列，通过set()转成集合
print(s1,type(s1))

s2=set([1,2,3,4,5,5,4])     #将列表通过set()转成集合
print(s2,type(s2))
s3=set((1,2,3,4,5,5,4))     #将元组通过set()转成集合     集合中的元素是无序的
s4=set('python')            #将字符串通过set()转成集合
s5=set({1,2,3,4,5,5,4})     #集合类型
s6=set(())

#3.定义一个空集合
s7=set()
print(s7)
#s8={}   不能直接使用花括号，不然定义的是字典

##4.集合生成式
print('--------------------------------------')
f={i*i for i in range(1,10)}
print(f)
print('--------------------------------------')


'''集合的相关操作'''
#1.集合元素的判断操作    in;not in
k1={10,20,30,40,50}
print(10 in k1)
print(10 not in k1)

#2.集合元素的新增操作
k1.add(900)     #调用add()方法
print(k1)
k1.update({70,45})      #调用update()
print(k1)

#3.集合元素的删除操作
k1.remove(70)       #调用remove()方法，一次删除一个指定元素,指定元素不存在会报错
print(k1)
k1.discard(40)      #调用remove()方法，一次删除一个指定元素，指定元素不存在不会报错
print(k1)
k1.pop()           #调用pop()方法，一次只删除一个任意元素
print(k1)
k1.clear()
print(k1)           #clear()清空集合


'''集合间的相关关系'''
#1.判断两个集合是否相等
p1={10,20,30,40,50}
p2={50,40,30,20,10}
print(p1==p2)   #True
print(p1!=p2)   #False

#2.判断一个集合是否是另一个集合的子集    调用issubset()
q1={10,20,30,40,50}
q2={10,20,30}
q3={10,20,80}
print(q2.issubset(q1))      #q2是否是q1的子集 True
print(q3.issubset(q1))      #q3是否是q1的子集 False

#如果B是A的子集那么A就是B的超集
#3.判断一个集合是否是另一个集合的子集    调用issuperset()
print(q2.issuperset(q1))    #q2是否是q1的超集 False
print(q1.issuperset(q2))    #q1是否是q2的超集 True

#4.判断两个集合是否“没有交集”     调用isdisjoint()
t1={10,20,30,40,50}
t2={40,50,60,70,80}
t3={12,23,34,45,56}
print(t1.isdisjoint(t2))    #False  有交集
print(t1.isdisjoint(t3))    #True   没有交集



'''集合的数学操作'''
#1.交集    intersection()和&是等价的
u1={10,20,30,40,50}
u2={30,40,50,60,90}
print(u1.intersection(u2))      #打印输出的交集是{40, 50, 30}
print(u1 & u2)                  #也可以使用&,打印输出的交集是{40, 50, 30}

#2.并集    union()和|是等价的
print(u1.union(u2))     #打印输出的并集是{40, 10, 50, 20, 90, 60, 30}
print(u1 | u2)          #也可以使用|,打印输出的并集是{40, 10, 50, 20, 90, 60, 30}

#3.差集   集合之间做差去掉另一个集合的全部部分  difference()和-是等价的
print(u1.difference(u2))    #打印输出的差集是{10, 20}
print(u1-u2)                #也可以使用-,打印输出的差集是{10, 20}

#4.对称差集   去掉中间部分后剩余的元素    symmetric_difference()和^是等价的
print(u1.symmetric_difference(u2))       #打印输出的对称差集是{10, 20, 90, 60}
print(u1^u2)                             #也可以使用^,打印输出的对称差集是{10, 20, 90, 60}


