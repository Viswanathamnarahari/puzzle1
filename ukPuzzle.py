#!/usr/bin/python
#
#Conventions:
# (1,4,5)	:(H,H,H) or HHH,  This is what is known.
#  H indicates number of 1 s cover by the H. Here H =1, H =4, H =5
# (H,L,H.L,H)	:L indicates number of 0 s.
# Our aim is go guess the L which can be one or more to make total of L and H 20.
#  		:HLHLH
#		:H+L+H+L+H = 20( or stripSize)
#Hidden zeros	:lHLHLHl   =20  l's are hidden zeros. It can be none or some
#		:l+H+L+H+L+H+l =20
#H_strip holds H,H,H
#L_strip hold  LL
#l_strip holds lLLl
#z = L+L+L
#p = number of H s, for example (H,H,H) is 3
# 

stripSize = 20
def get_z_p(x):
	numberofOnes = 0
	for d in x: 
		numberofOnes  = numberofOnes + d
	neededZeros = stripSize - numberofOnes - (len(x) - 1)
        #calculateZeros(neededZeros,len(x))
	return(neededZeros,len(x))

#get L or l for p  position a total of z	
def calculateZeros(z,p):
	#print z, p
	#z=z-(p-1) 
	d= (10**(p+1))
	pading = 10**(p+1) 	# left most pad is added for convinience and save CPU time for later process. 
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
			digits = digits + pading
			zpattern.append(digits)
			lpattern.append(tuple(str(digits)))
		 
def formHLpattern(Zarry):
	print Zarry[0], H_strip
	print lpattern[0], H_strip
	# typical data : 10008 (1, 4, 5)
	#		 12411 (1, 4, 5) 
	#		 xlLLl (H, H, H)
	#	          lHLHLHl	
	# ('1', '0', '0', '0', '8') (1, 4, 5)
	#   x    l    L    L    l    H  H  H
	# x - padding, which can be ignored. 
	# l - if zero ignore. If not add l corresponding zeros before corresponding H
	# L - add L+1 zeros before corresponding H
	#
	for i in range(len(H_strip)):
		print H_strip[i]
H_strip = (1,4,5)
print get_z_p(H_strip)
lpattern=[]
zpattern=[]
calculateZeros(8,3)
print zpattern
formHLpattern(zpattern)
