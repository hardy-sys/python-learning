name = "专职播客"
setup_year = 2006
stock_price = 19.99
message = "%s,成立于：%d,我今天的股价是:%f"%(name,setup_year,stock_price)
print(message)

num1 = 11
num2 = 11.345
print("数字11宽度限制5，结果是:%5d"%num1)
print("数字11宽度限制1，结果是:%1d"%num1)
print("数字11.345宽度限制7，小数精度2,结果是:%7.2f"%num2)
print("数字11.345不限制，小数精度2,结果是:%2f"%num2)
