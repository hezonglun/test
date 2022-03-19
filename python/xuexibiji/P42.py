#else的使用
'''if--else;     for in--else;       while--else'''

#for in--else
for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
else:
    print('三次密码均输入错误')


#while--else
i=1
while i<=3:
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')
    i+=1
else:
    print('三次密码均输入错误')