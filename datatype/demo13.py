import math
v1 = [2,3]
v2 = [4,-1]

add = [v1[0]+v2[0], v1[1]+v2[1]]

dot = v1[0]*v2[0] + v1[1]*v2[1]

mag = math.sqrt(v1[0]**2 + v1[1]**2)
print("相加", add)
print("点积", dot)
print("v1模长", mag)

import math
a = [1,2,3]
b = [0,2,-1]

sub = [a[0]-b[0],a[1]-b[1],a[2]-b[2]]

mul = [x*3 for x in a]

dot2 = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
print("相减",sub)
print("数乘3倍",mul)
print("点积",dot2)

import math
v = [3,4]

m = math.sqrt(v[0]**2+v[1]**2)
unit = [v[0]/m, v[1]/m]
u = [-4,3]

is_v = math.isclose(v[0]*u[0]+v[1]*u[1],0)
print("单位向量",unit)
print("垂直？",is_v)


p = [2,5]
q = [-3,1]

plus = [p[0]+q[0],p[1]+q[1]]
minus = [p[0]-q[0],p[1]-q[1]]

d = p[0]*q[0] + p[1]*q[1]
print("p+q",plus)
print("p-q",minus)
print("点积",d)
