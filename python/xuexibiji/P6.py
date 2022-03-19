#P6转义字符

print('hello\nworld')  #\ +转义字符de首字母  n-->newline的首字符表示换行

print('hello\tworld')  #\t表示一个制表位，一个制表位占4个字符位，满4开1
print('helloooo\tworld')

print('hello\rworld')  #world将hello进行了覆盖
print('hello\bworld')  #b是退一个格，将o给退没了

print('https:\\www.baidu.com')  #输入双斜杠最后只能输出一个斜杠，如需要两个斜杠可以输入4个斜杠
print('https:\\\\www.baidu.com')

print('老师说:\'大家好\'')  #加上反斜杠后引号不再是字符串的边界

#原字符，不希望字符串中的转义字符起作用，就使用转义字符，在字符串之前加上r，或R
print(r'hello\nworld')

#注意事项，最后一个字符不能是反斜杠，但是你是两个行
#print(r'hello\nworld\')
print(r'hello\nworld\\')