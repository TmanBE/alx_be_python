#Ask user for pattern
pattern = int(input("Enter the size of the pattern: "))

#Drawing the pattern

row = 0
count = 0

while count < pattern:
        for  row in range(pattern):
            print("*", end="")
        print()
        count += 1
        
