input_s = input("Please enter a string: ")
print("input:", input_s)
reverse_input = ""

for i in input_s:
    reverse_input = i + reverse_input

# for i in range(len(input_s)-1, -1, -1):
#     reverse_input += input_s[i]

if input_s.replace(" ", "") == reverse_input.replace(" ", ""):
    print('output:', input_s, 'is a palindrome!')
else:
    print('output:', input_s, 'is NOT a palindrome!')