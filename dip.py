import time, busio, digitalio, board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import KeyPad


#Display Functionality
lcd_columns = 16
lcd_rows = 2
lcd_address = 0x27
i2c = busio.I2C(scl=board.GP1, sda=board.GP0)
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

AMEN=False
BMEN=False
CMEN=False
DMEN=False

def A_menu():
    AMEN=True
    BMEN=False
    CMEN=False
    DMEN=False
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Events:")
    lcd.set_cursor_pos(15,0)
    lcd.print("A")
def B_menu():
    AMEN=False
    BMEN=False
    CMEN=True
    DMEN=False
def C_menu():
    AMEN=False
    BMEN=False
    CMEN=True
    DMEN=False
def D_menu():
    AMEN=False
    BMEN=False
    CMEN=False
    DMEN=True
    lcd.clear()
    lcd.set_cursor_pos(0,0)
    lcd.print("Custom")
    lcd.set_cursor_pos(0,15)
    lcd.print("D")
    time.sleep(1)
    lcd.set_cursor_pos(0,0)
    lcd.print("Set Speed:")
    lcd.set_cursor_pos(1,0)

    speed=""
    characters =["1","2","3","4","5","6","7","8","9","A","B","C","D","*","#","0"]
    while DMEN:
        x = KeyPad.getkey()
        if x != -999: # A key has been pressed!
            if x == 15:
                break
            lcd.print(characters[x-1])
            speed+=characters[x-1]
            
    #speed=int(speed)            

    # Setup STEP and DIR pins
    step_pin_dip = digitalio.DigitalInOut(board.GP2)
    step_pin_dip.direction = digitalio.Direction.OUTPUT
    step_pin_rot = digitalio.DigitalInOut(board.GP6)
    step_pin_rot.direction = digitalio.Direction.OUTPUT

    dir_pin_dip = digitalio.DigitalInOut(board.GP3)  # Optional direction control
    dir_pin_dip.direction = digitalio.Direction.OUTPUT
    dir_pin_rot = digitalio.DigitalInOut(board.GP7)
    dir_pin_rot.direction = digitalio.Direction.OUTPUT


    # Set direction
    dir_pin_dip.value = True  # True or False for direction
    dir_pin_rot.value = True

    # Motor step settings
    step_delay = 0.00051  # Delay between steps in seconds (adjust for speed)

    # Number of steps
    step_count = 600  # One full rotation for 1.8° stepper at 1 step/full

    while DMEN:
        for _ in range(step_count):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            time.sleep(step_delay)
            #time.sleep(2)
        

        # Optional direction change after each full rotation
        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
        time.sleep(1)  # Wait 1 second before changing direction
        
        for _ in range(step_count):
            step_pin_dip.value = True
            time.sleep(step_delay)
            step_pin_dip.value = False
            time.sleep(step_delay)
            #time.sleep(2)
        
        for _ in range(400):
            step_pin_rot.value=True
            time.sleep(step_delay)
            step_pin_rot.value=False
            time.sleep(step_delay)

        dir_pin_dip.value = not dir_pin_dip.value
        dir_pin_rot.value=not dir_pin_rot.value
D_menu()