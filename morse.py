### Arduino  Morse Code Generator
### Enter a word, and get morse code output in LED and/or buzzer



#Copyright (c) 2014 Joshua Kouri

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


import pyfirmata


### DEFINE MORSE CODE ALPHABET ###
morse = {'a':['.','-'],
	 'b':['-','.','.','.'],
	 'c':['-','.','-','.'],
	 'd':['-','.','.'],
	 'e':['.'],
	 'f':['.','.','-','.'],
	 'g':['-','-','.'],
	 'h':['.','.','.','.'],
	 'i':['.','.'],
	 'j':['.','-','-','-'],
	 'k':['-','.','-'],
	 'l':['.','-','.','.'],
	 'm':['-','-'],
	 'n':['-','.'],
	 'o':['-','-','-'],
	 'p':['.','-','-','.'],
	 'q':['-','-','.','-'],
	 'r':['.','-','.'],
	 's':['.','-','-','-'],
	 't':['-','.','-'],
	 'u':['.','-','.','.'],
	 'v':['-','-'],
	 'w':['-','.'],
	 'x':['-','-','-'],
	 'y':['.','-','-','.'],
	 'z':['-','-','.','-'],
	 ' ':' '}


### CONNECT TO ARDUINO ###
try:
	PORT = '/dev/ttyACM0'
	board = pyfirmata.Arduino(PORT)
except:
	PORT = raw_input("Enter full Arduino device location (ie: 'dev/ttyUSB0' etc): ")
	board = pyfirmata.Arduino(PORT)

### SET PIN NUMBER ###
pin = int(raw_input('Enter Arduino digital pin number used: '))


def program():


### DELAY FACTORS ###
  delay = 0.15						# Length of time LED between inter elemental lighting (dits/dahs in a single letter)
  delay_factor = 1					# Speed up or slow down entire program by set percentage (Default: 1)
  delay_intraletter = delay * delay_factor * 3		# Length of time between letters (standard morse = 3x inter element delay)
  delay_interword = delay * delay_factor * 7		# Length of time between words (standard morse = 7x inter element delay)
  delay_dit = delay * delay_factor			# Length of illumination/buzz for dot/dit  (.)
  delay_dah = delay_intraletter	 			# Lenght of illumination/buzz for dash/dah (-)


### SELECT WORD ###
  user_list = [] 									# Blank
  user_input = raw_input("\nEnter word to convert to morse code: ").lower()		# Take user input, convert to lowercase


### CONVERT USER INPUT TO MORSE CODE ###
  for x in user_input:
    user_list.extend(morse.get(x))
  print user_list
  print '\n Creating morse message now...'
  user_list = ''.join(user_list)


### 'TRANSMIT' MORSE CODE ### 
  for l in user_list:
    
    if l == '.':
      board.pass_time(delay_intraletter)
      board.digital[pin].write(1)
      print 'TRANSMITTING: .'
      board.pass_time(delay_dit)
      board.digital[pin].write(0)
    
    elif l == '-':
      board.pass_time(delay_intraletter)
      board.digital[pin].write(1)
      print 'TRANSMITTING: -'
      board.pass_time(delay_dah)
      board.digital[pin].write(0)
      
    elif l == ' ':
      board.pass_time(delay_interword)
      print 'NEW WORD'	

    else:
	pass
      
   
   
program()
  
