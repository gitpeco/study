# #while循环语句
# n = 1
# while n !=2:
#     n = int(input())
#     print(n)
i=1
sum=0
while i<=5:
    print(" ")
    j = 1
    while j<=5:
        print("%2.0f"%sum,end=" ")
        sum +=1
        j+=1
    i+=1


i=1
sum=0
while i<=9:
    print(" ")
    j = 1
    while j<=i:
        sum =i*j
        print("%2.0f * %2.0f=%2.0f" % (j, i, sum), end="\t")
        j+=1
    i+=1
#for循环
print()
total=0
website = "www.porcmagic\"\"''.com"
for w in website:
    print(w)
    if w=='\'':#字符的等于要用引号包住
        total+=1
print(total)


#for循环的嵌套
for i in range(1,10):#range(start,stop,步长),不包括后面的数包前面的
    for j in range(1,10):
        print("第%s行，第%s列"% (i,j),end=" ")
    print()


