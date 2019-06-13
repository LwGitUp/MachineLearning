
"""
###线性分割

"""

from numpy import *
import matplotlib.pyplot as plt

def loadDataSet(fileName):
	dataMat = [];
	labelMat = []
	fr = open(fileName)
	for line in fr.readlines():
		lineArr = line.strip().split()
		dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
		labelMat.append(int(lineArr[2]))
	return dataMat, labelMat


# 数据标准化(归一化):统计均值和标准差归一化
def normalize(dataMat):
	# 计算均值
	height = mean(dataMat[:, 1])
	weight = mean(dataMat[:, 2])
	# 计算均方差
	stdh = std(dataMat[:, 1])
	stdw = std(dataMat[:, 2])
	# 标准化
	dataMat[:, 1] = (dataMat[:, 1] - height) / stdh
	dataMat[:, 2] = (dataMat[:, 2] - weight) / stdw
	return dataMat


# 显示绘制图形
def displayplot():
	plt.show()


# 绘制二维数据集坐标散点图:无分类
# 适用于 List 和 Matrix
def drawScatter(dataMat, flag=True):
	if type(dataMat) is list:
		px = (mat(dataMat)[:, 1]).tolist()
		py = (mat(dataMat)[:, 2]).tolist()
	if type(dataMat) is matrix:
		px = (dataMat[:, 1]).tolist()
		py = (dataMat[:, 2]).tolist()
	plt.scatter(px, py, c='blue', marker='o')
	if flag: displayplot();


# 绘制二维数据集坐标散点图:有分类
# 适用于 List 和 Matrix
def drawClassScatter(dataMat, classLabels, flag=True):
	# 绘制list
	if type(dataMat) is list:
		i = 0
		for mydata in dataMat:
			if classLabels[i] == 0:
				plt.scatter(mydata[1], mydata[2], c='blue', marker='o')
			else:
				plt.scatter(mydata[1], mydata[2], c='red', marker='s')
			i += 1;
	# 绘制Matrix
	if type(dataMat) is matrix:
		i = 0
		for mydata in dataMat:
			if classLabels[i] == 0:
				plt.scatter(mydata[0, 1], mydata[0, 2], c='blue', marker='o')
			else:
				plt.scatter(mydata[0, 1], mydata[0, 2], c='red', marker='s')
			i += 1;
	if flag: displayplot();


# 绘制分类线
def ClassifyLine(begin, end, weights, flag=True):
	# 确定初始值和终止值,精度
	X = linspace(begin, end, (end - begin) * 100)
	# 建立线性分类方差
	Y = -(float(weights[0]) + float(weights[1]) * X) / float(weights[2])
	plt.plot(X, Y, 'b')
	if flag: displayplot()


# 绘制趋势线: 可调整颜色
def TrendLine(X, Y, color='r', flag=True):
	plt.plot(X, Y, color)
	if flag: displayplot()


# 合并两个多维的Matrix，并返回合并后的Matrix
# 输入参数有先后顺序
def mergMatrix(matrix1, matrix2):
	[m1, n1] = shape(matrix1)
	[m2, n2] = shape(matrix2)
	if m1 != m2:
		print("different rows,can not merge matrix")
		return;
	mergMat = zeros((m1, n1 + n2))
	mergMat[:, 0:n1] = matrix1[:, 0:n1]
	mergMat[:, n1:(n1 + n2)] = matrix2[:, 0:n2]
	return mergMat


# 绘制等高线
def classfyContour(x, y, z, level=8, flag=True):
	plt.contour(x, x, z, 1, colors='black')
	if flag: displayplot()




# 数据集: 列1:截距 1;列2:x坐标; 列3:y坐标
dataMat,classLabels = loadDataSet("student.txt")
dataMat = mat(dataMat)
classMat= mat(classLabels)

# 数据归一化
dataMat = normalize(dataMat)

# 绘制数据集坐标散点图
drawClassScatter(dataMat,classLabels,False)
		
# m行数 n列数
m,n = shape(dataMat)
labelMat = classMat.transpose()
# 步长
alpha = 0.001
# 迭代次数
maxCycles = 500
#构成线性分割线 y=a*x+b: b:weights[0]; a:weights[1]/weights[2]
weights = ones((n,1))
# 计算回归系数 weights
for k in range(maxCycles):
	# 通过sigmoid函数返回结果，h是梯度计算的结果，是一个列向量
	# h = logRegres2.sigmoid(dataMatrix*weights)
	h = 1.0/(1+exp(-dataMat*weights))
	# 误差计算:分类标签(0,1)-h
	error = (labelMat - h)  
	# 回归系数：更新权重
	weights = weights + alpha * dataMat.transpose()* error 
print(weights)

# 绘制分类线图形
ClassifyLine(-3,3,weights)
