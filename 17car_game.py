user_command = ""
started = False
while True:
    user_command = input(">").lower()
    if started and user_command == 'start':
        print("The car is already started")
    elif not started and user_command == 'stop':
        print("The car is already stopped")
    elif user_command == 'start':
        print("Started the car Ready to go!")
        started = True
    elif user_command == 'help':
        print("Start - to start the car")
        print("Stop - to stop the car")
        print("Quit - to Quit the game")
    elif user_command == 'stop':
        print("Car stopped!")
        started = False
    elif user_command == 'quit':
        break
    else:
        print("I don't Undestant that...")
