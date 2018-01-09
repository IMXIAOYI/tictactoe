######problem one

#subproblem: draw board
#parameter: choice[]
#returns: no return 
def drawboard(choice):
	print(choice[0]+"|"+choice[1]+"|"+choice[2]+"\n")
	print("-----------------\n")
	print(choice[3]+"|"+choice[4]+"|"+choice[5]+"\n")
	print("-----------------\n")
	print(choice[6]+"|"+choice[7]+"|"+choice[8]+"\n")


#subproblem: ask users to input and also deal with invalid input 
#parameters: boolean xturn
#returns: input
def askforinput(x):
	if(x):
		move=int(input("Player X, please move:"))
	else:
		move=int(input("Player O, please move:"))
	return move


#subproblem: is there a winnner?
#parameter: alist
#return: boolean 
def winner(alist):
	if set([0,1,2])<=set(alist) or set([3,4,5])<=set(alist) or set([6,7,8])<=set(alist) or set([0,3,6])<=set(alist) or set([1,4,7])<=set(alist) or set([2,5,8])<=set(alist) or set([0,4,8])<=set(alist) or set([2,4,6])<=set(alist):
		return True
	else: 
		return False


#subproblem: is there a tie?
#paramenter: xlist,ylist
#return:boolean 
def tie(xlist,ylist):
	if(set(xlist+ylist)==set(range(9))):
		print("This is a tie!")
		return True
	else:
		return False

if __name__=='__main__':
	print("valid moves are 0,1,2,3,4,5,6,7,8");
	choice=['     ']*9
	xturn=True
	haswinner=False
	hastie=False
	xlist=[]
	ylist=[]

	while not haswinner and not hastie:
		drawboard(choice)
		move=askforinput(xturn)
		if(move not in range(9)):
			print("valid input are 0-8")
		elif (move in xlist or move in ylist):
			print("this place has been taken, choose another place")
		else:
			if(xturn):
				xturn=False
				xlist.append(move)
				choice[move]='  x  '
				if(winner(xlist)):
					print("X wins!")
					haswinner=True
				elif(tie(xlist,ylist)):
					drawboard(choice)
					hastie=True
			else:
				xturn=True
				ylist.append(move)
				choice[move]='  O  '
				if(winner(ylist)):
					print("O wins!")
					haswinner=True
				elif(tie(xlist,ylist)):
					drawboard(choice)
					hastie=True







