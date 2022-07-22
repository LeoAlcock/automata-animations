import random
import sys
import os
import time
import numpy as np


class CellBoard:
	w,h = None, None
	board, boardAux = None, None
	windowAux = None

	def __init__(self, width, height):
		self.w = width
		self.h = height
		self.board = np.zeros((width,height))
		self.boardAux = np.zeros((width,height))
		self.windowAux = [[0 for x in range(3)] for y in range(3)]


	#Specifying data methods/functions. 

	def printBoard(self):
		print("---")
		for x in self.board:
			print(x)
		print("---")

	#pass np ndarray
	def setGrid(self,grid):
		self.board = grid 


	def setRandom(self):
		for i in range(self.w):
			for j in range(self.h):
				self.board[i][j] = random.randint(0,1)

	def getBoard(self):
		return self.board

	def setRandomPrintTime(self):
		t0 = time.perf_counter()
		self.setRandom()
		elapsed = time.perf_counter() - t0
		print("Random ", self.w, " by ", self.h, " board generated in ", elapsed, " seconds.")

	def updatePrint(self):
		self.updateBoard()
		self.printBoard()


	#Calculations/UPdates

	def updateBoard(self):
		for i in range(self.w):
			for j in range(self.h):
				self.boardAux[i][j] = self.updateCell(i,j)

		#Swap board data post update.
		t = self.board
		self.board = self.boardAux
		self.boardAux = t

	#updates the cell at i,j by populating windowAux and passing to an update function. Also been tested!
	def updateCell(self,i,j):
		if(self.board[i][j]==-1):
			return -1
		window = self.windowAux
		for k in range(3):
			for l in range(3):
				a = i+k-1
				b = j+l-1
				if(a < 0 or b < 0 or a >= self.w or b >= self.h):
					window[k][l] = -1
				else:
					window[k][l] = self.board[a][b]

		return self.conwayUpdate(window)


	#3x3 double-array of integers required. Outputs what the middle cell turns into after a Conway Game of Life update. 
	#This has been checked in a rudimentary fashion. 
	def conwayUpdate(self, window):
		cc = window[1][1]
		if(cc==-1):
			return -1
		nCount = 0
		for i in range(3):
			for j in range(3):
				if(window[i][j]==1 and (i!= 1 or j != 1)):
					nCount+= 1
		if(cc==0 and nCount==3):
			return 1
		elif (cc==1 and nCount>=2 and nCount <=3):
			return 1
		else:
			return 0
		return -1


class RPSBoard(CellBoard):
	



#testing shit
if __name__ == '__main__':
	a = TestBoard(5,5)
	a.setRandom()
	a.updateBoard()
	print(a.getBoard())







