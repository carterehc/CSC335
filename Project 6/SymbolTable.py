
#SymbolTable
#6.2.3 has table

##Assignment: Project 6; CSC 335, Berea College
# Name: Emily Carter - cartere
# Date: 12 / 06 / 17
#Instructor: Mario Nakazawa


#will have to make address binary
#next available memory address. how to find next available? make

class SymbolTable:
    def __init__(self):
        #R0-R15:0-15
        self.sym_d = {'SP':'0', 'LCL':'1', 'ARG':'2', 'THIS':'3', 'THAT':'4',
                      'R0':'0', 'R1':'1', 'R2':'2', 'R3':'3', 'R4':'4',
                      'R5':'5', 'R6':'6', 'R7':'7', 'R8':'8', 'R9':'9',
                      'R10':'10', 'R11':'11', 'R12':'12', 'R13':'13', 'R14':'14', 'R15':'15',
                      'SCREEN':'16384', 'KBD':'24576'}    #creates new symbol dictionary holding 23 predefined ASM symbols


    def addEntry(self, symbol, address):
        """symbol: a string, the asm symbol
           address: an integer, address associated with the symbol"""
        self.sym_d[symbol] = str(address)    #add new key value pair
        #does not return anything, just alters sym_d

    def has_key(self, symbol):
        """symbol: a string
        returns true if symbol is key in self.sym_d
        returns false if symbol is not key in self.sym_d"""
        return symbol in self.sym_d

    def GetAddress(self, symbol):
        """symbol: a string from the asm instruction
        :return: address, the address associated with the symbol
        """
        if self.has_key(symbol):
            address = self.sym_d.get(symbol)
            return address

