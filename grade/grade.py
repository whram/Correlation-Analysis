data = []
dataIn = open('grade.csv')
for line in dataIn.readlines():
        lineArr = line.strip().split(',')
        data.append([lineArr[0],float(lineArr[9])])

dataG = []

for l in range(0,len(data),6):
    a=data[l][1] + data[l + 1][1] * 2 + data[l + 2][1] * 2 + data[l + 3][1] * 4 + data[l + 4][1] * 2 + data[1 + 5][1] * 2
    dataG.append([data[l][0],a])

dataG = sorted(dataG, key=lambda x:x[1])
for i in range(0,len(dataG)):
    if i < 10 :
        dataG[i][1]='C'
    if 10 <= i < len(dataG) - 10 :
        dataG[i][1]='B'
    if i >= len(dataG) - 10:
        dataG[i][1]='A'

print dataG