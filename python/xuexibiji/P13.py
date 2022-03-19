#python中常见的数据类型
#2浮点类型》float》3.1415

a=3.14159
print(a,type(a))

#浮点数存储不精确---计算时可能会出现小数位数不确定的情况 如：
print(2.2+1.1)
#解决方法---导入模块decimal
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))