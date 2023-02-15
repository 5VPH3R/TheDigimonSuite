
# Libraries to import
import random
import string
from datetime import datetime


# Disclaimer
print('\n----------------------------------------------------------')
print('Reppassword Mugenerator Tool to Generate Secure Passwords.')
print('Part of The Digimon Suite by 5VPH3R.')
print('----------------------------------------------------------\n')


# Function that returns the current date and time; used to keep track of execution times of different commands
def dt():
	now = datetime.today().strftime("%Y/%m/%d %T")
	return now

# Run the script for as long as the user desires until the user explicitly exits the script
while True:
	# Ask the user to provide the desired length of the new password
	while True:
		try:
			print('\n[+] [',dt(),'] : ', end='')
			length = int(input('Enter the desired length for your new password (1 <= length <= 70): '))
		except ValueError:
			print('\n[+] [',dt(),'] : ', end='')
			print('The entered value is not a number. Please enter a valid number within stated range.', end='')
		else:
			if 1 <= length <= 70:
				break
			else:
				print('\n[+] [',dt(),'] : ', end='')
				print('The entered value is out of range. Please enter a number within stated range.', end='')


	# Define the arrays of different sets of characters that will be used to generate the new password randomly
	## Array of digits
	digs = string.digits
	## Array of lowercase characters
	lowchars = string.ascii_lowercase
	## Array of uppercase characters
	uppchars = string.ascii_uppercase
	## Array of symbols
	syms = '!@#$%&-_.'
	## Array of all combined arrays of characters
	comb = digs + lowchars + uppchars + syms


	# Generate the secured random password in a temporary variable
	tmp_pass = random.sample(comb,length)

	# Transform the secured random password from an array of characters to a string of characters
	password = "".join(tmp_pass)


	# Print out the secured random password to the user
	print('\n[+] [',dt(),'] : ', end='')
	print('your new password is: ', password, '\n')

	# Ask the user if they wish to generate a new password
	while True:
		print('\n[+] [',dt(),'] : ', end='')
		new_password = input("Would you like to generate a new password? (y/n): ")

		if new_password.lower() == 'n':
			print('\n[+] [',dt(),'] : ', end='')
			print("Thank you for using Reppassword Mugenerator by 5VPH3R!\n")
			exit()
		elif new_password.lower() == 'y':
			break
		else:
			print('\n[+] [',dt(),'] : ', end='')
			print("Invalid input. Please enter 'y' or 'n' in the following prompt.")
