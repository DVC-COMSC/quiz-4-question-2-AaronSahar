longest = ''
string = input("Enter a string, or enter 'stop' or 'STOP' to end the program.")
while string != 'stop' and string != 'STOP':
    if len(string) > len(longest):
        longest = string
    string = input("Enter a string, or enter 'stop' or 'STOP' to end the program.")
print(longest)