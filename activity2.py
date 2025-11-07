string = input("Please enter your own string:")
string2 = ('')
for i in string:
    string2 = i + string2
    print("\nThe Original String is:", string)
    print("The Reversed String is:", string2)