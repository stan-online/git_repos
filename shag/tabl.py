import random

def randomise():
	x = random.randint(1,10)
	y = random.randint(1,10)
	print(x, "*", y, "= ?")
	return x * y

def main():
	answer = randomise()
	z = input()
	try:
		if answer == int(z):
			print("good")
		else:
			print("It is bad answer, please try again")
			main()
	except Exception:
		if z == "exit":
			sys.exit()
		else:
		    print("type a number")
		    main()
main()		    	