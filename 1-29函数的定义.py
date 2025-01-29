"""
    函数的定义
"""
# def hello():
#     print('hello')
#     return 1
# if __name__ == '__main__':
#     hello()
#
# def say():
#     syssh="""
#     床前明月光
#     疑是地上霜
# 新年快乐"""
#     print(syssh)
# for x in range(0,3):
#     say()
"""
    函数的参数       
"""


# 定义加方法的函数
def add(x, y):
    result = x + y
    print(f"{x} + {y} = {result}")


add(1, 2)
add(3, 4)


def add(a, b, c):
    result = a + b + c
    return print(f"{a} + {b} + {c} = {result}")


for g in range(1, 11):
    add(1, 2, 3)
"""关键字参数
"""
add(a=9, c=11, b=6)
# 部分使用关键字
add(3, c=9, b=11)


# 参数默认值
def say_hello(name="你好", msg="欢迎"):
    print(f"{name} {msg}")


say_hello("别说话", "这里的人都睡着了")
say_hello(msg="拜拜")
"""
    函数的返回值    
"""


# 定义加法函数
def all(n, m):
    result = n + m
    return result


print(all(n=1, m=2))

"""
    None
"""


def text(i=1, y=1):
    result = i * y


def check_user(name,passwork):
    if name =="11" and passwork == "2":
        return True
    else:
        return None


dd = text()
print(f"{dd},类型是{type(dd)}")

user1 = check_user("11","22")
print(user1)
if user1:
    print("成功登录")
else:
    print("失败")

