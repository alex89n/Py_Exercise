str = "aleksaNdaR"

upper_c = []

tmp = ""
for i in range(0, len(str)):
    if str[i].isupper():
        tmp += str[i]
    elif str[i].isupper() and str[i-1].islower():
        tmp += ' ' + str[1]
    else:
        tmp += str[i]
print tmp

if str[6].isupper() and str[5].islower():
    print "  lll" + str[6]

        
# for i in str:
    # if chr.isupper():
        # tmp += chr
    # elif chr.isupper() and     
# print tmp

# for i in range(1, len(upper_c)):
    # print str.split(upper_c[i])
        
# # # print "Capital Letters: ", sum(1 for c in str if c.isupper())

# def split_uppercase(str):
	# x = ''
	# i = 0
	# for c in str:
		# # print c, str[i-1]
		# if i == 0: 
			# x += c
		# elif c.isupper() and not str[i-1].isupper():
			# x += ' %s' % c
		# else:
			# x += c
		# i += 1
        # print x
	# return x

# split_uppercase(str) 