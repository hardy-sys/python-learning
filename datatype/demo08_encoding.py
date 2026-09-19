str1 = "中"
print(str1.encode("utf-8"))
print(str1.encode("gbk"))
print("==============================")
print(str1.encode("utf-8").decode("utf-8"))
print(str1.encode("gbk").decode("gbk"))


