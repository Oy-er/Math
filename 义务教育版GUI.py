#代码由AI根据无GUI版生成
import tkinter as tk
from tkinter import messagebox

# 定义一个函数用于处理答案并更新分数
def check_answer():
    global fs
    question = question_label.cget('text')
    answer = answer_entry.get().strip()

    if question == "一年级\n37-12=" and answer == "25":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "二年级\n25*4=" and answer == "100":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "三年级\n288/9/2=" and answer == "16":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "四年级\n125*25*32=" and answer == "100000":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "五年级\n1/2+1/4+1/4=" and answer == "1":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "六年级+高数\n1/2+1/4+1/4+1/8+1/16+1/32+1/64+1/128+1/256...=" and answer == "1":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "七年级\n(-5)+7-(-3)*2=" and answer == "8":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "八年级\n27的立方根是" and answer == "3":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "九年级\n(-4)/(-5)*(-0.2)=" and answer == "-0.16":
        fs += 1
        messagebox.showinfo("结果", "对")
    else:
        messagebox.showinfo("结果", "错")

    # 清空输入框
    answer_entry.delete(0, tk.END)

    # 显示下一个问题
    if question == "一年级\n37-12=":
        question_label.config(text="二年级\n25*4=")
    elif question == "二年级\n25*4=":
        question_label.config(text="三年级\n288/9/2=")
    elif question == "三年级\n288/9/2=":
        question_label.config(text="四年级\n125*25*32=")
    elif question == "四年级\n125*25*32=":
        question_label.config(text="五年级\n1/2+1/4+1/4=")
    elif question == "五年级\n1/2+1/4+1/4=":
        question_label.config(text="六年级+高数\n1/2+1/4+1/4+1/8+1/16+1/32+1/64+1/128+1/256...=")
    elif question == "六年级+高数\n1/2+1/4+1/4+1/8+1/16+1/32+1/64+1/128+1/256...=":
        question_label.config(text="七年级\n(-5)+7-(-3)*2=")
    elif question == "七年级\n(-5)+7-(-3)*2=":
        question_label.config(text="八年级\n27的立方根是")
    elif question == "八年级\n27的立方根是":
        question_label.config(text="九年级\n(-4)/(-5)*(-0.2)=")
    elif question == "九年级\n(-4)/(-5)*(-0.2)=":
        show_final_result()

def show_final_result():
    total_correct = fs
    total_wrong = 9 - total_correct
    messagebox.showinfo("测试结束", f"总分：{total_correct}分\n你做对了{total_correct}题\n你做错了{total_wrong}题")
    if total_correct == 9:
        messagebox.showinfo("结果", "恭喜你通过了测试！")
    elif total_correct >= 5:
        messagebox.showinfo("结果", f"你及格了，但还可以再做对{9-total_correct}题！")
    else:
        messagebox.showinfo("结果", "你没有及格，再学学一段时间吧！")
    messagebox.showinfo("提示", "加好友，获取更多题目 微信号：zzz29130109")

# 初始化全局变量
fs = 0

# 创建主窗口
root = tk.Tk()
root.title("数学计算测试")
root.geometry("400x300")

# 欢迎信息
welcome_label = tk.Label(root, text="欢迎来到\n数学计算测试！(一到九年级)", font=("Arial", 14))
welcome_label.pack(pady=10)

# 问题标签
question_label = tk.Label(root, text="一年级\n37-12=", font=("Arial", 12))
question_label.pack(pady=10)

# 用户答案输入框
answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=10)

# 提交按钮
submit_button = tk.Button(root, text="提交", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=10)

# 运行主循环
root.mainloop()




















































































































































































































































































































































































































































































































































































#没错，我就是乱搞的