import os
opcodes={"add":"00000","sub":"00001","movimm":"00010","movreg":"00011","ld":"00100","st":"00101","mul":"00110","div":"00111",
             "rs":"01000","ls":"01001","xor":"01010","or":"01011","and":"01100","not":"01101","cmp":"01110","jmp":"01111",
             "jlt":"10000","jgt":"10001","je":"10010","hlt":"10011"}
registers={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110","FLAGS":"111"}
def errordetection(temp):
        lst=temp.split()
        if(len(lst)==1):
            if(lst[0]=="hlt"):
                return 1
            else:
                print("General syntax error")
                return 0
        elif(len(lst)==2):
            pass
        elif(len(lst)==3):
            pass
        elif(len(lst)==4):
            pass
        else:
            print("general syntax error")
def process():
    pass
def main():
    lines = os.read(0, 10 ** 6).strip().splitlines()
    file=""
    for x in lines:
        line = x.decode('utf-8')  # convert bytes-like object to string
        file+=line
        file+="\n"
    print(file)
    flag=1
    for temp in file.split("\n"):
        flag=errordetection(temp)
        if(flag==0):
            break
    if(flag==1):
        process(file)
if __name__=="__main__":
    main()