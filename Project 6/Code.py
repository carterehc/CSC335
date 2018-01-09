
#code
#6.2.2 has table
#@ means a instruction
#not @ means c instruction

##Assignment: Project 6; CSC 335, Berea College
# Name: Emily Carter - cartere
# Date: 12 / 06 / 17
#Instructor: Mario Nakazawa

class Code:
    """ translates ASM mnemonic to binary"""
    def __init__(self):

        self.comp_d = comp_d = {'0': '0101010', '1': '0111111', '-1': '0111010', 'D': '0001100', 'A': '0110000', '!D': '0001101',
              '!A': '0110001',
              '-D': '0001111', '-A': '0110011', 'D+1': '0011111', 'A+1': '0110111', 'D-1': '0001110', 'A-1': '0110010',
              'D+A': '0000010',
              'D-A': '0010011', 'A-D': '0000111', 'D&A': '0000000', 'D|A': '0010101',
              'M': '1110000', '!M': '1110001', '-M': '1110011',
              'M+1': '1110111', 'M-1': '1110010', 'D+M': '1000010', 'D-M': '1010011', 'M-D': '1000111',
              'D&M': '1000000', 'D|M': '1010101'}  # a comp dictionary. has 28 key-val pairs. Last ten a=1

        self.jump_d = {'JGT':'001', 'JEQ':'010', 'JGE':'011', 'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}    #a jump dictionary. Seven key-val pairs

        self.dest_d = {'M': '001', 'D': '010', 'MD': '011', 'A': '100', 'AM': '101', 'AD': '110',
              'AMD': '111'}  # seven key-val pairs for destination bits

    def get_jump(self, j_key):
        """finds the binary equivalent for the jump j_key
        param: j_key: a string telling the ASM jump code
        :return: j_c: a three character string with the binary jump code for j_key (jjj)"""
        j_c = self.jump_d.get(j_key)    #find jump binary in jump dictionary
        return j_c    #return the jump command in binary

    def get_dest(self, d_key):
        """
        finds the binary equivalent for the destination d_key
        :param d_key: a string telling the destination
        :return: d_c: a three character string holding the binary equivalent for d_key (ddd)
        """
        d_c = self.dest_d.get(d_key)    #assign destination binary to d_c
        return d_c

    def get_comp(self, c_key):
        """finds the binary equivalent for the computation c_key
        :param: c_key: a string with the ASM computation code
        :return: c_c: a seven character string holding the binary equivalent for c_key (acccccc)"""
        c_c = self.comp_d.get(c_key)
        return c_c