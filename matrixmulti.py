import random
x1=input(" No. of rows in the first matrix: ")
y1=input(" No. of columns in the first matrix: ")
a = [[random.random() for col in range(y1)] for row in range(x1)]
for i in range(x1):
    for j in range(y1):
        a[i][j]=input()
x2=input ("No. of rows in the second matrix: ")
y2=input ("No. of columns in the second matrix: ")
b = [[random.random() for col in range(y2)] for row in range(x2)]
for i in range(x2):
    for j in range(y2):
        b[i][j]=input()
c=[[random.random()for col in range(y2)]for row in range(x1)]
if (y1==x2):
    for i in range(x1):
        for j in range(y2):
            c[i][j]=0
            for k in range(y1):
                c[i][j]+=a[i][k]*b[k][j]
            print c[i][j],'\t',
        print
else:
    print "not possible"

