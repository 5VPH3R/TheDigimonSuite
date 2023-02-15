
#!/bin/bash

# To be placed in "/usr/local/bin" for system-wide access
# Create alias garurupdate="bash garurupdate.sh" for easier usage (add 'sudo' if you are not root)


# Disclaimer
echo ""
echo "--------------------------------------------------"
echo "Garurupdate Script to update Debian-based systems."
echo "Part of The Digimon Suite by 5VPH3R."
echo "--------------------------------------------------"
echo ""


# Exit script with error message if no flags are set
if [[ $# -eq 0 ]]
then
    echo "Error: no flags set"
	echo "Use 'garurupdate -h' for help manual"
    exit 1
fi


# Functions Area

# Function that displays Help message
help_function(){
	echo "usage: garurupdate [flag]"
	echo ""
	echo "flags:"
	echo "    -e:        exit script after update is complete"
	echo "    -p:        poweroff system after update is complete"
	echo "    -r:        reboot system after update is complete"

	exit
}

# Function that returns the current date and time; used to keep track of execution times of different commands
dt(){
    date +'%Y/%m/%d %T'
}

# Function that sends a poweroff command to the system after update is complete

poweroff_function(){
	sleep 1; echo -n "Powering off in 3... "; sleep 1; echo -n "2... "; sleep 1; echo -n "1..."; sleep 1;

    poweroff
}

# Function that sends a poweroff command to the system after update is complete

reboot_function(){
	sleep 1; echo -n "Rebooting in 3... "; sleep 1; echo -n "2... "; sleep 1; echo -n "1..."; sleep 1;
	
    reboot
}

# Function that exits the script after update is complete
exit_function(){
    exit
}


# Main Area

# Display help message when requested
if [[ $1 == '-h' ]]
then
	help_function
fi

# Update sources
echo ""
echo "-------------------------------------------"
echo "[+] [$(dt)] Updating sources:"
echo "-------------------------------------------"
echo ""

apt update

echo ""
echo "[+] [$(dt)] Waiting for changes to take effect..."
sleep 3
echo "[+] [$(dt)] Done."
sleep 1
echo ""

# Update packages
echo ""
echo "--------------------------------------------"
echo "[+] [$(dt)] Updating packages:"
echo "--------------------------------------------"
echo ""

apt full-upgrade -y

echo ""
echo "[+] [$(dt)] Waiting for changes to take effect..."
sleep 3
echo "[+] [$(dt)] Done."
sleep 1
echo ""

# Clean unused packages
echo ""
echo "---------------------------------------------------"
echo "[+] [$(dt)] Cleaning unused packages:"
echo "---------------------------------------------------"
echo ""

apt autoremove -y

echo ""
echo "[+] [$(dt)] Waiting for changes to take effect..."
sleep 3
echo "[+] [$(dt)] Done."
sleep 1
echo ""

# Proceed to executing user's choice
echo ""
echo "--------------------------------------------------------------------"
echo "[+] [$(dt)] Update complete."
echo ""
echo "[+] [$(dt)] Thank you for using Garurupdate by 5VPH3R!"
echo "--------------------------------------------------------------------"
echo ""

while getopts "epr" flag
do
	case "${flag}" in
		e) exit_function;;
		p) poweroff_function;;
		r) reboot_function;;
	esac
done
