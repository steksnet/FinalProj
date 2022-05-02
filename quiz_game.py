print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0
totalQestions=10

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What is considered to be the heart of the computer? ")
if answer.lower() == "the motherboard" or answer.lower() == "motherboard":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The image on a monitor is made up of? ")
if answer.lower() == "pixels" or answer.lower() == "pixel":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("How many megabyties makes up a gigabyte? ")
if answer.lower() == "1000" or answer.lower() == "one thousand":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does LAN stand for? ")
if answer.lower() == "local area network" :
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The first computer was programmed using what language? ")
if answer.lower() == "machine language":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("What does ISP stand for? ")
if answer.lower() == "internet service provider":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The number system that only uses two digits, 0 and 1, is called the ____ number system. ")
if answer.lower() == "binary":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

answer = input("The _______ refers to the physical components of a computer. ")
if answer.lower() == "hardware" or answer.lower() == "motherboard":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")


print("Thank you for playing, you got " + str(score) + " questions correct!")
percent = (score/totalQestions) * 100
print("You got " + str(int(percent)) + "%.")

if percent >= 60:
    print ("Good Job! You have passed the quiz!")
else:
    print ("Sorry, better luck next time")