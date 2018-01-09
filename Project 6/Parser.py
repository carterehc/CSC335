
#parser
#6.2.2 has table
#@ means a instruction
#not @ means c instruction

##Assignment: Project 6; CSC 335, Berea College
# Name: Emily Carter - cartere
# Date: 12 / 06 / 17
#Instructor: Mario Nakazawa

class Parser:
    """Parser encapsulates access to input code.
    Removes white spaces and comments. produces list of lines
    """
    def __init__(self):
        """"""
        self.lines = []    #instantiate parser, an empty list

    def read_instr(self, string):
        """reads one string at a time and, if string is not comment or newline, adds to parser.

        :return: none
        """
        if string[0:2]=='//' or string=='\n' or string[0]=='(':    #don't keep comments or new lines, or labels
            return

        if '//' in string:    #if string has a comment
            string = string.split('//', 1)[0]    #remove the comment
        #if '\n' in string:    #if newline character in string
        string = string.replace('\n','')    #remove newline char
        string = string.replace(' ','')    #remove spaces
        self.lines.append(string)    #add the parsed instruction to lines list.