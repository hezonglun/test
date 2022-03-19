'''字符串的常用操作'''

'''字符串的查询操作'''  #index();rindex();find;rfind.
s='hello,hello'
print(s.index('lo'))    #第一次出现的位置，不存在会报错
print(s.rindex('lo'))   #最后一次出现的位置，不存在会报错
print(s.find('lo'))     #第一次出现的位置，不存在不会报错会返回-1
print(s.find('tr'))    #不存在不会报错会返回-1
print(s.rfind('lo'))    #最后一次出现的位置，不存在不会报错会返回-1
print(s.rfind('tr'))   #不存在不会报错会返回-1


'''字符串大小写转换的操作方法'''     #转换之后会产生一个新的字符串对象
s1='hello,python'
print(s1.upper())   #把字符串所有字符都转换成大写
print(s1.lower())   #把字符串所有字符都转换成小写     转换之后会产生一个新的字符串对象    字符串的驻留机制没有起作用
print(s1.swapcase())    #把字符串所有大写字符都转换成小写，所有小写字符都转换成大写
print(s1.capitalize())  #把第一个字符转换成大写，其他所有字符都转换成小写
print(s1.title())       #把每一个单词的第一个字符都转换成大写，单词剩余字符都转换成小写
a=s1.upper()
print(a,id(s1),id(a))       #说明了转换之后会产生一个新的字符串对象


'''字符串内容对齐的操作方法'''
s2='hello,python'
print(s2.center(20,'*'))    #居中对齐，第一个参数指定宽度，第二个参数指定填充符(可不填默认空格)，如果指定宽度小于字符串宽度将返回原字符
print(s2.ljust(20,'*'))     #左对齐，第一个参数指定宽度，第二个参数指定填充符(可不填默认空格)，如果指定宽度小于字符串宽度将返回原字符
print(s2.rjust(20,'*'))     #右对齐，第一个参数指定宽度，第二个参数指定填充符(可不填默认空格)，如果指定宽度小于字符串宽度将返回原字符
print(s2.zfill(20))         #右对齐，只接受一个参数用于指定宽度，左边用0填充如果指定宽度小于字符串宽度将返回原字符
s3='-1234'
print(s3.zfill(8))  #默认会将减号置于首位


'''字符串劈分操作的方法'''
s4='hello world python'
s5='hello|world|python'
print(s4.split())                       #从字符串左边开始劈分，默认的劈分字符为空格字符，返回值都是一个列表
print(s5.split(sep='|'))                #通过参数sep指定劈分字符串的劈分符
print(s5.split(sep='|',maxsplit=1))     #通过参数maxsplit指定劈分字符串的最大劈分次数，经过最大劈分次数后剩余的字符串会单独作为一部分
print(s4.rsplit())                      #从字符串右边开始劈分，默认的劈分字符为空格字符，返回值都是一个列表
print(s5.rsplit(sep='|'))               #通过参数sep指定劈分字符串的劈分符
print(s5.rsplit(sep='|',maxsplit=1))    #通过参数maxsplit指定劈分字符串的最大劈分次数，经过最大劈分次数后剩余的字符串会单独作为一部分


'''判断字符串的方法'''
print('判断指定字符串是不是合法字符串','asd_123'.isidentifier())
print('判断指定字符串是不是全部由空白字符组成(回车，换行，水平制表符)','\t'.isspace())
print('判断指定字符串是否全部由字母组成','asd'.isalpha())
print('判断指定字符串是否全部由十进制数字组成','1234567890'.isdecimal())
print('判断指定字符串是否全部由数字组成','12三四'.isnumeric())
print('判断指定字符串是否全部由字母和数字组成','123asdFGH三四'.isalnum())


'''字符串的替换与合并'''
#字符串的替换 replace()
s6='hello,python'
print(s6.replace('python','java'))      #第一个参数指定被替换的子符，第二个参数指定替换字符的字符串，该方法返回替换后的字符串 替换前的字符串不发生变化
s7='hello,python,python,python'
print(s7.replace('python','java',2))    #该方法可以通过第三个参数指定最大的替换次数

#字符串的合并 join()
lst2=['hello','world','python']
print(''.join(lst2))
print('|'.join(lst2))
#元组的合并
t=('hello','world','python')
print(''.join(t))
print('|'.join(t))
print('*'.join('python'))   #把python字符串作为字符串序列进行连接


'''字符串的比较操作'''
print('apple'>'app')
print('apple'>'banana')
print(ord('a'),ord('b'))    #字符串比较的是原始值，可调用ord()函数查看其原始值，chr()函数是其反向操作
print(ord('何'))
print(chr(20309))
#==与is的区别
#==比较的是值，is比较的是id


'''字符串的切片操作'''
r1='hello','python'
r2=r1[:5]
r3=r1[6:]
r4='!'
nowstr=r2+r4+r3


