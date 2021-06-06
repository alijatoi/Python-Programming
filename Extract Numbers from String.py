print("Enter the String: ")
text = input()
textLen = len(text)
nums = []
for i in range(textLen):
  if text[i]>='0' and text[i]<='9':
    nums.append(text[i])
print("\nNumbers List in String:")
print(nums)
