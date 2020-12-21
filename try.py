trainInput = [[1,1],[9.4,6.4],[2.5,2.1],[8,7.7],[0.5,2.2],[7.9,8.4],[7,7],[2.8,0.8],[1.2,3],[7.8,6.1]]
trainOutput = [1, 1 ,1, -1, -1, -1, -1, 1, -1, 1]  #Desired Output
W = [-0.6, 0.75, 0.5] # initial weights

# for i in range(10):
# 	for j in range(2):
# 		if i == 0 and j == 0:
# 			print("x1\tx2\tDesired")
# 		print(trainInput[i][j], end = '\t')
# 	print(trainOutput[i], end = '\t')
# 	print()
W[0] = 0
W[1] = 1
W[2] = 2
print(W)