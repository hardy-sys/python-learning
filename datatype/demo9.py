if int(input("175（cm）:")) <120:
    print("身高小于120cm，可以免费。")
elif int(input("输入你的VIP等级（1-5）:")) >3:
    print("VIP等级大于3，可以免费")
elif int(input("请告诉我今天几号：")) == 1:
    print("今天一号免费日，可以免费")
else:
    print("不好意思，条件不满足，需要购买10元")