import math
C=50
H=30
Q = []														#Value to be displayed
items=[x for x in input().split(',')]						#Value of varible D in form of dictionary
for d in items:
    value.append(str(int(round(math.sqrt(2*C*float(d)/H)))))		#CALCULATED VALUE

print (','.join(value))