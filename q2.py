string = input("Enter a string, or enter 'stop' or 'STOP' to end the program.")
shortest = string
longest = string
while string != 'stop' and string != 'STOP':
    if len(string) > len(longest):
        longest = string
    if len(string) < len(shortest):
        shortest = string
    string = input("Enter a string, or enter 'stop' or 'STOP' to end the program.")
print(longest, shortest)