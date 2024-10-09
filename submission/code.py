import time
from adafruit_circuitplayground import cp


cp.pixels.auto_write = False
cp.pixels.brightness = 0.3

def set_color(color):
    for i in range(10):
        cp.pixels[i] = color
    cp.pixels.show()
    
while True:
   
    print("Select any color")
    print("Red: Press 1")
    print("Green: Press 2")
    print("Blue: Press 3")
    print("Press 'q' to exit")

    user_input = input("Enter your preference: ")
    

    if user_input.lower() == 'q':
        print("Exiting the program.")
        break


    try:
        choice = int(user_input)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 3, or 'q' to quit.")
        continue

  
    if choice ==1:
        set_color((255,0,0)) 
    elif choice ==2:
        set_color((0, 255, 0)) 
    elif choice == 3:
        set_color((0, 0, 255)) 
    else: 
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    
    time.sleep(0.5)