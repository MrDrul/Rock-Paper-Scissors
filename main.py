import random as r
import sys
import time

i = 0#rounds number

win = 0
tie = 0
lose = 0

tie_msg = """


████████╗██╗███████╗██╗██╗
╚══██╔══╝██║██╔════╝██║██║
░░░██║░░░██║█████╗░░██║██║
░░░██║░░░██║██╔══╝░░╚═╝╚═╝
░░░██║░░░██║███████╗██╗██╗
░░░╚═╝░░░╚═╝╚══════╝╚═╝╚═╝"""

win_msg = """


░██╗░░░░░░░██╗██╗███╗░░██╗██╗██╗
░██║░░██╗░░██║██║████╗░██║██║██║
░╚██╗████╗██╔╝██║██╔██╗██║██║██║
░░████╔═████║░██║██║╚████║╚═╝╚═╝
░░╚██╔╝░╚██╔╝░██║██║░╚███║██╗██╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝"""

lose_msg = """


██╗░░░░░░█████╗░░██████╗███████╗██╗░█████╗░
██║░░░░░██╔══██╗██╔════╝██╔════╝██║██╔══██╗
██║░░░░░██║░░██║╚█████╗░█████╗░░██║╚═╝███╔╝
██║░░░░░██║░░██║░╚═══██╗██╔══╝░░╚═╝░░░╚══╝░
███████╗╚█████╔╝██████╔╝███████╗██╗░░░██╗░░
╚══════╝░╚════╝░╚═════╝░╚══════╝╚═╝░░░╚═╝░░"""

#w-l-t variables


rvr = """
    _______              ██╗░░░██╗░██████╗              _______
---'   ____)             ██║░░░██║██╔════╝             (____   '---
      (_____)            ╚██╗░██╔╝╚█████╗░            (_____)
      (_____)            ░╚████╔╝░░╚═══██╗            (_____)
      (____)             ░░╚██╔╝░░██████╔╝             (____)
---.__(___)              ░░░╚═╝░░░╚═════╝░              (___)__.---"""
rvp = """
    _______              ██╗░░░██╗░██████╗                   _______
---'   ____)             ██║░░░██║██╔════╝              ____(____   '---
      (_____)            ╚██╗░██╔╝╚█████╗░             (______
      (_____)            ░╚████╔╝░░╚═══██╗            (_______
      (____)             ░░╚██╔╝░░██████╔╝             (_______
---.__(___)              ░░░╚═╝░░░╚═════╝░              (___________.---"""
rvs = """
    _______              ██╗░░░██╗░██████╗                   _______
---'   ____)             ██║░░░██║██╔════╝              ____(____   '---
      (_____)            ╚██╗░██╔╝╚█████╗░             (______
      (_____)            ░╚████╔╝░░╚═══██╗            (__________
      (____)             ░░╚██╔╝░░██████╔╝                  (____)
---.__(___)              ░░░╚═╝░░░╚═════╝░                   (___)__.---"""






pvp = """
    _______              ██╗░░░██╗░██████╗              _______
---'   ____)____         ██║░░░██║██╔════╝         ____(____   '---
          ______)        ╚██╗░██╔╝╚█████╗░        (______
          _______)       ░╚████╔╝░░╚═══██╗       (_______
         _______)        ░░╚██╔╝░░██████╔╝        (_______
---.__________)          ░░░╚═╝░░░╚═════╝░         (___________.---"""
pvr = """
    _______              ██╗░░░██╗░██████╗         _______
---'   ____)____         ██║░░░██║██╔════╝        (____   '---
          ______)        ╚██╗░██╔╝╚█████╗░       (_____)
          _______)       ░╚████╔╝░░╚═══██╗       (_____)
         _______)        ░░╚██╔╝░░██████╔╝        (____)
---.__________)          ░░░╚═╝░░░╚═════╝░         (___)__.---"""
pvs = """
    _______              ██╗░░░██╗░██████╗              _______
---'   ____)____         ██║░░░██║██╔════╝         ____(____   '---
          ______)        ╚██╗░██╔╝╚█████╗░        (______
          _______)       ░╚████╔╝░░╚═══██╗       (__________
         _______)        ░░╚██╔╝░░██████╔╝              (____)
---.__________)          ░░░╚═╝░░░╚═════╝░              (___)__.---"""




svs = """
    _______              ██╗░░░██╗░██████╗              _______
---'   ____)____         ██║░░░██║██╔════╝         ____(____   '---
          ______)        ╚██╗░██╔╝╚█████╗░        (______
       __________)       ░╚████╔╝░░╚═══██╗       (__________
      (____)             ░░╚██╔╝░░██████╔╝              (____)
---.__(___)              ░░░╚═╝░░░╚═════╝░              (___)__.---"""
svr = """
    _______              ██╗░░░██╗░██████╗         _______
---'   ____)____         ██║░░░██║██╔════╝        (____   '---
          ______)        ╚██╗░██╔╝╚█████╗░       (_____)
       __________)       ░╚████╔╝░░╚═══██╗       (_____)
      (____)             ░░╚██╔╝░░██████╔╝        (____)
---.__(___)              ░░░╚═╝░░░╚═════╝░         (___)__.---"""

