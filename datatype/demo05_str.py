str1 = "i love money"
str2 = '涛哥和金莲的故事'
print(type(str1))
print(str1)
print(str2)

# 单引号和双引号可以嵌套
str3 = "涛哥和'金莲'的故事"
print(str3)

str4 = '涛哥和"金莲"的故事'
print(str4)

print("=========================")
str5 = """abc"""
print(str5)

print("=========================")
"""
   双引号表示字符串:字符串内容不能换行
   三双引号表示字符串:字符串内容可以换行 -> 如果表示一些具有特殊格式的字符串内容就用三双引
"""
# print("hello
#       world")

print("""
    hello
    world
""")
print("=========================")
str6 = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>首页</title>
</head>
<body>
   性感涛哥,在线发牌
</body>
</html>
"""
print(str6)