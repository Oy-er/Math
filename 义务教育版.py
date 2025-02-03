8
3
fs=0
print('''欢迎来到
数学计算测试！(一到九年级)''')

import time
time.sleep(1)
print("开始小学测试")
time.sleep(1)

print("一年级")
x = (input("37-12="))
x = int(x)
if x==25:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("二年级")
x = (input("25*4="))
x = int(x)
if x==100:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("三年级")
x = (input("288/9/2="))
x = int(x)
if x==16:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("四年级")
x = (input("125*25*32="))
x = int(x)
if x==100000:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("五年级")
x = (input("1/2+1/4+1/4="))
x = int(x)
if x==1:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("六年级+高等数学")
x = (input("1/2+1/4+1/4+1/8+1/16+1/32+1/64+1/128+1/256...="))
x = int(x)
if x==1:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

print("测试结束")
time.sleep(1)
print("总分：6")
time.sleep(1)
print("分数："+str(fs))
time.sleep(1)
if fs==6:
    print("恭喜你通过了测试！")
elif fs>=3:
    print("你及格了，但还有"+str(6-fs)+"分可以提高！")
else:
    print("你没有及格，再学学一段时间吧！")
print("测试结束，祝你学习愉快！")

time.sleep(1)
print('加好友，获取更多题目 微信号：zzz29130109')
time.sleep(3)

czfx = 0
print("开始初中测试")
time.sleep(1)

print("七年级")
x = (input("(-5)+7-(-3)*2="))
x = int(x)
if x==8:
    print("对")
    czfx+=1
else:
    print("错")
time.sleep(1)

print("八年级")
x = (input("27的立方根是"))
x=int(x)
if x==3:
    print("对")
    czfx+=1
else:
    print("错")
time.sleep(1)

print("九年级")
x = (input("(-4)/(-5)*(-0.2)="))
if x=="-0.16":
    print("对")
    czfx+=1
else:
    print("错")
time.sleep(1)

print("测试结束")
time.sleep(1)
print("总分：3")
time.sleep(1)
print("分数："+str(czfx))
time.sleep(1)
if czfx==3:
    print("恭喜你通过了测试！")
elif czfx>=1:
    print("你及格了，但还有"+str(3-czfx)+"分可以提高！")
else:
    print("你没有及格，再学学一段时间吧！")
print("测试结束，祝你学习愉快！")
time.sleep(1)

print('加好友，获取更多题目 微信号：zzz29130109')
time.sleep(15)

print("隐藏题目")
x = (input("1111111111*1111111111="))
x = int(x)
if x==1234567900987654321:
    print("对")
    fs+=1
else:
    print("错")
time.sleep(1)

for i in range(2):
    print("恭喜做完做完题目！")
    time.sleep(1)
    print("一共10题")
    
    time.sleep(1)
    print("你做对了"+str(fs+czfx)+"题")
    time.sleep(1)
    print("你做错了"+str(10-fs-czfx)+"题")
    time.sleep(1)
    if fs+czfx!=10:
        print("你还可以再做对"+str(10-fs-czfx)+"题")
        time.sleep(2)
print("加油哦！")
time.sleep(5)
for i in range(250):
    print("加好友，获取更多题目 微信号：zzz29130109")
    time.sleep(0.05)
time.sleep(30)

print("真正的隐藏题目")
x = (input("-1的平方根是"))
if x=="i":
    print("啊对对对！")
    time.sleep(1)
else:
    print("啊就不对！")     
    time.sleep(1)

for i in range(2500):
    print('''加好友，获取更多题目
    微信号：zzz29130109
    邮箱：q3324991557@outlook.com
    QQ：3324991558''')

print("The+End")
time.sleep(10)