svp = """
    _______              ██╗░░░██╗░██████╗              _______
---'   ____)____         ██║░░░██║██╔════╝         ____(____   '---
          ______)        ╚██╗░██╔╝╚█████╗░        (______
       __________)       ░╚████╔╝░░╚═══██╗       (_______
      (____)             ░░╚██╔╝░░██████╔╝       (_______
---.__(___)              ░░░╚═╝░░░╚═════╝░         (___________.---"""




		

#Start messege
print("""							░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░  
							░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗  
							░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║  
							░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║  
							░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝  
							░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░  

					██████╗░░█████╗░░█████╗░██╗░░██╗   ██████╗░░█████╗░██████╗░███████╗██████╗░  ░██████╗░█████╗░██╗░██████╗░██████╗░█████╗░██████╗░░██████╗
					██╔══██╗██╔══██╗██╔══██╗██║░██╔╝   ██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗  ██╔════╝██╔══██╗██║██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝
					██████╔╝██║░░██║██║░░╚═╝█████═╝░   ██████╔╝███████║██████╔╝█████╗░░██████╔╝  ╚█████╗░██║░░╚═╝██║╚█████╗░╚█████╗░██║░░██║██████╔╝╚█████╗░
					██╔══██╗██║░░██║██║░░██╗██╔═██╗░   ██╔═══╝░██╔══██║██╔═══╝░██╔══╝░░██╔══██╗  ░╚═══██╗██║░░██╗██║░╚═══██╗░╚═══██╗██║░░██║██╔══██╗░╚═══██╗
					██║░░██║╚█████╔╝╚█████╔╝██║░╚██╗   ██║░░░░░██║░░██║██║░░░░░███████╗██║░░██║  ██████╔╝╚█████╔╝██║██████╔╝██████╔╝╚█████╔╝██║░░██║██████╔╝
					╚═╝░░╚═╝░╚════╝░░╚════╝░╚═╝░░╚═╝   ╚═╝░░░░░╚═╝░░╚═╝╚═╝░░░░░╚══════╝╚═╝░░╚═╝  ╚═════╝░░╚════╝░╚═╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░

						██╗░░░██╗██╗░░░░░████████╗██╗███╗░░░███╗░█████╗░████████╗███████╗ ███████╗██████╗░██╗████████╗██╗░█████╗░███╗░░██╗
						██║░░░██║██║░░░░░╚══██╔══╝██║████╗░████║██╔══██╗╚══██╔══╝██╔════╝ ██╔════╝██╔══██╗██║╚══██╔══╝██║██╔══██╗████╗░██║
						██║░░░██║██║░░░░░░░░██║░░░██║██╔████╔██║███████║░░░██║░░░█████╗░░ █████╗░░██║░░██║██║░░░██║░░░██║██║░░██║██╔██╗██║
						██║░░░██║██║░░░░░░░░██║░░░██║██║╚██╔╝██║██╔══██║░░░██║░░░██╔══╝░░ ██╔══╝░░██║░░██║██║░░░██║░░░██║██║░░██║██║╚████║
						╚██████╔╝███████╗░░░██║░░░██║██║░╚═╝░██║██║░░██║░░░██║░░░███████╗ ███████╗██████╔╝██║░░░██║░░░██║╚█████╔╝██║░╚███║
						░╚═════╝░╚══════╝░░░╚═╝░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝ ╚══════╝╚═════╝░╚═╝░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝




----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------""")

name = input("Challenger. Enter your name!")

time.sleep(0.5)
	#Aghas = Master!
if name.capitalize() == "Aghas" or name.capitalize() == "Aghasy":
	print("""░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ██████╗░░█████╗░░█████╗░██╗░░██╗  ███╗░░░███╗░█████╗░░██████╗████████╗███████╗██████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ██████╦╝███████║██║░░╚═╝█████═╝░  ██╔████╔██║███████║╚█████╗░░░░██║░░░█████╗░░██████╔╝
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ██╔══██╗██╔══██║██║░░██╗██╔═██╗░  ██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░██╔══██╗
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ██████╦╝██║░░██║╚█████╔╝██║░╚██╗  ██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░███████╗██║░░██║
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝""")


else:
	print("Welcome to RPS Ultimate Edition " + name.capitalize() + "!")
time.sleep(1)

