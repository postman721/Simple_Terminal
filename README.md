

## Simple terminal

rxvt-unicode Pyqt5 terminal implementation with less than 20 lines of code.

![simple](https://user-images.githubusercontent.com/29865797/71637276-61015980-2c47-11ea-8f18-fbb615124c14.jpg)



		Simple Terminal Copyright (c) 2020 JJ Posti <techtimejourney.net> 
		This program comes with ABSOLUTELY NO WARRANTY; 
		for details see: http://www.gnu.org/copyleft/gpl.html. 
		This is free software, and you are welcome to redistribute it under 
		GPL Version 2, June 1991")


### Dependencies

Requires pyqt5 and python3 installed. Packages vary upon distributions.

Requires rxvt-unicode to be installed. Can also be named as urxvt depending on a distribution.


### Functionality: 

Copy with left-clicking and painting the terminal area to copy. Paste with middle-clicking the mouse.
	 
Most of the settings come from the supplied Xresources file. 
		
By default scrollbar is disabled. See the supplied Xresources file for more.

		
If changes are made or resources otherwise need to be reloaded use: 

		xrdb -load Xresources

It is also recommended to load the Xresources file before running Simple terminal - so that the outlook will be set correctly. 

Executing:

If needed make executable with:
		
		chmod +x simple.py

Then run the terminal:

		python simple.py

___________________________________
Release post is also available at: https://www.techtimejourney.net/simple-terminal-released/

