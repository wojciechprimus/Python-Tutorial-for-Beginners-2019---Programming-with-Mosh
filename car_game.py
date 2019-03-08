print("""start - to start the car
stop - to stop the car
quit - to exit the game""")

while True:
    inp=input("What is yours input: ")
    if inp=="start":
        print("Start the car...We can go")
    elif inp=="stop":
        print("Stopped the car")
    elif inp=="quit":
        break
    else:
        print("I don`t understand that...")

print("End of the game")
