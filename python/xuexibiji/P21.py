#运算符


#算术运算符
print(1+1)
print(2-1)
print(2*3)
print(11/2)     #除法运算
print(11//2)    #整除运算，结果只取整数部分
print(11%2)     #取余运算符，结果为1
print(2**3)     #幂运算符，2的3次方




#赋值运算符
#运算顺序是从右往左
a=b=c=20    #链式赋值
print(a,id(a))
print(b,id(b))
print(c,id(c))

print('-------支持参数赋值--------')
a=20
a+=20   #a=a+20
print(a)    #其他以此类推

print('-------解包赋值---------')
a,b,c=20,30,40  #值需要一一对应
print(a,b,c)

print('--------交换两个变量的值-----------')
a,b=20,30
print('交换之前:',a,b)
a,b=b,a
print('交换之后:',a,b)




#比较运算符，运算结果是bool类型
a,b=20,30
print('a>b吗？',a>b)
print('a<=b吗？',a<=b)
print('a==b吗？',a==b)
print('a!=b吗？',a!=b)
"""==比较的是值，不是标识；标识(id)的比较用is和is not比较"""
#is
a,b=10,10
print(a==b)         #True   说明，a与b的value相等
print(a is b)      #True    说明，a与b的id标识相等
'''数组例子'''
lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)       #value-----true
print(lst1 is lst2)     #id--------false
print(id(lst1))
print(id(lst2))
#is not
print(a is not b)           #False  说明a与b的id是相等的
print(lst1 is not lst2)     #True   说明lst1与lst2的id是不相等的



#布尔运算符
a,b=1,2
print('------------and 并且----------------')
print(a==1 and b==2)    #True    True and True-->True
print(a==1 and b!=2)    #False   True and False-->False
print(a!=1 and b==2)    #False   False and True-->False
print(a!=1 and b!=2)    #False   False and False-->False

print('--------or 或者---------')
print(a==1 or b==2)    #True   True and True-->True
print(a==1 or b!=2)    #True   True and False-->True
print(a!=1 or b==2)    #True   False and True-->True
print(a!=1 or b!=2)    #False   False and False-->False

print('--------not 对bool类型操作数取反----------')
a=True
b=False
print(not a)    #False
print(not b)    #True

print('--------in 与 not in----------')  #in表示在什么什么里;not in表示不在什么什么里
s='helloworld'
print('w'in s)          #True
print('k'in s)          #False
print('w'not in s)      #False
print('k'not in s)      #False



#位运算符
"""或|；与&；左移运算符<<;右移运算符>>"""
print(4&8)      #按位 与&，同为1时结果为1
print(4|8)      #按位 或|，同为0时结果为0
print(4<<1)     #向左移动1位（移动一个位置）相当于乘2
print(4<<2)     #向左移动2位（移动二个位置）相当于乘4
print(4>>1)     #向右移动1位（移动一个位置）相当于除2
print(4>>2)     #向右移动2位（移动二个位置）相当于除4

#运算符的优先级
#()->算术运算符->位运算符->比较运算符->布尔运算发->赋值运算符