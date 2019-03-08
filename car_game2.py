command = ""
start=0
stop=0

while True:
    command=input("> ").lower()
    if command=="start" and start == 0:
        print("Car started...")
        start=1
        stop=0

    elif command=="start" and start == 1:
        print("Car already started...")
        start=1
        stop=0

    elif command=="stop" and stop == 0:
        print("Car stopped.")
        start=0
        stop=1

    elif command=="stop" and stop == 1:
        print("Car already stopped.")
        start=0
        stop=1

    elif command=="help":
        print("""start - start the car
stop - to stop the car
quit - to quit 
        """)
    elif command=="quit":
        break
    else:
        print("I don`t get it")
