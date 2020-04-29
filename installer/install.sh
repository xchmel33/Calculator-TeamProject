#!/bin/sh

dependency0=python3
dependency1=pip3
dependency2=pyinstaller
dependency3=xterm
dependency4=pyqt5

isInstalled0=false #python3
isInstalled1=false #pip3
isInstalled2=false #pyinstaller
isInstalled3=false #xterm
isInstalled4=false #pyqt5

isInstalledAll=true

if [ -f "/usr/share/ivs-calc" ]; then
    echo "This application is already installed."
else
    for i in $(seq 0 3)
    do
        if eval which "\$dependency$i" > /dev/null; then
            eval isInstalled$i=true
        else
            eval isInstalled$i=false
            isInstalledAll=false
        fi
    done

    if pip3 show $dependency4 > /dev/null; then
        isInstalled4=true
    else 
        isInstalled4=false
        isInstalledAll=false
    fi

    if [ "$isInstalledAll" = "false" ]; then
        echo "You need to install following dependencies for calculator to work: "
        
        for i in $(seq 0 4)
        do
            if eval \$isInstalled$i; then
                printf ""
            else 
                eval echo "\ \$dependency$i"
            fi
        done

        echo "Do you wish to install them? (y/n)"
        read answer

        if echo "$answer" | grep -iq "^y"; then
            if eval \$isInstalled0; then
                printf ""
            else 
                sudo -H apt-get install python3.8
            fi

            if eval \$isInstalled1; then
                printf ""
            else 
                sudo -H apt-get install python3-pip
            fi

            if eval \$isInstalled2; then
                printf ""
            else 
                sudo -H pip3 install pyinstaller
            fi

            if eval \$isInstalled3; then
                printf ""
            else 
                sudo -H apt-get install xterm
            fi

            if eval \$isInstalled4; then
                    printf ""
            else 
                sudo -H pip3 install pyqt5==5.14
            fi
        else
            echo "Application installation was unsuccessful."
            exit
        fi
    fi

    echo "Application ivs-calc will be installed now. Do you wish to continue? (y/n)"
    read answer

    if echo "$answer" | grep -iq "^y"; then
        pyinstaller -F ../src/gui.py

        sudo mv ./dist/gui /usr/share/applications/ivs-calc
        sudo mkdir /usr/share/ivs-calc
        sudo cp ../ivs-calc-icon.png /usr/share/ivs-calc
        sudo cp ../ivs-calc-icon-uninstaller.png /usr/share/ivs-calc

        if [ ! -e "ivs-calc.desktop" ]; then 
            echo "[Desktop Entry]" >> "ivs-calc.desktop"
            echo "Type=Application" >> "ivs-calc.desktop"
            echo "Terminal=false" >> "ivs-calc.desktop"
            echo "Exec=/usr/share/applications/ivs-calc" >> "ivs-calc.desktop"
            echo "Name=ivs-calc" >> "ivs-calc.desktop"
            echo "Icon=/usr/share/ivs-calc/ivs-calc-icon.png" >> "ivs-calc.desktop"
        fi

        sudo mv ./ivs-calc.desktop /usr/share/applications
        sudo chmod +x "/usr/share/applications/ivs-calc.desktop"
        xdg-desktop-menu install /usr/share/applications/ivs-calc.desktop

        sudo cp ./uninstall.sh /usr/share/applications
        sudo chmod +x "/usr/share/applications/uninstall.sh"
        cp /usr/share/applications/uninstall.sh ./
    
        if [ ! -e "ivs-calc-uninstaller.desktop" ]; then
            echo "[Desktop Entry]" >> "ivs-calc-uninstaller.desktop"
            echo "Type=Application" >> "ivs-calc-uninstaller.desktop"
            echo "Terminal=true" >> "ivs-calc-uninstaller.desktop"
            echo "Exec=/usr/share/applications/uninstall.sh" >> "ivs-calc-uninstaller.desktop"
            echo "Name=ivs-calc-uninstaller" >> "ivs-calc-uninstaller.desktop"
            echo "Icon=/usr/share/ivs-calc/ivs-calc-icon-uninstaller.png" >> "ivs-calc-uninstaller.desktop"
        fi 

        sudo mv ./ivs-calc-uninstaller.desktop /usr/share/applications
        sudo chmod +x "/usr/share/applications/ivs-calc-uninstaller.desktop"
        xdg-desktop-menu install /usr/share/applications/ivs-calc-uninstaller.desktop

        sudo rm -rf ./dist
        sudo rm -rf ./build
        sudo rm -rf ./gui.spec
        sudo rm -rf ../src/__pycache__

        echo "Application installation was successful."

    else
        echo "Application installation was unsuccessful."
        exit
    fi

fi