secret=9
guess_count=0
guess_limit=3

while guess_count < guess_limit:
    guess=int(input("guess the number:"))
    guess_count+=1
    if guess==secret:
        print("You won")
        break

else:
    print("You failed")

print("End of the game")
