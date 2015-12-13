#!/usr/bin/python
#
#Conventions:
# (1,4,5)	:(H,H,H) or HHH,  This is what is known. H indicates number of 1s. Here there are total of 10 ones. 
# (H,L,H.L,H)	:L indicates number of 0 s. Our aim is go guess the L which can be one or more to make total of L and H 20.
#  		:HLHLH
#		:H+L+H+L+H = 20( or stripSize)
#Hidden zeros	:lHLHLHl   =20  l's are hidden zeros. It can be none or some
#		:l+H+L+H+L+H+l =20
#		: H strip holds HHH
#		: L strip hold  LL
#		: l strip holds lLLl
#		: z = L+L+L
#		: p = number of H s, for example (H,H,H) is 3
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
	#z=z-(p-1)
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
		 
def formHLpattern(Zarry):
	for z in Zarry:
		print z

	
cstrip = (14,4)
#print expandStrip(cstrip)
zpattern=[]
calculateZeros(1,1)
print zpattern
formHLpattern(zpattern)
