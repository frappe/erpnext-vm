sudo apt-get -y install --no-install-recommends libdbus-1-3
VBOX_ISO=/home/frappe/vbox.iso
sudo mount -o loop $VBOX_ISO /mnt
yes| sudo sh /mnt/VBoxLinuxAdditions.run
sudo umount /mnt

#Cleanup VirtualBox
sudo rm $VBOX_ISO
