# Currency Converter
# Made by: Abdulahi Osoble
# Values that can be converted or converted to: AED, USD, EURO, POUND.
# Data to be used:
# 1 AED = 0.27 USD, 1 AED = 0.24 EURO, 1 AED = 0.21 POUND
# 1 USD = 3.67 AED, 1 USD = 0.89 EURO, 1 USD = 0.76 POUND
# 1 EURO = 4.11 AED, 1 EURO = 1.12 USD, 1 EURO = 0.85 POUND
# 1 POUND = 4.82 AED, 1 POUND = 1.31 USD, 1 POUND = 1.17 EURO

def toAED(s, i):
	if i == 1:
		print "%f AED" %s
	elif i == 2:
		s *= 3.67
		print "%f AED" %s
	elif i == 3:
		s *= 4.11
		print "%f AED" %s
	elif i == 4:
		s *= 4.82
		print "%f AED" %s
	doAgain()
		
def toUSD(s, i):
	if i == 1:
		s /= 3.67
		print "%f USD" %s
	elif i == 2:
		print "%f USD" %s
	elif i == 3:
		s /= 0.89
		print "%f USD" %s
	elif i == 4:
		s /= 0.76
		print "%f USD" %s
	doAgain()

def toEURO(s, i):
	if i == 1:
		s /= 4.82
		print "%f EUR" %s
	elif i == 2:
		s /= 1.12
		print "%f EUR" %s
	elif i == 3:
		print "%f EUR" %s
	elif i == 4:
		s /= 0.85
		print "%f EUR" %s
	doAgain()

def toPOUND(s, i):
	if i == 1:
		s /= 4.11
		print "%f POUND" %s
	elif i == 2:
		s /= 1.31
		print "%f POUND" %s
	elif i == 3:
		s /= 1.17
		print "%f POUND" %s
	elif i == 4:
		print "%f POUND" %s
	doAgain()


def inputF():
	input1 = int(raw_input("What would you like to convert: 1)AED  2)USD  3)EURO  4)POUND:  "))
	input2 = int(raw_input("What would you like to convert it to: 1)AED  2)USD  3)EURO  4)POUND:  "))
	amount = float(raw_input("Enter amount to convert:  "))
	print"--------------------------------------------------------"
	if input1 < 1 or input1 > 4:
		print"Invalid choice!!"
	if input2 == 1:
		toAED(amount, input1)
	elif input2 == 2:
		toUSD(amount, input1)
	elif input2 == 3:
		toEURO(amount, input1)
	elif input2 == 4:
		toPOUND(amount, input1)
	else:
		print"Invalid choice!!"


def doAgain():
	choice = raw_input("Would you like to convert anything else?  ")
	if choice == 'y' or choice == 'Y':
		inputF()
	else:
		print "Have a nice day! "

inputF()

