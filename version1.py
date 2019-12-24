import re
while(1):
	try:	
		print("choose one of the following: ")
		print("1)Evaluate truth table")
		print("2)Syntax help")
		print("3)Exit")
		choice=int(input("Enter your choice:"))
		if choice==1:
			n=int(input("\nEnter the number of variables in expression: "))
			if n>0 and n<=26:
				var_names=[chr(ord("A")+i) for i in range(n)]
				exp=input("enter expression to evaluate[having A,B,C...etc.): ")
				var=dict.fromkeys(var_names)
				print(*var_names,sep="\t",end="\tOUTPUT\n")

				for i in range(0,2**n):
					temp=list(str(bin(i))[2:].rjust(n,'0'))
					for idx,i in enumerate(var):
						var[i]=temp[idx]
					print(*temp,sep="\t",end="\t")
					temp_exp=exp
					for i in temp_exp:
						if i in var_names:
							temp_exp=re.sub(i,var[i],temp_exp)
					print(eval(temp_exp))
			else:
				print("INVALID INPUT!!")
		elif choice==2:
			print("Variables are always expressed starting from A and then go on to Q,R,S etc... till Z")
			print("| represents OR, & is AND, ~ is NOT, ^ is XOR... use parenthesis wherever necessary")
		elif choice==3:
			exit()
		else:
			print("WRONG CHOICE TRY AGAIN!!")
	except:
		pass
