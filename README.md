morse
=====

Convert inputted text to morse code

### Requirements

Needs the python module pyfirmata

### Usage 

See fritzing schematic in morse.fzz for example setup 

Run by typing 'python morse.py' 

The script will attempt to connect to your arduino, if it is not located at the default location (/dev/ttyACM0), enter the full absolution location ie: /dev/ttyACM1, etc. 

Enter your pin number used when prompted.

Type your message and it will be converted to morse as console output and in led flashes / piezo buzzes depending on your setup. 


