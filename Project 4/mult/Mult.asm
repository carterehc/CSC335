// This file is part of the materials accompanying the book 
// "The Elements of Computing Systems" by Nisan and Schocken, 
// MIT Press. Book site: www.idc.ac.il/tecs
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[3], respectively.)

    //Assignment: Project 4, CSC 335, Berea College
    //Name: Emily Carter - cartere
    //Date: 10/13/17
    //Instructor: Mario Nakazawa

    @product  //@ refers to some mem. location, which we will call product
//What if R0 or R1 is 0? We need to start at 0
    M=0  //product holds R1, since we put R1 in M, and M refers to the value in A, IE, the register we are using, product

    @R1  //grab R1
    D=M  //D is R1
    @decrementer
    M=D

(LOOP)  //I think can also be called beginWhile:
    @decrementer
    D=M
    @END
    D;JEQ
  
    @R0  //grab multiplier
    D=M
    @product  //grab product
    M=M+D  //add R1 to product
    //got this far, R0>0
    @decrementer  //grab decrementer
    M=M-1

    //I think can start over now
    @LOOP
    0;JMP
(END)  //I think can also be called endWhile:
    @product
    D=M  //D holds product

    @R2  //access R2
    M=D  //store product in R2