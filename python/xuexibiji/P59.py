'''字典'''

'''字典的创建'''
#1.使用花括号
he={'张三':100,'李四':90,'王五':45}
print(he)
print(type(he))         #<class 'dict'>

#2.使用内置函数dict()
he2=dict(name='jack',age=20)
print(he2)
print(type(he2))

#3.创建空字典
h={}
print(h)

print('---------------------------------------------------------------------')
#4.字典生成式
    #内置函数zip() 可将可迭代对象作为参数，将对象中对应的元素打包成一个元组，然后返回由这些元组组成的列表
    #字典生成式  {item.upper():price     for item,price in zip(items,prices)}
items=['abc','bcd','dea']
prices=[12,34,56,78,89]
d={item.upper():price     for item,price in zip(items,prices)}
print(d)
print('------------------------------------------------------------------')

'''字典元素的操作'''

#1.字典元素的获取
    #1.[]方法     举例:scores['张三']
    #2.get()方法  举例:scores.get('张三')
he={'张三':100,'李四':90,'王五':45}
print(he['张三'])      #1.[]方法
print(he.get('张三'))
#区别
#print(he['王二麻'])        #KeyError: '王二麻'   会报错
print(he.get('王二麻'))    #不会报错，会输出None
print(he.get('王麻',199))     #199是在查找键所对的值不存在时，提供的一个默认值



#2.字典元素的增删改操作
    #1.key判断指定的键在字典中是否存在 in；not in 返回布尔值
he={'张三':100,'李四':90,'王五':45}
print('张三'in he)        #True
print('张三'not in he)    #False

    #2.字典元素的删除     del 字典名['键名']
del he['张三']    #删除指定的键值对
print(he)
#he.clear()      #清空字典元素
print(he)

    #3.新增元素
he['陈六']=20     #{'李四': 90, '王五': 45, '陈六': 20}
print(he)

    #4.更改元素的值
he['陈六']=888    #{'李四': 90, '王五': 45, '陈六': 888}
print(he)
