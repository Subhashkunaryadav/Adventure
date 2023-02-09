message="Adventure Game"
print(message.center(100))

name = str(input("Enter Your Name:" + '\n'))
message = 'Your Situation'
print(message)
print(f"\n{name},you are stuck in a forest. Your task is to get out from the forest without dieing.")
print("You are walking through forest and suddenly a wolf comes in your way.\nNow You have two options" +'.\n')
print("1.Run\n2.Climb The Nearest Tree\n3.It was a dream "+'\n')
user = int(input("Choose one option 1 or 2 or 3" + '.\n'))
if user==1:
    print("You Died!!")
elif user==2:
    print("Hurray!!!You Survived!!")
elif user ==3:
    print("It was a dream!")    
else:
    print("Incorrect Input")
