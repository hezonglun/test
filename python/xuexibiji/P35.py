#range()的三种创建方式
'''用于生成一个整数序列；返回值是一个迭代器对象'''
r=range(10)
print(r)
print(list(r))      #将range产生的值一一列出来    list是列表的意思

a=range(1,12,2)     #(起始（默认为0），结束，步长（默认为1））


'''判断指定的整数在序列中是否存在 in   not in'''
print(10 in a)          #不存在
print(9 in r)

print(10 not in a)      #不存在
print(9 not in r)

#range对象所占用的内存空间都是相同的只有(起始（默认为0），结束，步长（默认为1））
