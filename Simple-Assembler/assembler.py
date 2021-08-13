import os
def main():
    # here 0 and 10**6 represents starting point and end point in bytes.
    lines = os.read(0, 10 ** 6).strip().splitlines()
    file=""
    for x in lines:
        line = x.decode('utf-8')  # convert bytes-like object to string
        file+=line
        file+="\n"
    print(file)
if __name__=="__main__":
    main()