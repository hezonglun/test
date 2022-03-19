#for in 循环

for item in 'python':       #第一次取出的是怕p，将p赋值给item，将item的值输出
    print(item)

#range() 产生一个整数序列，整数序列也是一个可迭代对象
for i in range(10):
    print(i)

#如果循环体中不需要使用到自定义变量，可以将自定义变量写为下划线
for _ in range(10):
    print('人生苦短')

print('---------使用for循环，计算1-100之间的偶数和-------------')
sum=0
for i in range(0,101,2):
    sum+=i
print(sum)


print('--------输出100-999之间的水仙花数---------')
#例：153=3**3+5**3+1**3 此叫水仙花数

for item in range(100,1000):
    ge=item%10          #个位
    shi=item//10%10     #十位
    bai=item//100       #百位
    #print(bai,shi,ge)  #打印输出所有100-999之间的个，十，百位的值
    if ge**3+shi**3+bai**3==item:
        print(item)
