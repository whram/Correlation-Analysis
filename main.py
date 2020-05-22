from numpy import*
import numpy
import kMeans
import fpGrowth
import grade


dataSN = []
dataVS = []
dataFT = []
dataBW = []
dataPG = []
dataIF = []
dataNS = []
dataMA = []
dataSSL = []
dataO = []
dataNO = []

dataIn = open('dataIn\Netbehavior')
for line in dataIn.readlines():
	lineArr = line.strip().split(',')
	dataSN.append([int(lineArr[1]),0])
	dataVS.append([int(lineArr[2]),0])
	dataFT.append([int(lineArr[3]),0])
	dataBW.append([int(lineArr[4]),0])
	dataPG.append([int(lineArr[5]),0])
	dataIF.append([int(lineArr[6]),0])
	dataNS.append([int(lineArr[7]),0])
	dataMA.append([int(lineArr[8]),0])
	dataSSL.append([int(lineArr[9]),0])
	dataO.append([int(lineArr[10]),0])
	dataNO.append(lineArr)

dataSN = kMeans.km(dataSN,3,"social_network")
dataVS = kMeans.km(dataVS,3,"video_strem")
dataFT = kMeans.km(dataFT,3,"fil_transfer")
dataBW = kMeans.km(dataBW,3,"browse_web")
dataPG = kMeans.km(dataPG,3,"play_game")
dataIF = kMeans.km(dataIF,3,"internet_financial")
dataNS = kMeans.km(dataNS,3,"network_shopping")
dataMA = kMeans.km(dataMA,3,"mobile_app")
dataSSL = kMeans.km(dataSSL,3,"ssl_data")
dataO = kMeans.km(dataO,3,"other")


for i in range(0,len(dataNO)):
	dataNO[i][1] = 'SN_'+dataSN[i][1]
	dataNO[i][2] = 'VS_'+dataVS[i][1]
	dataNO[i][3] = 'FT_'+dataFT[i][1]
	dataNO[i][4] = 'BW_'+dataBW[i][1]
	dataNO[i][5] = 'PG_'+dataPG[i][1]
	dataNO[i][6] = 'IF_'+dataIF[i][1]
	dataNO[i][7] = 'NS_'+dataNS[i][1]
	dataNO[i][8] = 'NA_'+dataMA[i][1]
	dataNO[i][9] = 'SSL_'+dataSSL[i][1]
	dataNO[i][10] = 'O_'+dataO[i][1]
numpy.savetxt('dataOut\dataNO.txt', dataNO, fmt = '%s',delimiter=',')

dataGrade = open('dataIn\grade.txt')
dataG = grade.grade(dataGrade)
numpy.savetxt('dataOut\dataG.txt', dataG, fmt = '%s')

A = []
B = []
C = []

for i in range(0,len(dataG)):
	for j in range(0,len(dataNO)):
		if dataG[i][1] == 'C':
			if dataG[i][0] == dataNO[j][0]:
				C.append([dataNO[j][1],dataNO[j][2],dataNO[j][3],dataNO[j][4],dataNO[j][5],dataNO[j][6],dataNO[j][7],dataNO[j][8],dataNO[j][9],dataNO[j][10],])
		if dataG[i][1] == 'B':
			if dataG[i][0] == dataNO[j][0]:
				B.append([dataNO[j][1],dataNO[j][2],dataNO[j][3],dataNO[j][4],dataNO[j][5],dataNO[j][6],dataNO[j][7],dataNO[j][8],dataNO[j][9],dataNO[j][10],])
		if dataG[i][1] == 'A':
			if dataG[i][0] == dataNO[j][0]:
				A.append([dataNO[j][1],dataNO[j][2],dataNO[j][3],dataNO[j][4],dataNO[j][5],dataNO[j][6],dataNO[j][7],dataNO[j][8],dataNO[j][9],dataNO[j][10],])

numpy.savetxt('dataOut\A.txt', A, fmt = '%s')
numpy.savetxt('dataOut\B.txt', B, fmt = '%s')
numpy.savetxt('dataOut\C.txt', C, fmt = '%s')


fpconfidenceA,Afptree = fpGrowth.fp(A,5,"A")
numpy.savetxt('result\A.txt', fpconfidenceA, fmt = '%s',delimiter='	')
Afptree.disp()

fpconfidenceB,Bfptree = fpGrowth.fp(B,3,"B")
numpy.savetxt('result\B.txt', fpconfidenceB, fmt = '%s',delimiter='	')
Bfptree.disp()

fpconfidenceC,Cfptree = fpGrowth.fp(C,6,"C")
numpy.savetxt('result\C.txt', fpconfidenceC, fmt = '%s',delimiter='	')
Cfptree.disp()