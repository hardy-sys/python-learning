import random

salary = 1000
money = 10000
for i in range(1,21):
    num = random.randint(1, 10)
    if num < 5:
        print(f"员工{i}，绩效分{num}，不发工资, 下一位")
    else:
        if money >= salary:
            #money = money - salary
            money -= salary
            print(f"向员工{i}，发放工资{salary}，账户余额还剩余{money}")

        else:
            print(f"结束发工资")
            break