# example: python assembler.py "add/Add.asm"

import sys

class Parser:
    def __init__(self,file_address):
        self.f = open(file_address, "r")
        self.current_command = self.f.readline()

    def hasMoreCommands(self):
        return self.current_command != ""

    def advance(self):
        self.current_command = self.f.readline()

    def commandType(self):
        #what is difference between L and C command?
        if self.current_command[0] == "@":
            return "A_COMMAND"
        elif ';' in self.current_command or '=' in self.current_command and '//' not in self.current_command:
            return "C_COMMAND"
        else:
            return "L_COMMAND"

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
                start_index = 0
                for char in self.current_command:
                    if char != "=":
                        start_index += 1
                    else:
                        output_str = self.current_command[start_index+1:-1]
                        break
            else:
                output_str = ""
                for char in self.current_command:
                    if char == ";":
                        break
                    else:
                        output_str += char
            return output_str
        return ""
    
    def jump(self):
        if self.commandType() == "C_COMMAND":
            if ";" in self.current_command:
                output_str = ""
                colon_encountered = False
                for char in self.current_command:
                    if colon_encountered:
                        output_str += char
                    elif char == ";":
                        colon_encountered = True
                return output_str[:-1]
        return ""

def dest_code(string):
    lookup = {
    "":"000",
    "null":"000",
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
        '0': '0101010',
        '1': '0111111',
        '-1': '0111010',
        'D': '0001100',
        'A': '0110000',
        '!D': '0001101',
        '!A': '0110001',
        '-D': '0001111',
        '-A': '0110011',
        'D+1': '0011111',
        'A+1': '0110111',
        'D-1': '0001110',
        'A-1': '0110010',
        'D+A': '0000010',
        'D-A': '0010011',
        'A-D': '0000111',
        'D&A': '0000000',
        'D|A': '0010101',
        'M': '1110000',
        '!M': '1110001',
        '-M': '1110011',
        'M+1': '1110111',
        'M-1': '1110010',
        'D+M': '1000010',
        'D-M': '1010011',
        'M-D': '1000111',
        'D&M': '1000000',
        'D|M': '1010101'
    }
    return lookup[string]

def jump_code(string):
    lookup = {
    "":"000",
    "null":"000",
    'JGT': '001',
    'JEQ': '010',
    'JGE': '011',
    'JLT': '100',
    'JNE': '101',
    'JLE': '110',
    'JMP': '111'}
    return lookup[string]

def to_binary(string):
    num = f"{int(string[1:]):b}"
    return num

if __name__ == "__main__":
    file_address = sys.argv[1]
    p = Parser(file_address)
    output_filename = file_address[:file_address.index(".")]
    f = open(f"{output_filename}.HACK", "w")
    counter = 0
    while p.hasMoreCommands():
        counter += 1
        print(counter)
        print(p.current_command)
        if p.commandType() == "C_COMMAND":
            print(p.dest())
            print(p.comp())
            print(p.jump())
            new_line = "111" + comp_code(p.comp()) +dest_code(p.dest()) + jump_code(p.jump()) +"\n"
        elif p.commandType() == "A_COMMAND":
            new_line = f"{to_binary(p.current_command)}" +"\n"
            while len(new_line)<16:
                new_line = "0"+new_line
            new_line = "0"+new_line #adding the very first zero at the start
        else:
            new_line = ""
        f.writelines(new_line)
        p.advance()

    f.close()



