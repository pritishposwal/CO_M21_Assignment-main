import os
opcodes={'00000': 'add', '00001': 'sub', '00010': 'mov', '00100': 'ld', '00101': 'st', '00110': 'mul', '00111': 'div', '01000': 'rs',
         '01001': 'ls', '01010': 'xor', '01011': 'or', '01100': 'and', '01101': 'not', '01110': 'cmp', '01111': 'jmp', '10000': 'jlt',
         '10001': 'jgt', '10010': 'je', '10011': 'hlt'}
registers={"000":0,"001":0,"010":1,"011":0,"100":0,"101":0,"110":0,"111":0}
R0=0
R1=0
R2=0
R3=0
R4=0
R5=0
R6=0
FLAG=0
overflow=0
lessthan=0
greaterthan=0
equal=0
pc=0
def decimalToBinary(n):
    return bin(n).replace("0b","")
def flagset(overflow,lessthan,greaterthan,equal):
    global FLAG
    FLAG="0"*12
    FLAG+=str(overflow)+str(lessthan)+str(greaterthan)+str(equal)
def bincomp(length,num):
    binpc1 = decimalToBinary(num)
    tempval=length-len(binpc1)
    if (tempval!=0):
        final = (length - len(binpc1)) * "0"
        final += binpc1
    else:
        final=binpc1
    return final
def typea(operation, reg1, reg2, reg3):
    if (operation == "add"):
        registers[reg1]=registers[reg2]+registers[reg3]
        if (registers[reg1] > 65535):
            global overflow
            overflow=1
            flagset(overflow,lessthan,greaterthan,equal)
            temp=str(decimalToBinary(registers[reg1]))
            templ=len(temp)
            finalstore=temp[templ-16:]
            registers[reg1]=int(finalstore,2)
        global pc
        fcounter = bincomp(8, pc)
        r0bin = bincomp(16, registers["000"])
        r1bin = bincomp(16, registers["001"])
        r2bin = bincomp(16, registers["010"])
        r3bin = bincomp(16, registers["011"])
        r4bin = bincomp(16, registers["100"])
        r5bin = bincomp(16, registers["101"])
        r6bin = bincomp(16, registers["110"])
        r7bin = bincomp(16, registers["111"])
        print(fcounter, r0bin, r1bin, r2bin, r3bin, r4bin, r5bin, r6bin, r7bin)
def main():
    lines = os.read(0, 10 ** 6).strip().splitlines()
    file = ""
    for x in lines:
        line = x.decode('utf-8')  # convert bytes-like object to string
        file += line
        file += "\n"
    flag = 1
    counter = 1
    lt = file.split("\n")
    global pc
    pc=0
    while(True):
        instruction=lt[pc]
        temp=instruction[0:5]
        if(temp=="01111" or temp=="10000" or temp=="10001" or temp=="10010"):
            pass
        else:
            if(opcodes[temp]=="add" or opcodes[temp]=="mul" or opcodes[temp]=="sub" or opcodes[temp]=="xor" or opcodes[temp]=="or" or opcodes[temp]=="and"):
                typea(opcodes[temp],instruction[7:10],instruction[10:13],instruction[13:])
                break
if __name__=="__main__":
    main()