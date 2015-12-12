#!/usr/bin/python
#
stripSize = 20
def expandStrip(x):
	stripLenth = 0
	for d in x: 
		stripLenth = stripLenth + d
	#print stripLenth
	calculateZeros(len(x), stripSize - stripLenth)
	return  stripSize - stripLenth 
#Calculate for ecah position number of zeros for a total of z	
def calculateZeros(z,p):
	#print z, p
	z=z-(p-1)
	d= (10**(p+1))
	#print d , z
	for digits in range(d):
		#print digits
		tempd  = digits
		reminder = 0
		zeros =0
		while tempd != 0:
			reminder = tempd%10
			tempd = tempd//10
			zeros = zeros + reminder
		if zeros == z:
			#print digits
			zpattern.append(digits)
		 

	
cstrip = (14,4)
#print expandStrip(cstrip)
zpattern=[]
calculateZeros(10,4)
print zpattern

