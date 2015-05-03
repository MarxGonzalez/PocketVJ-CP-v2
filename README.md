# PocketVJ Control Panel 2.0

http://www.pocketvj.com

This file is used to control the PocketVJ over the webbrowser.

Clone everything into the `/var/www/` directory.

This file is only useful if you use the omxplayer-sync https://github.com/turingmachine/omxplayer-sync script.
Read turingmachines installation instructions and get the custom build of omxplayer.

##Instruction

Add www-data to your sudoers list with: `visudo` add this line at the end: `www-data ALL=(ALL) NOPASSWD: ALL`

Allow php with: `sudo lighty-enable-mod fastcgi-php`

The videofiles have to be stored in `/media/internal/video`
The imagefiles have to be stored in `/media/internal/images`

We recommend to use your RPi as a Hotspot, setup as described here: http://elinux.org/RPI-Wireless-Hotspot

###To do:
- Create a .torrent image for download (anyone can tell me where to put a 16GB image as torrent?)
- Make sync script to act faster at beginning of video
- Make sync script compatible with video mapper
- Automaticly detect when slave is connected while already playing (ifplug.d)
- Fix Video Mapper input texture issue
- Automaticly convert incompatible movies
- Master Slave auto-detection
- Add pause function
- Add screenshot function
- Integrate LPMT
- Integrate RaspiVJ function for videomixing
- OSC support
- Artnet output for lightning control
- DMX Creator bridge
- Add new HD testfiles by Manuel Berner
- Start all functions without reboot


###Dependencies to install:

apt-get -y install ntfs-3g

apt-get -y install python-pexpect

apt-get -y install vim

apt-get -y install figlet

apt-get -y install git-core

apt-get -y install firmware-ralink

apt-get -y install hostapd

apt-get -y install isc-dhcp-server

apt-get -y install lighttpd

apt-get -y install samba samba-common-bin

apt-get -y install php5-common php5-cgi php5 php5-mysql

apt-get -y install screen

apt-get -y install fbi

apt-get -y install ttf-mscorefonts-installer

apt-get -y install mediainfo

apt-get -y install gparted

apt-get -y install php5-cli

apt-get -y install iptables

apt-get -y install xtightvncviewer

apt-get -y install imagemagick

apt-get -y install dosfstools

apt-get -y install exfat-utils exfat-fuse

apt-get -y install hfsplus hfsprogs hfsutils

apt-get -y install xdotool

apt-get -y install expect expect-dev

If you want to use PiMapper you must install openframeworks: http://forum.openframeworks.cc/t/raspberry-pi-2-setup-guide/18690
and then install and compile PiMapper https://github.com/kr15h/ofxPiMapper, then you have to simulate a fake keyboard to unleash the remote control, see here: 
http://www.fsays.eu/Blogging/Blog/Details/23


Copyright by http://magdesign.ch


Firmware written by: Simon Josi, http://www.yokto.net
Pi-Mapper written by: Krisjanis Rijnieks, https://github.com/kr15h/
Virtual Keyboard written by: Erwin van Dijk, http://www.fsays.eu/
Testmovie by: Manuel Berner, http://towerbus.ch/
Testaudio by: Marcel Bieri, https://facebook.com/casashowband

Idea, support and concept by: Marc-André Gasser, http://magdesign.ch/
Please support this project!
