s = "1,2,3,4,5,6,7,8,9,10"
s.split(",")
print s, 

a,b,c,d,e,f,g,h,i,j = s.split(",")
print s,
compute_num = d

response = raw_input("Guess a number: ")

while response != compute_num:
	if response < compute_num:
		print "too low"
		break
	elif response > compute_num:
		print "too high"
		break
else:
	print "You win"
	


