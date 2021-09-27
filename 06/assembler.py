# example: python assembler.py "add/Add.asm"

import sys

class Parser:
    def __init__(self,file_address):
        self.f = open(file_address, "r")
        self.current_command = self.f.readline()

    def hasMoreCommands(self):
        return next(self.f) != None

    def advance(self):
        self.current_command = self.f.readline()

    def commandType(self):
        #what is difference between L and C command?
        if self.current_command[0] == "@":
            return "A_COMMAND"
        elif self.current_command[0] == '(':
            return "L_COMMAND"
        else:
            return "C_COMMAND"

    def symbol(self):
        if self.commandType() == "A_COMMAND":
            return self.current_command[1:]
        elif self.commandType() == "A_COMMAND":
            return [char for char in self.current_command if char not in ['(',')']]
        else:
            return None

    def dest(self):
        if self.commandType() == "C_COMMAND":
            if ";" not in self.current_command:
                output_str = ""
                for char in self.current_command:
                    if char == "=":
                        break
                    else:
                        output_str += char
                return output_str
        return ""

    def comp(self):
        if self.commandType() == "C_COMMAND":
            if "=" in self.current_command:
                output_str = ""
                for char in self.current_command:
                    if char == "=":
                        break
                    else:
                        output_str += char
            else:
                output_str = ""
                for char in self.current_command:
                    if char == "=":
                        break
                    else:
                        output_str += char
            return output_str
        return ""
    
    def jump(self):
        if self.commandType() == "C_COMMAND":
            if ";" in self.current_command():
                output_str = ""
                colon_encountered = False
                for char in self.current_command:
                    if colon_encountered:
                        output_str += char
                    elif char == ";":
                        colon_encountered = True
                return output_str
        return ""

def dest_code(string):
    lookup = {"null":"000",
    "M":"001",
    "D":"010",
    "MD":"011",
    "A":"100",
    "AM":"101",
    "AD":"110",
    "AMD":"111",}
    return lookup[string]

def comp_code(string):
    lookup = {
    "0":"101010",
    "1":"111111",
    "-1":"111010",
    "D":"001100",
    "A":"110000",
    "M":"110000",
    "!D":"001101",
    "!A":"110001",
    "!M":"110001",
    "-D":"001111",
    "-A":"110011",
    "-M":"110011",
    "D+1":"011111",
    "A+1":"110111",
    "M+1":"110111",
    "D-1":"001110",
    "A-1":"110010",
    "M-1":"110010",
    "D+A":"000010",
    "D+M":"000010",
    "D-A":"010011",
    "D-M":"010011",
    "A-D":"000111",
    "M-D":"000111",
    "D&A":"000000",
    "D&M":"000000",
    "D|A":"010101",
    "D|M":"010101",
    }
    return lookup[string]

def jump_code(string):
    lookup = {"null":"000",
    "JGT":"001",
    "JEQ":"010",
    "JGE":"011",
    "JLT":"100",
    "JNE":"101",
    "JLE":"110",
    "JMP":"111",}
    return lookup[string]

def to_binary(string):
    num = int(string)

if __name__ == "__main__":
    file_address = sys.argv[1]
    p = Parser(file_address)
    output_filename = file_address[:file_address.index(".")]
    f = open(f"{output_filename}.HACK", "w")
    while p.hasMoreCommands():
        if p.commandType == "C_COMMAND":
            new_line = "0" + dest_code(p.dest()) + comp_code(p.comp()) + jump_code(p.jump()) 
            f.write(new_line)
        elif:
            p.commandType == "A_COMMAND":
            new_line = "1" + f"{p.current_command:b}"
        p.advance()

    f.close()



