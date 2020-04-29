#!/bin/sh
  
if [ -f "/usr/share/applications/ivs-calc" ]; then
    echo "The application ivs-calc is now going to be uninstalled. Do you want to continue? (y/n)"
    read answer

    if echo "$answer" | grep -iq "^y" ;then
	    sudo rm /usr/share/applications/ivs-calc
        sudo rm -rf /usr/share/ivs-calc
        sudo rm /usr/share/applications/ivs-calc.desktop
        sudo rm /usr/share/applications/ivs-calc-uninstaller.desktop
        sudo rm /usr/share/applications/uninstall.sh

        echo "Application uninstallation was successful."
    else
        echo "Application uninstallation was unsuccessful."
        exit
    fi

else
    echo "Application does not exist."
    exit
fi