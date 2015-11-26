### MAIN ###

def main():

	import platform
	import os

	import platform.system().upper() != "LINUX": exit()

	cfg = 'https://github.com/CakeGamingHub/MotherflippinI3WM.git'

	fork = -1
	custom = input("Do you have a custom fork, based off of o4dev's ? (Y/N) ")


	if custom.upper() == 'Y': fork = input("What is the Git repo's https address? ")
	else: fork = "https://github.com/o4dev/i3.git"

	#Set Git Repo to pull i3wm source from

	try:
		open("~/.i3/config", mode='r')
		os.system("sudo cp ~/.i3/config ~/.i3/oldConfig") #Check for existence and backup.

	except Exception as e:
		open("~/.i3/config", mode='w')

		#Create file (blank)

	#Ensure if .i3/config exists it's backed-up

	try:
		if '.git' not in fork: 
			raise NameError

		if 'https://' not in fork:
			raise FutureWarning #Raise specific Exception as it may be a local repo, or not use https, and can handle appropriately

		if 'i3' not in fork:
			raise FutureWarning

	except NameError:
		print("Not a git repo. Cannot continue.")
	
	except FutureWarning:
		print("Check the git repo address.")
		if input("Press Y to continue").upper() != 'Y': exit()

	except Exception as e: print(e)

	#Check repo is likely to exist

	os.system('sudo apt-get purge i3')

	os.system('git pull ' + fork)
	os.system('sudo make')
	os.system('sudo make install')

	#Install i3

	os.system('git pull ' + cfg)
	os.system('rm ~/.i3')
	os.system('cp config ~/.i3/')

	print("Swap XSession to i3wm.")

main()
