x0 = 1
Weights = [-0.6, 0.75, 0.5] # initial weights
learningRate = 0.02 # learning rate
epochs = 30 #total iterations over the training data

trainInput = [[1,1],[9.4,6.4],[2.5,2.1],[8,7.7],[0.5,2.2],[7.9,8.4],[7,7],[2.8,0.8],[1.2,3],[7.8,6.1]]
trainOutput = [1, 1 ,1, -1, -1, -1, -1, 1, -1, 1]  #Desired Output

def givenData():
	for i in range(10):
		for j in range(2):
			if i == 0 and j == 0:
				print("x1\tx2\tDesired")
			print(trainInput[i][j], end = '\t')
		print(trainOutput[i], end = '\t')
		print()

def activationFunction(Output):
	if Output >= 0:
		return 1
	else:
		return -1

def actualOutput(Weights, X):
	Output = (Weights[0] * x0) + (Weights[1] * X[0]) + (Weights[2] * X[1])
	return activationFunction(Output)

def updateWeights(actual_Output, desiredOutput, X, Weights):
	Weights[0] = Weights[0] + (l_r * (desiredOutput - actual_Output) * x0)
	Weights[1] = Weights[1] + (l_r * (desiredOutput - actual_Output) * X[0])
	Weights[2] = Weights[2] + (l_r * (desiredOutput - actual_Output) * X[1])
	return Weights