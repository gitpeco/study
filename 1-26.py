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
# 变量命名不已数字开头以及不能是关键字
# 运算符
# 赋值运算符 运算运算符
# ctrl+D复制多行
print("a+b=", a + b)
# **是次方 -\是除  --\\是整除  --%是取余
# c += a     ---  c = c+a

# 字符串定义和转义字符
# 用不同的引号   或者前面加个\将单双引号转意义变成普通符号
str10 = """
   床前明月光
疑是地上霜
"""
print(str10)

# 字符串拼接
name = "peco"
site = "编程日志"
tel = 114514
print("ID=" + name + "的", site)  # +直接链接,会有空格
# input
# name = input("输入名字老弟：")
# name = int(name)#int是字符转换转换为int，float（）转化为浮点型
print(name, type(name))
# 字符串格式化%对各种格式进行格式化
name = "peco"
print("我的名字是 %s" % name)
print("我是%s, 就是%s" % (name, tel))  # s是字符串，d是整型，f是浮点型
# mn是数字精度%.2f就只出现小数点后两位 (有四舍五入)—————— 精度在.的前面如果大于数的所有位就前面加空格小于就不生效%m.n
# 看起来整齐属于格式化的作用
# 有快速格式化更方便——没精度也不管类型
print(f"我的名字{name},我今年{tel},创立{site}")
# 流程控制if判断
b1 = True
b2 = False
print(f"b1={b1},b2={b2},类型是{type(b1)}和{type(b2)}")
# 比较运算符
n1 = 10
n2 = 20
print({f"n1==n2的结果是：{n1 == n2}"})
print({f"n1!=n2的结果是：{n1 != n2}"})
print({f"n1>=n2的结果是：{n1 >= n2}"})
# if语句
# age = input("输入你的年龄")
# age = int(age)
# if age >= 18:
#     print(f"我今年{age}岁")
# print("关你啥事")
# if else
# if age == 18:
#     print("我今年十八岁")
# else:
#     print("未成年退款")
# score = input("输入成绩：")
# print(f"我的语文成绩是:{score}")
# score = float(score)
# if score >= 90:
#     print("成绩优秀")
# elif score >= 80:
#     print("成绩一般")
# elif score >= 60:
#     print("及格")
# else:
#     print("再接再厉")
# if嵌套应用
# vip = False
# amount = input("输入充值金额：")
# amount = float(amount)
# if amount >= 100:
#     vip = True
#     if vip:
#         amount += 0.2 * amount
#     else:
#         amount += 0.1 * amount
# else:
#     vip = False
#     if vip:
#         amount += 0.2 * amount
#     else:
#         amount += 0.1 * amount
# print(f"你的余额是：%.0f" % amount)
# add = input("输入充值金额：")
# add = float(add)
#
# if amount+add >= 100:
#     vip = True
#     if vip:
#         add += 0.2 * add
#     else:
#         add += 0.1 * add
# else:
#     vip = False
#     if vip:
#         add += 0.2 * add
#     else:
#         add += 0.1 * add
# amount += add
# print(f"你的余额是：%.0f" % amount)
# 设计一个充值系统和上面逻辑一样，但是能循环充值
# 随机数生成random
# 生成1——10的随机数
import random
import sys
num = random.randint(1, 10)
print(num)
num2 = random.randint(1, 100)
print(num2)
for a in range(0, 3):#刚刚这里换成了num所以num一直在变化导致运行出错，字符要有对应意义好识别也不容易出错
    g = input("猜数字：输入一个数")
    g = int(g)
    if g > num:
        print("大了")
    elif g < num:
        print("小了")
    elif g == num:
        print("good")
        sys.exit()
# g = input("猜数字：输入一个数")
# g = int(g)
# if g > num:
#     print("大了")
# elif g < num:
#     print("小了")
# else:
#     print("good")
#     sys.exit()
#
# g = input("猜数字：输入一个数")
# g = int(g)
# if g > num:
#     print("大了")
# elif g < num:
#     print("小了")
# else:
#     print("good")
#     sys.exit()

