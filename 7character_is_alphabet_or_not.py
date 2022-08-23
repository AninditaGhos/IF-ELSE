#Write a python program to check whether a character is an alphabet or not.
chr=input("Enter the character:- ")
if chr>="a" and chr<="z" or chr>="A" and chr<="Z":
    print(chr,"is a character")
else:
    print(chr,"is not a character")