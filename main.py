class Controller():
	def __init__(self):
		self. queue = []
		self.usedValues = []


	def transferUntilExpectedResult(self, canister1StartingLoad, canister2StartingLoad, canister1TargetLoad, canister2TargetLoad):
		#procefure A - start with canister1 --> canister 2
		canister1.info(), canister2.info()
		canister1.transfuseToCanister2(canister2)
		canister1.targetReached()
		canister2.targetReached()
		canister2.emtpyOut()
		canister1.transfuseToCanister2(canister2)
		canister1.showCanisterGraphic()
		canister2.showCanisterGraphic()

		
		return

class Canister():
	def __init__(self, name, maxLoad, startingLoad, targetLoad):
		self.name = name
		self.maxLoad = maxLoad
		self.startingLoad = startingLoad
		self.currentLoad = startingLoad
		self.targetLoad =	targetLoad

	def userInputInt(self, textForUser):
		#user input. If input is not digit, repeat
		#TODO better graphic window
		i = 0
		while i < 5:
			userInput = input(textForUser + ": ")
			if userInput.isdigit():
				return userInput
			else:
				print("Input is not valid")
				i += 1	

	def info(self):
		#print short info abouth Canister
		print("{}: Max load: {}, currentLoad = {}, startingLoad = {}".format(self.name, self.maxLoad, self.currentLoad, self.startingLoad))

	def fillToMax(self):
		#set currentLoad to maxLoad
		self.currentLoad = self.maxLoad

	def emtpyOut(self):
		#set currentLoad to 0
		self.currentLoad = 0

	def IsEmpty(self):
		#return true if canister is empty
		if self.currentLoad == 0:
			return True
		else:
			return False

	def isFull(self):
		if self.currentLoad == self.maxLoad:
			return True
		else:
			return False

	def checkWaterInRange(self):
		if self.currentLoad <= self.maxLoad and self.currentLoad >= 0:
			return True
		else:
			return False

	def transfuseToCanister2(self, canister2):
		#fill all water that fits from this canister to canister 2
		emptySpace = canister2.maxLoad - canister2.currentLoad
		if emptySpace > 0:
			self.currentLoad = self.currentLoad - emptySpace
			canister2.currentLoad = canister2.currentLoad + emptySpace
			if self.checkWaterInRange() and canister2.checkWaterInRange():
				return

	def showCanisterGraphic(self):
		print(self.name + ": ")
		for item in range(self.maxLoad - self.currentLoad):
			print("| |")
		for item in range(self.currentLoad):
			print("|#|")
		print("")

	def targetReached(self):
		if self.currentLoad == self.targetLoad:
			print(self.name + " is at target load!!!!!!!!!!!!. Current load: {}, target load: {}".format(self.currentLoad, self.targetLoad))
			return True
		else:
			return False

controller = Controller()
canister1 = Canister("Canister1", 4, 3, 2)
canister2 = Canister("Canister2", 3, 3, 2)


controller.transferUntilExpectedResult(canister1.startingLoad, canister2.startingLoad, canister1.targetLoad, canister2.targetLoad)

"""
canister1.showCanisterGraphic()
canister2.showCanisterGraphic()
canister1.info()
canister2.info()
canister1.transfuseToCanister2(canister2)
canister1.info()
canister2.info()
"""