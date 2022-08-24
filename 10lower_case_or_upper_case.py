#Write a python program to check whether a character is uppercase or lowercase alphabet.
chr=input("Enter the character:- ")
if chr>="a" and chr<="z":
    print(chr,"is lower case")
elif chr>="A" and chr<="Z":
    print(chr,"is upper case")
else:
    print(chr,"is not a alphabet")