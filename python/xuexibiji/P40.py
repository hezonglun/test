#流程控制语句
'''
#break
#从键盘录入密码，最多录入3次，如果正确就结束循环
#for in 方法
for item in range(3):
    pwd=input('请输入密码:')
    if pwd=='8888':
        print('密码正确')
        break
    else:
        print('密码不正确')

#while 方法
i=1
while i<=3:
    pwd=input('请输入密码:')
    if pw确')
        breakd=='8888':
        print('密码正
    else:
        print('密码不正确')
    i+=1




#continue
#要求输出1-50之间所有5的倍数
#正常方法
for item in range(1,51):
    if item%5==0:
        print(item)


print('------------使用continue-------------------')
for item in range(1,51):
    if item%5!=0:
        continue
    else:
        print(item)

'''

print('---------二重循环中的break;continue------------')
for i in range(5):
    for j in range(1,12):
        if j%2==0:
            #break
            continue
        print(j,end='\t')
    print()
