# ----codescracker.com----

print("Enter the First String: ")
strOne = input()
print("Enter the Second String: ")
strTwo = input()

lenOne = len(strOne)
lenTwo = len(strTwo)

if lenOne==lenTwo:
    i = 0
    chk = 0
    while i<lenOne:
        if strOne[i] != strTwo[i]:
            chk = 1
            break
        i = i+1
    if chk==0:
        print("\nStrings are Equal")
    else:
        print("\nStrings are Not Equal")
else:
    print("\nStrings are Not Equal")
