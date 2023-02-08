"""
Write a program that computes the values of
1+1.0/ (1!) + 1.0 / (2!) + 1.0 / (3!) + …+ 1.0 / (n!) (eq-1)
(where i! = i x (i-1) x (i-2) x (i-3) x … x 2 x 1)
• Your program should prompt for and read from the keyboard the
value of n. So that for an input n, calculate and display the results of
(eq-1) above. Keep your data as double.
• Check your results for n = 10, 100 and 1000.

3.759
10.536
?

"""
import math
while(1):
	print("Enter a number for how far to calculate the formula 1+ (1/1!) + (1/2!) + (1/3!) ...")
	while (1):
		lvl = input("Enter the level of recursion: ")
		while (lvl.isdigit()==False):
			lvl=input("Enter a number with no letters.")
		lvl=float(lvl)
		if lvl<0:
			print("Enter a non-negative number.")
		else:
			lvl=math.floor(lvl)
			break
	
	
	x=1
	for i in range(1, (lvl+1)):
		'''
		y=1
		
		for j in range (1, (i+1)):
			y=y*j
			'''
		#print("fac of ", lvl, "is :", y)
		#y=1/math.factorial(i)
		x+=(1/math.factorial(i))
	print("Formula to n ", lvl, " is equal to ", x)
	print("\n")
	
