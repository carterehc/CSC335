
#parser
#6.2.2 has table
#@ means a instruction
#not @ means c instruction

##Assignment: Project 6; CSC 335, Berea College
# Name: Emily Carter - cartere
# Date: 12 / 06 / 17
#Instructor: Mario Nakazawa

from Parser import Parser
from Code import Code
from SymbolTable import SymbolTable

def mk_bin(num):
    """"converts a decimal number to binary
    num: a string of a number
    :return: bnum, binary translation of num"""
    num = int(num)    #convert to integer
    bnum = format(num, 'b').zfill(16)    #put number in binary, pad with 0s
    return bnum

def build_sym(symbol, table):
    """symbol: a string of either digits or symbols
    table: a SymbolTable object
    :return:
    """
    if symbol.isdigit():    #if symbol is a digit
        return table   #do nothing
    else:    #if is variable/symbol
        if table.has_key(symbol) is False:    #not in table
            i =16
            while i in table.sym_d.values() and i < 16384:    #while address is already used
                i=i+1    #increment i
            table.addEntry(symbol, i)    #add symbol with address
        return table

def is_a(a_instr, table):
    """runs if is a instruction, an @ is found in the string
    a_instr: assembly language a instruction
    table: symbolTable in case @ instruction is symbol
    puts the number into address A
    ##but what if is symbol, not number
    :return: out_instr, a 16 character binary a instruction"""
    if a_instr.isdigit():    #is digit A instruction
        out_instr=mk_bin(a_instr)

    else:    #is symbol a instruction
        add = table.GetAddress(a_instr)    #get address of symbol
        out_instr=mk_bin(add)    #convert address to binary

    return out_instr    #return translated a instruction

def is_c(c_instr, code):
    """runs if is c instruction, no @ found in string. finds the right binary equivalents
    c_instr: the assembly language instruction
    code: a Code object holding the jump, comp, and destination dictionaries
    :return: out_instr, a 16 character binary instruction
    """
    out_instr='111'   #start output instruction. 111 acccccc ddd jjj

    #to get dest, split at =
    if '=' in c_instr:    #has destination
        comp_dest = c_instr.split('=',1)   #split at =
        dest_key = comp_dest.pop(0)    #get destination command. put before = in dest_key
        c_instr = comp_dest.pop(0)   #get rest of c instruction. put after = in c_instr
        dest = code.get_dest(dest_key)    #assign destination binary to dest
    else:    #no destination
        #c instruction is unchanged
        dest = '000'    #destination is null

    #to get jump, split at ';'
    if ';' in c_instr:
        split_line = c_instr.split(';', 1)    #split at jump command
        # send jump command to function and concatenate is_jump output to out instruction
        jump = code.get_jump(split_line[1])    #get jump command
        c_instr = split_line[0]    #line without jump command
    else:    #jump is null
        #c instruction is unchanged
        jump = '000'

    comp = code.get_comp(c_instr)    #get a cccc cc bits from computation dictionary
    return out_instr +comp+dest+jump    #concatenate parts of binary equiv and return

def main():
    asm_file = raw_input('enter file name ')    #get file
    myfile = open(asm_file, 'r')    #open asm file
    asm_instr = myfile.readlines()    #returns list of strings, each one a line

    hack_instr = open(asm_file[0:len(asm_file)-3] + 'hack', 'w')    #open new file with hack ext and same name as asm. to store binary instructions in.

    parse = Parser()    #instantiate new parser object

    symbols = SymbolTable()    #instantiate new SymbolTable object

    code = Code()    #instantiate new Code object. has binary equivalents for ASM commands.

    #actually add lines to parser
    for line in asm_instr:    #for each asm line
        parse.read_instr(line)    #build parsed list

    #build SymbolTable - first run through
    for line in parse.lines:    #for each parsed line
        if '@' in line:    #if is a instruction
            symbols = build_sym(line[1:len(line)], symbols)    #send symbol and table

    #conversion run through
    for line in parse.lines:    #for each parsed line
        if '@' in line:  # is A instruction
            line = line[1:len(line)]  # remove @
            out_line = is_a(line, symbols)    #translated a instruction

        else:  # is C instruction
            out_line = is_c(line, code)

        hack_instr.write(out_line+'\n')    #store the translated instruction in the hack file.

    return hack_instr    #return translated hack file

if __name__ == "__main__":
    main()