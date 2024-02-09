import random
a = input("Hello! What is your name?\n")
b = random.randint(1, 20)
c = -1
d = 0
print("Well, " + a + ", I am thinking of a number between 1 and 20.")
while(c != b):
    c = int(input("Take a guess.\n"))

    if(c < b):
        print("Your guess is too low.")
    elif(c > b):
        print("Your guess is too high.")
    d += 1
print("Good job, "+ a + "! You guessed my number in " + str(d) + " guesses!")