#获取字典视图
he={'张三':100,'李四':90,'王五':45}
'''获取字典中所有的键：keys()'''
he2=he.keys()
print(type(he2))
print(list(he2))    #将所有的键组成的视图转换成列表

'''获取字典中所有的值：values()'''
he3=he.values()
print(type(he3))
print(list(he3))

'''获取字典中所有的键值对：items()'''
he4=he.items()
print(type(he4))
print(list(he4))    #转换后的列表元素是由元组组成的



#字典元素的遍历
for item in he:
    print(item,he[item],he.get(item))       #键遍历，键遍历，键遍历

