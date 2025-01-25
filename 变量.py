a = 12
print(a)
# 单行注释
# ctrl+AIt+L格式化
"""注释"""
'''注释'''
# 数据类型
a = 11
b = 3.14
c = "你好"

print("a=", a, type(a))
print("b=", b, type(b))
print("c=", c, type(c))
c = b
print("c=", c, type(c))
#变量命名不已数字开头以及不能是关键字
#运算符
#赋值运算符 运算运算符
#ctrl+D复制多行
print("a+b=", a+b)
#**是次方 -\是除  --\\是整除  --%是取余
#c += a     ---  c = c+a

#字符串定义和转义字符
#用不同的引号   或者前面加个\将单双引号转意义变成普通符号
str10="""
   床前明月光
疑是地上霜
"""
print(str10)

#字符串拼接
name = "peco"
site = "编程日志"
tel = 114514
print("ID="+name+"的",site)#+直接链接,会有空格
#input
#name = input("输入名字老弟：")
#name = int(name)#int是字符转换转换为int，float（）转化为浮点型
print(name,type(name))
#字符串格式化%对各种格式进行格式化
name = "peco"
print("我的名字是 %s" % name)
print("我是%s, 就是%s" % (name, tel))#s是字符串，d是整型，f是浮点型
#mn是数字精度%.2f就只出现小数点后两位 (有四舍五入)—————— 精度在.的前面如果大于数的所有位就前面加空格小于就不生效%m.n
#看起来整齐属于格式化的作用
#有快速格式化更方便——没精度也不管类型
print(f"我的名字{name},我今年{tel},创立{site}")