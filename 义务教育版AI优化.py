#AI优化
import time

def show_message(message, delay=1.5):
    """显示消息并暂停"""
    print(message)
    time.sleep(delay)

def ask_question(grade, question, correct_answer, score):
    """统一的题目问答逻辑"""
    show_message(f"{grade}年级")
    answer = input(question)
    try:
        if isinstance(correct_answer, int) or isinstance(correct_answer, float):
            answer = float(answer)
        if answer == correct_answer:
            print("对")
            score += 1
        else:
            print("错")
    except ValueError:
        print("错")
    time.sleep(1)
    return score

def show_result(score, total, level):
    """显示测试结果"""
    show_message("测试结束")
    time.sleep(1)
    print(f"总分：{total}")
    print(f"分数：{score}")
    if score == total:
        print("恭喜你通过了测试！")
    elif score >= total / 2:
        print(f"你及格了，但还有 {total - score} 分可以提高！")
    else:
        print("你没有及格，再学学一段时间吧！")
    print("测试结束，祝你学习愉快！")
    time.sleep(1)

def main():
    """主程序"""
    score_primary = 0
    score_middle = 0

    # 欢迎信息
    show_message('''欢迎来到
数学计算测试！(一到九年级)''', delay=2)

    # 小学部分
    show_message("开始小学测试")
    primary_questions = [
        ("一", "37-12=", 25),
        ("二", "25*4=", 100),
        ("三", "288/9/2=", 16),
        ("四", "125*25*32=", 100000),
        ("五", "1/2+1/4+1/4=", 1),
        ("六", "1/2+1/4+1/4+1/8+1/16+1/32+1/64+1/128...=", 1)
    ]
    for grade, question, answer in primary_questions:
        score_primary = ask_question(grade, question, answer, score_primary)

    show_result(score_primary, len(primary_questions), "小学")

    # 初中部分
    show_message("开始初中测试")
    middle_questions = [
        ("七", "(-5)+7-(-3)*2=", 8),
        ("八", "27的立方根是", 3),
        ("九", "(-4)/(-5)*(-0.2)=", -0.16)
    ]
    for grade, question, answer in middle_questions:
        score_middle = ask_question(grade, question, answer, score_middle)

    show_result(score_middle, len(middle_questions), "初中")

    # 隐藏题目
    show_message("隐藏题目")
    score_primary = ask_question("？", "1111111111*1111111111=", 1234567900987654321, score_primary)

    # 总结
    total_score = score_primary + score_middle
    total_questions = len(primary_questions) + len(middle_questions) + 1
    print("恭喜做完题目！")
    print(f"一共 {total_questions} 题")
    print(f"你做对了 {total_score} 题")
    print(f"你做错了 {total_questions - total_score} 题")
    if total_score != total_questions:
        print(f"你还可以再做对 {total_questions - total_score} 题")
    print("加油哦！")
    time.sleep(5)

    # 额外隐藏题目
    show_message("真正的隐藏题目")
    answer = input("-1的平方根是")
    if answer.lower() == "i":
        print("啊对对对！")
    else:
        print("啊就不对！")

    # 广告信息
    for _ in range(5):
        print("加好友，获取更多题目 微信号：zzz29130109")
        time.sleep(0.05)

    print("The+End")
    time.sleep(5)

if __name__ == "__main__":
    main()