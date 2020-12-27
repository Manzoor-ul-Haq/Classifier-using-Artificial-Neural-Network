import matplotlib.pyplot as plt
import numpy as np

class Perceptron():
	def __init__(self):
		self.x0 = 1
		self.W = [-0.6, 0.75, 0.5] # initial weights
		self.l_r = 0.02 # learning rate
		self.epochs = 30 #total iterations over the training data

		self.trainingInput = [[1,1],[9.4,6.4],[2.5,2.1],[8,7.7],[0.5,2.2],[7.9,8.4],[7,7],[2.8,0.8],[1.2,3],[7.8,6.1]]
		self.trainingOutput = [1, 1 ,1, -1, -1, -1, -1, 1, -1, 1]  #Desired Output
	def showData(self, trainInput, trainOutput):
		for i in range(10):
			for j in range(2):
				if i == 0 and j == 0:
					print("x1\tx2\tDesired")
				print(trainInput[i][j], end = '\t')
			print(trainOutput[i], end = '\t')
			print()

	def activationFunction(self, Output):
		if Output >= 0:
			return 1
		else:
			return -1

	def actualOutput(self, Weights, X):
		Output = (Weights[0] * self.x0) + (Weights[1] * X[0]) + (Weights[2] * X[1])
		return self.activationFunction(Output)

	def updateWeights(self, actual_Output, desired_Output, X, Weights, learningRate):
		updatedWeights = [0, 0, 0]
		updatedWeights[0] = Weights[0] + (learningRate * (desired_Output - actual_Output) * self.x0)
		updatedWeights[1] = Weights[1] + (learningRate * (desired_Output - actual_Output) * X[0])
		updatedWeights[2] = Weights[2] + (learningRate * (desired_Output - actual_Output) * X[1])
		return updatedWeights

	def desiredOutput(self, trainInput, trainOutput, X):
		for i in range(10):
			if trainInput[i] == X:
				index = i
				break
		return trainOutput[index]

	def learning(self, Weights, trainInput, trainOutput, learningRate):
		count = 0
		while True:
			previousWeights = Weights
			count += 1
			for X in trainInput:
				actual_Output = self.actualOutput(Weights, X)
				desired_Output = self.desiredOutput(trainInput, trainOutput, X)
				Weights = self.updateWeights(actual_Output, desired_Output, X, Weights, learningRate)
			if Weights == previousWeights:
				return Weights, count

	def graph(self, Weights, trainInput):
		x = np.linspace(0,10,100)
		y = -((Weights[1] * x) + (Weights[0] * 1)) / Weights[2]
		plt.scatter(*zip(*trainInput))
		plt.plot(x, y, '-r', label='Classifier')
		plt.title('Classifier')
		plt.xlabel('x', color='#1C2833')
		plt.ylabel('y', color='#1C2833')
		plt.legend(loc='upper left')
		plt.grid()
		plt.show()

	def main(self):
		self.showData(self.trainingInput, self.trainingOutput)
		Weights, self.epochs = self.learning(self.W, self.trainingInput, self.trainingOutput, self.l_r)
		print("Epochs: ", self.epochs)
		self.graph(Weights, self.trainingInput)

def main():
	Perceptron().main()

main()