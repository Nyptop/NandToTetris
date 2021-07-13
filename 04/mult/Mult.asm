@R0
D=M
@a
M=D // a = R0
@R1
D=M
@b
M=D // b = R1
@total
M=0

(LOOP)
@b
D = M
@STOP
D;JEQ

@b
M=M-1
@a
D=M
@total
M=D+M

@LOOP
0;JMP

(STOP)
@total
D=M
@R2
M=D

(END)
@END
0;JMP






