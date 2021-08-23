import os
opcodes={'00000': 'add', '00001': 'sub', '00010': 'mov', '00100': 'ld', '00101': 'st', '00110': 'mul', '00111': 'div', '01000': 'rs',
         '01001': 'ls', '01010': 'xor', '01011': 'or', '01100': 'and', '01101': 'not', '01110': 'cmp', '01111': 'jmp', '10000': 'jlt',
         '10001': 'jgt', '10010': 'je', '10011': 'hlt'}
registers={"000":32,"001":0,"010":5,"011":2,"100":0,"101":0,"110":0,"111":0}
variable={}
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
def comp1(bit_s):

    inverse_s = ''

    for i in bit_s:

        if i == '0':
            inverse_s += '1'

        else:
            inverse_s += '0'

    return inverse_s
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
def printreg():
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
def typea(operation, reg1, reg2, reg3):
    global overflow
    if (operation == "add"):
        registers[reg1]=registers[reg2]+registers[reg3]
        if (registers[reg1] > 65535):
            overflow=1
            flagset(overflow,lessthan,greaterthan,equal)
            temp=str(decimalToBinary(registers[reg1]))
            templ=len(temp)
            finalstore=temp[templ-16:]
            registers[reg1]=int(finalstore,2)
        printreg()
    elif(operation=="mul"):
        registers[reg1] = registers[reg2] * registers[reg3]
        if (registers[reg1] > 65535):
            overflow=1
            flagset(overflow,lessthan,greaterthan,equal)
            temp=str(decimalToBinary(registers[reg1]))
            templ=len(temp)
            finalstore=temp[templ-16:]
            registers[reg1]=int(finalstore,2)
        printreg()
    elif(operation=="sub"):
        registers[reg1] = registers[reg2] - registers[reg3]
        if (registers[reg1] < 0):
            overflow = 1
            flagset(overflow, lessthan, greaterthan, equal)
            registers[reg1] = 0
        printreg()
    elif(operation=="xor"):
        registers[reg1]= registers[reg2]^registers[reg3]
        printreg()
    elif(operation=="or"):
        registers[reg1]=registers[reg2] | registers[reg3]
        printreg()
    elif(operation=="and"):
        registers[reg1]=registers[reg2]&registers[reg3]
        printreg()
def typeb(operation , reg1, value):
     label=operation
     if(label=="mov" ):
         registers[reg1]=int(value,2)
         printreg()
     elif(label=="ls"):
         registers[reg1]=registers[reg1]<<int(value,2)
         printreg()
     elif(label=="rs"):
         registers[reg1]=registers[reg1]>>int(value,2)
         printreg()
def typec(operation, reg1, reg2):
    if(operation=="div"):

        registers["000"]=registers[reg1]//registers[reg2]
        registers["001"]=registers[reg1]%registers[reg2]
        printreg()

    elif(operation=="mov"):
        registers[reg1]=registers[reg2]
        printreg()
    elif(operation=="not"):
        registers[reg1]=int(comp1(bincomp(16,registers[reg2])),2)
        printreg()
    elif(operation=="cmp"):
        rr1=registers[reg1]
        rr2 = registers[reg2]
        global greaterthan, lessthan, equal
        if(rr1>rr2):
            greaterthan=1
            registers["111"]=2
        elif(rr1<rr2):
            lessthan=1
            registers["111"]=4
        elif(rr1==rr2):
            equal=1
            registers["111"]=1
        printreg()

def typed(operation ,reg, memadd):
    if(operation=="ld"):
        if(memadd not in variable.keys()):
            variable[memadd]=0
        registers[reg]=variable[memadd]
        printreg()


    elif(operation=="st"):
        if(memadd not in variable.keys()):
            variable[memadd]=0
        variable[memadd]=registers[reg]
        printreg()
def typee(operation, memadd):
    global pc ,greaterthan,lessthan,equal

    if(operation=="jgt"):
        if(greaterthan==1):
            pc=int(memadd,2)
            greaterthan=0


    elif(operation=="jmp"):
        pc=int(memadd,2)
    elif(operation=="jlt"):
        if(lessthan==1):
            pc=int(memadd,2)
            lessthan=0
    elif(operation== "je"):
        if(equal==1):
            pc=int(memadd,2)
            equal=0
    printreg()
def hlt(lt):
    for i in range(len(lt)):
        print(lt[i])
    for i in variable.keys():
        print(variable[i])
    rem=256-len(lt)-len(variable)
    for i in range(rem):
        print("0"*16)




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
            elif(temp=="00010" or opcodes[temp]=="ls" or opcodes[temp]=="rs"):
                typeb(opcodes[temp],instruction[5:8] ,instruction[8:])
            elif(opcodes[temp] =="div" or opcodes[temp]=="mov" or opcodes[temp]=="not" or opcodes[temp]=="cmp"):
                typec(opcodes[temp],instruction[10:13], instruction[13:])
            elif(opcodes[temp]=="ld" or opcodes[temp]=="st"):
                typed(opcodes[temp],instruction[5:8],instruction[8:])
            elif(opcodes[temp]=="jlt" or opcodes[temp]=="jmp" or opcodes[temp]=="je" or opcodes[temp]=="jgt"):
                typee(opcodes[temp], instruction[8:])
            break
        pc+=1

if __name__=="__main__":
    main()
