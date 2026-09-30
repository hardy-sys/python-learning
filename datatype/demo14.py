
data1 = 10
data1+=10
print(data1)

data2 = 10
data2//=3
print(data2)

print("===================")
data3 = 10
print(data3)
# print(data3 = 10)
print(data3:=10)

data1 = 10
data2 = 20
data3 = 10
print(data1 == data2)
print(data1 != data2)
print(data1 > data2)
print(data1 < data2)
print(data1 >= data3)
print(data1 <= data3)

data1 = 10
data2 = 20
data3 = 10
result01 = (data1>data2) and (data1==data3)
print(result01)

result02 = (data1>data2) or (data1==data3)
print(result02)

result03 = not(data1>data2)
print(result03)

data1 = [1,2,3,4,5]
print(1 in data1)
print(6 not in data1)

data1 = [1,2,3,4,5]
data2 = [1,2,3,4,5]
print(data1 is data2)
print(data1 is not data2)

score = 60
result = "及格" if score >= 60 else "不及格"
print(result)