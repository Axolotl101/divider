inter = int(input("Input an integer->"))
numb = int(input("How many cycles do you want?>"))
name = input("Filename of the log file:")
fh = open(name, "w+")
numbers = 0
for x in range(numb):
    if (x % inter == 0):
        print(x)
        line=str(x) + "\n"
        fh.write(line)
        numbers = numbers + 1
    else:
        pass
fh.close()
print(numbers, "numbers found!")
