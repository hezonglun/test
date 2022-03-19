#条件表达式
'''从键盘输入两个整数，比较两个整数的大小'''
a=int(input('请输入第一个整数'))
b=int(input('请输入第二个整数'))
#比较大小
if a>b:
    print(a,'大于等于',b)
else:
    print(a,'小于',b)



print('使用条件表达式进行比较')
print(str(a)+'大于等于'+str(b)     if a>=b else    str(a)+'小于'+str(b))