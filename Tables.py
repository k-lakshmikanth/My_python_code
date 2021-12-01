import random
def main():
	try:
		x=int(input("Which table you want to practice:"))

		print()
		for i in range (25):
			y=random.randrange(2,11)
			z=x*y
			try:
				a=int(input("{} X {} =".format(x,y)))
				if a != z:
					print(">>>INCORRECT<<<")
				else:
					pass
			except ValueError:
				pass
		print("you pracitced",x,"table\n")
		print()
		print(x,'table:')
		print()
		for i in range(1,11):
			print("{}*{}={}".format(x,i,x*i))
		input()
	except ValueError:
		main()
main()