#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    total = len(sys.argv)
    sum = 0
    if total <= 1:
        print("0")
    else:
        for i in range(1, total):
            sum += int(sys.argv[i])
        print("{:d}".format(sum))
