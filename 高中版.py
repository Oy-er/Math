fs=0
print('''欢迎来到
数学闯关
高中版''')
import time
time.sleep(1.5)

print("必修一")
x=(input("集合A={x|x^2-2x+1=0},则集合A="))
if x=="{1}":
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("必修二")
x=(input('在复平面内，复数z=1-2i对应的点的坐标为 A. （1，2） B. （2，1） C. （1，-2） D. （2，-1）    答案：'))
if x=="C" or x=="c":
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("恭喜你做完了所有题目")
print("总分：2分")
print("分数："+str(fs))
if fs==2:
    print("你通过了测试")
else:
    print("你未能通过测试")
time.sleep(2)  

print("the+end")
time.sleep(10)

print('隐藏题目')
time.sleep(1)
a=(input('没有隐藏题目'))
if a == "滚":
    a=(input('√-1'))
    if a == 'i':
        print('对')
    else:
        print('滚')
time.sleep(2)
for i in range(2500):
    print('''加好友，获取更多题目 微信号：zzz29130109
邮箱：q3324991557@outlook.com''')