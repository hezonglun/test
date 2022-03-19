#输入函数input

#简单示例
dog=input('小狗想要什么礼物呢？\n')
print(dog,type(dog))

#输入两个数整数，计算两个整数的和
a=input('请输入一个数')   #或者a=(int(input('请输入一个数')))
b=input('请输入另一个数')
print(type(a),type(b))
print(int(a)+int(b))    #此次需进行类型转换