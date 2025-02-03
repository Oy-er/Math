import tkinter as tk
from tkinter import messagebox

# 定义一个函数用于处理答案并更新分数
def check_answer():
    global fs
    question = question_label.cget('text')
    answer = answer_entry.get().strip()

    if question == "必修一\n集合A={x|x^2-2x+1=0},则集合A=" and answer == "{1}":
        fs += 1
        messagebox.showinfo("结果", "对")
    elif question == "必修二\n在复平面内，复数z=1-2i对应的点的坐标为 A. （1，2） B. （2，1） C. （1，-2） D. （2，-1）    答案：" and (answer == "C" or answer == "c"):
        fs += 1
        messagebox.showinfo("结果", "对")
    else:
        messagebox.showinfo("结果", "错")

    # 清空输入框
    answer_entry.delete(0, tk.END)

    # 显示下一个问题
    if question == "必修一\n集合A={x|x^2-2x+1=0},则集合A=":
        question_label.config(text="必修二\n在复平面内，复数z=1-2i对应的点的坐标为 A. （1，2） B. （2，1） C. （1，-2） D. （2，-1）    答案：")
    elif question == "必修二\n在复平面内，复数z=1-2i对应的点的坐标为 A. （1，2） B. （2，1） C. （1，-2） D. （2，-1）    答案：":
        show_final_result()

def show_final_result():
    messagebox.showinfo("测试结束", f"总分：{fs}分\n你做对了{fs}题\n你做错了{2-fs}题")
    if fs >= 2:
        messagebox.showinfo("结果", "你通过了测试")
    else:
        messagebox.showinfo("结果", "你未能通过测试")
    messagebox.showinfo("提示", "加好友，获取更多题目 微信号：zzz29130109\n邮箱：q3324991557@outlook.com")

# 初始化全局变量
fs = 0

# 创建主窗口
root = tk.Tk()
root.title("数学闯关 高中版")
root.geometry("400x300")

# 欢迎信息
welcome_label = tk.Label(root, text="欢迎来到\n数学闯关\n高中版", font=("Arial", 14))
welcome_label.pack(pady=10)

# 问题标签
question_label = tk.Label(root, text="必修一\n集合A={x|x^2-2x+1=0},则集合A=", font=("Arial", 12))
question_label.pack(pady=10)

# 用户答案输入框
answer_entry = tk.Entry(root, font=("Arial", 12))
answer_entry.pack(pady=10)

# 提交按钮
submit_button = tk.Button(root, text="提交", command=check_answer, font=("Arial", 12))
submit_button.pack(pady=10)

# 运行主循环
root.mainloop()
