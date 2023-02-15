
# Libraries to Import
import json
import shodan
import string
from datetime import datetime


# Disclaimer
print('\n--------------------------------------------------')
print('Bishodan Tool to Check Servers Exposure on Shodan.')
print('Part of The Digimon Suite by 5VPH3R.')
print('--------------------------------------------------\n')


# Function that returns the current date and time; used to keep track of execution times of different commands
def dt():
	now = datetime.today().strftime("%Y/%m/%d %T")
	return now


# Define the Shodan API Connector
api = shodan.Shodan('<insert_your_api_here')


# Run the script for as long as the user desires until the user explicitly exits the script
while True:
	# Ask the user to provide the desired IP address
	print('\n[+] [',dt(),'] : ', end='')
	ip = input('Enter the desired IP address: ')


	# Perform the search and print out the results
	try:
		host_info = api.host(ip)
		# Print the results in a nicely-formatted JSON output
		print('\n[+] [',dt(),'] : ', end='')
		print(json.dumps(host_info, indent=4))
	except shodan.APIError as e:
		print('\n[+] [',dt(),'] : ', end='')
		print('Error: %s' % e)

	# Ask the user if they wish to search for another IP address
	while True:
		print('\n[+] [',dt(),'] : ', end='')
		new_search = input("Would you like to search for another IP address? (y/n): ")

		if new_search.lower() == 'n':
			print('\n[+] [',dt(),'] : ', end='')
			print("Thank you for using Bishodan by 5VPH3R!\n")
			exit()
		elif new_search.lower() == 'y':
			break
		else:
			print('\n[+] [',dt(),'] : ', end='')
			print("Invalid input. Please enter 'y' or 'n' in the following prompt.")
