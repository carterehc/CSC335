// This file is part of the materials accompanying the book 
// "The Elements of Computing Systems" by Nisan and Schocken, 
// MIT Press. Book site: www.idc.ac.il/tecs
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input. 
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel. When no key is pressed, 
// the screen should be cleared.

    //Assignment: Project 4, CSC 335, Berea College
    //Name: Emily Carter - cartere
    //Date: 10/13/17
    //Instructor: Mario Nakazawa
	
//So we want addresses 16384 (IE @SCREEN) to Screen + len of screen -1, IE 256 * 32 = len. len= 8192
//So screen is 16,384-24,575
	
//len is the length of the screen and decreases by one on every iteration of white xor black. When len reaches 0, break out of loop and go to END

(LOOP)

  //Start of screen
  //check keyboard

@WHITE	
D;JEQ  //if not at end of screen, go back to   


(WHITE)
//start of screen
//set to white (0)


//if at end of screen, go to end

(BLACK)
//start of screen 

(END)
@LOOP	
0;JEQ  //go back to LOOP