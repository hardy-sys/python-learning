import random
num = random.randint(1,10)
guess = int(input("猜1-10"))
if guess == num:
    print("猜对了")
else:
    print(f"猜错了，答案是{num}")
