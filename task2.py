
# Create a program that takes the input from the user
user_input = input()
# The input from the user should be saved onto a text file
with open('user.txt', 'w') as file:
    file.write(user_input)
user_confirmation = input("Do you want to read the file ? Yes/No: ")

# An option for the user to read or get data/info from the text file
if user_confirmation == 'Yes' :
   with open('user.txt', 'r') as file:
    contents = file.read()
    print(contents)
else :
    print("Your File have been saved!")



