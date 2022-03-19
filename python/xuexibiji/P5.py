#print输出函数的用法

#可以输出数字
print(200)

#可以输出字符串
print("helloworld")

#可以输出含有运算符的表达式
print(3+3)


#将数据输出到文件中，使用file=fp
fp=open('D:/text.txt','a+')#a+如果文件不存在就创建，存在就在文件内容的后面继续追加
print('helloworld',file=fp)
fp.close()

#不进行换行输出
print('hello''world''python')