from sys import stdin
def main():
    from sys import stdin
    for line in stdin:
        if line == '':  # If empty string is read then stop the loop
            break
        print(line)  # perform some operation(s) on given string
if __name__=="__main__":
    main()