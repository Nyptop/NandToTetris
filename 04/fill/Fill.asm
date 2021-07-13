// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

// problems:

// Why is it going straight to BLACK at the start when I haven't pressed a key

// Why do I get the error at line 31: Desination is M but A = 24608 is an illegal memory address


@SCREEN
D=A
@addr
M=D

//Setting Colour
@KBD
D=M

@BLACK
D;JEQ

@WHITE
D;JNE

// ---------------

(BLACK)
@KBD
D=A
@addr
D=D-M
@END
D;JLE


@addr
A=M
M=-1

@1
D=A
@addr
M=D+M

@BLACK
D;JMP

// -------------

(WHITE)
@KBD
D=A
@addr
D=D-M
@END
D;JLE

@addr
A=M
M=0

@1
D=A
@addr
M=D+M

@WHITE
D;JMP

(END)
@SCREEN
D=A
@addr
M=D

@KBD
D=M

@BLACK
D;JEQ

@WHITE
D;JNE