def fst_ready():

	if name.capitalize() == "Aghas" or name.capitalize() == "Aghasy":
		answer = input("Are you ready for the battle Master?(y/n)")


	else:
		answer = input("Are you ready for the battle " + name.capitalize() + "?(y/n)")

	time.sleep(0.5)

	if answer == "y" or answer == "Y":
		print("""████████╗██╗░░██╗███████╗███╗░░██╗   ██╗░░░░░███████╗████████╗  ████████╗██╗░░██╗███████╗  ██████╗░░█████╗░████████╗████████╗██╗░░░░░███████╗   ██████╗░███████╗░██████╗░██╗███╗░░██╗██╗██╗   
╚══██╔══╝██║░░██║██╔════╝████╗░██║   ██║░░░░░██╔════╝╚══██╔══╝  ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░░░██╔════╝   ██╔══██╗██╔════╝██╔════╝░██║████╗░██║██║██║
░░░██║░░░███████║█████╗░░██╔██╗██║   ██║░░░░░█████╗░░░░░██║░░░  ░░░██║░░░███████║█████╗░░  ██████╦╝███████║░░░██║░░░░░░██║░░░██║░░░░░█████╗░░   ██████╦╝█████╗░░██║░░██╗░██║██╔██╗██║██║██║
░░░██║░░░██╔══██║██╔══╝░░██║╚████║   ██║░░░░░██╔══╝░░░░░██║░░░  ░░░██║░░░██╔══██║██╔══╝░░  ██╔══██╗██╔══██║░░░██║░░░░░░██║░░░██║░░░░░██╔══╝░░   ██╔══██╗██╔══╝░░██║░░╚██╗██║██║╚████║╚═╝╚═╝
░░░██║░░░██║░░██║███████╗██║░╚███║   ███████╗███████╗░░░██║░░░  ░░░██║░░░██║░░██║███████╗  ██████╦╝██║░░██║░░░██║░░░░░░██║░░░███████╗███████╗   ██████╦╝███████╗╚██████╔╝██║██║░╚███║██╗██╗
░░░╚═╝░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚══╝   ╚══════╝╚══════╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚══════╝╚══════╝   ╚═════╝░╚══════╝░╚═════╝░╚═╝╚═╝░░╚══╝╚═╝╚═╝
""")
		time.sleep(0.25)

		print("""	Please choose one of the options below:
	>>>Rock : R/r
	>>>Paper : P/p
	>>>Scissors : S/s
	The best one wins!!!
""")
	elif answer == "n" or answer == "N":
		print("OK then... GoodBye!")
		sys.exit()


	else:
		print("Error : IncorrectInput")

		return fst_ready()


fst_ready()

	
def final_contest(win, lose, tie, i):

	#basic rps
	#paper id = 1
	#rock id = 2
	#sci id = 3


	ai_choice = 0#ai element id
	k = 0#player element id

	ai_choice = r.choice([1, 2, 3])
	user_choice = input("""input your element!
>>>""")
	if user_choice == "r" or user_choice == "R":
		k = 2

	elif user_choice == "p" or user_choice == "P":
		k = 1
		
	elif user_choice == "s" or user_choice == "S":
		k = 3
		
	else:
		print("Invalid Element Id please try again")
		return final_contest(win, lose, tie, i)


#id we need to know who wins
	i += 1
	print("=" * 15)
	print("R O U N D " + str(i))
	print("=" * 15)
	time.sleep(1)
	

	if k == 1 and ai_choice == 1:
		tie += 1
		print(pvp)
		time.sleep(0.75)
		print(tie_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")
		

	elif k == 1 and ai_choice == 2:
		win += 1
		print(pvr)
		time.sleep(0.75)
		print(win_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")

	elif k == 1 and ai_choice == 3:
		lose += 1
		print(pvs)
		time.sleep(0.75)
		print(lose_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")



	elif k == 2 and ai_choice == 1:
		lose += 1
		print(rvp)
		time.sleep(0.75)
		print(lose_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")
	elif k == 2 and ai_choice == 2:
		tie += 1
		print(rvr)
		time.sleep(0.75)
		print(tie_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")

	elif k == 2 and ai_choice == 3:
		win += 1
		print(rvs)
		time.sleep(0.75)
		print(win_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")


	elif k == 3 and ai_choice == 1:
		lose += 1
		print(svp)
		time.sleep(0.75)
		print(win_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")
	elif k == 3 and ai_choice == 2:
		win += 1
		print(svr)
		time.sleep(0.75)
		print(lose_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")

	elif k == 3 and ai_choice == 3:
		tie += 1
		print(svs)
		time.sleep(0.75)
		print(tie_msg)
		time.sleep(0.75)
		print("\nWin-Lose-Tie statistics  \\/" "\nTies > " + str(tie), "\nWins > " + str(win), "\nLosses > " + str(lose))
		while True:
			countinue = input("Continue Contest?(y/n)")
			if countinue == "y" or countinue == "Y":
				return final_contest(win, lose, tie, i)
				break
			
			elif countinue == "n" or countinue == "N":
				print("Ok GoodBye!")
				sys.exit()
			else:
				print("Invalid input. Try again")

final_contest(win, lose, tie, i)




"""
	def continue_request():
	while True:
		countinue = input("Continue Contest?(y/n)")
		if countinue == "y" or countinue == "Y":
			
		elif countinue == "n" or countinue == "N":
			print("Ok GoodBye!")
			sys.exit()
		else:
			print("Invalid input. Try again")



"""

