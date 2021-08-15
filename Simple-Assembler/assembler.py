import os
opcodes={"add":"00000","sub":"00001","mov":"00010","ld":"00100","st":"00101","mul":"00110","div":"00111",
             "rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110","jmp":"01111",
             "jlt":"10000","jgt":"10001","je":"10010","hlt":"10011"}
registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
labels={}  #dict to store mylabel
ldst={} #stores  variable and mem_address in fromt of that
def errordetection(temp, count, totline):  #temp-->single line instr, count-->no of instr, totline-->last instr of file
        lst=temp.split()
        mlabel=lst[0]
        templ=len(mlabel)
        if(mlabel[:templ-1] in labels.keys()):
            lst.remove(lst[0])  #removing label name
        if(len(lst)==1):
            if(lst[0]=="hlt" and count==totline):  #making sure hlt is last
                return 1
            else:
                print("General syntax error",end=" ")
                return 0
        elif(len(lst)==2):
            label=lst[0]
            value=lst[1]    # making sure var is alphanumeric or _
            if(label=="var" or label=="jgt" or label=="je" or label=="jmp" or label=="jlt"):
                if(label=="var"):
                    for i in value:
                        if(i in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890_"):
                            continue
                        else:
                            print("variable name incorrect",end=" ")
                            return 0
                elif(label=="jgt" or label=="je" or label=="jlt" or label =="jmp"):
                    if(value in labels.keys()):
                        return 1
                    else:
                        print("incorrect label",end=" ")
                        print(labels)
                        return 0
            else:
                print("Typo in instruction name ",end=" ")
                return 0
        elif(len(lst)==3):
            label=lst[0]
            ind1=lst[1]
            ind2=lst[2]
            if(label=="mov" or label=="div" or label=="ld" or label=="st" or label=="rs" or label=="ls" or label=="not" or label=="cmp"):
                if(ind1 in registers.keys()):
                   if(label=="mov"):
                       if(ind2 in registers.keys() or ind2[0]=="$"and 0<=int(ind2[1:])<=255):
                           return 1
                       else:
                           print("Invalid Syntax for mov",end=" ")
                           return 0
                   elif(label=="div" or label=="not" or label=="cmp" ):
                       if(ind2 in registers.keys()):
                           return 1
                       else :
                           print("Invalid second registers",end=" ")
                           return 0
                   elif(label=="rs" or label=="ls"):
                       if ( ind2[0] == "$" and  0 <= int(ind2[1:]) <= 255):
                           return 1
                       else:
                           print("Invalid value",end=" ")
                   elif(label=="ld" or label=="st"):
                       if(ind2 in ldst.keys()): #checking if mem_add is correct binary
                           return 1
                       else :
                           print("Invalid variable",end=" ")
                           return 0
                else:
                   print("invalid registers",end=" ")
            else:
                print("Typo in instruction name ", end=" ")
        elif(len(lst)==4):
            label =lst[0]
            r1=lst[1]
            r2=lst[2]
            r3=lst[3]
            if(label=="add" or label =="sub" or label =="mul" or label =="xor"or  label=="or" or label =="and" ):
                if( r1 in registers and r2 in registers and r3 in registers  ):
                    return 1
                else :
                    print("Inavlid register",end=" ")
            else :
                print("Typo in instruction name ", end=" ")
        else:
            print("general syntax error",end=" ")
def decimalToBinary(n):
    return bin(n).replace("0b","")
def process(file):
    lines=file.split("\n")
    lngth=len(lines)-len(ldst)-1
    cnt=1
    for inst in lines:
        stm =inst.split()
        templ=len(stm[0])
        if(stm[0][:templ-1] in labels):
            stm.remove(stm[0])
        if(len(stm)==1):
            print(opcodes["hlt"]+"00000000000")
            break
        elif(len(stm)==2):
            strng=""
            if(stm[0]!="var"):
                strng+=opcodes[stm[0]]+"000"
                Str2=str(decimalToBinary(int(labels[stm[1]]-2)))
                temp = len(Str2)
                Str2 = ("0" * (8 - temp)) + Str2
                strng+=Str2
                print(strng)
        elif(len(stm)==3):
            if(stm[0]=="mov"):
                if(stm[2] in registers):
                    strng="00011"
                    strng+="00000"
                    strng+=registers[stm[1]]+registers[stm[2]]
                    print(strng)
                else:
                    strng=opcodes[stm[0]]
                    strng+=registers[stm[1]]
                    Str2=decimalToBinary(int(stm[2][1:]))
                    temp=len(Str2)
                    Str2=("0"*(8-temp))+Str2
                    strng+=Str2
                    print(strng)
            elif(stm[0]=="div" or stm[0]=="cmp" or stm[0]=="not"):
                strng=""
                strng+=opcodes[stm[0]]
                strng+="00000"
                strng+=registers[stm[1]]+registers[stm[2]]
                print(strng)
            elif(stm[0]=="ld" or stm[0]=="st"):
                strng=""
                strng+=opcodes[stm[0]]
                strng+=registers[stm[1]]
                Str2=str(decimalToBinary(lngth+int(ldst[stm[2]]-1)))
                temp = len(Str2)
                Str2 = ("0" * (8 - temp)) + Str2
                strng+=Str2
                print(strng)
            elif(stm[0]=="rs" or stm[0]=="ls"):
                strng=""
                strng+=opcodes[stm[0]]
                strng+=registers[stm[1]]
                Str2=str(decimalToBinary(int(stm[2][1:])))
                temp = len(Str2)
                Str2 = ("0" * (8 - temp)) + Str2
                strng += Str2
                print(strng)
        elif(len(stm)==4):
            strng=""
            strng+=opcodes[stm[0]]
            strng+="00"
            strng+=registers[stm[1]]+registers[stm[2]]+registers[stm[3]]
            print(strng)
        cnt+=1
        if(cnt==len(lines)):
            break
def check(file):
    countr=1
    for temp in file.split("\n"):
        temp_lable= temp.split()
        if(len(temp_lable)>=1 and temp_lable[0][-1]==":"):  #making sure that label is followed by :
            tempstore = temp_lable[0]
            templength = len(tempstore)
            labels[temp_lable[0][0:templength-1]]=countr
        countr+=1
def vardict(file): #dictionary for declared variables
    countr = 1
    for temp in file.split("\n"):
        temp_lable = temp.split()
        if (len(temp_lable)>=2 and temp_lable[0] == "var"):
            ldst[temp_lable[1]] = countr
        countr += 1
def main():
    lines = os.read(0, 10 ** 6).strip().splitlines()
    file=""
    for x in lines:
        line = x.decode('utf-8')  # convert bytes-like object to string
        file+=line
        file+="\n"
    #print(file)
    flag=1
    counter=1
    lt=file.split("\n")
    vardict(file)
    check(file)
    for temp in lt:
        flag=errordetection(temp, counter,len(lt)-1)
        if(flag==0):
            print("and line number is",counter)
            break
        counter+=1
        if (counter == len(lt)):
            break
    if(flag==1):
        process(file)
if __name__=="__main__":
    main()