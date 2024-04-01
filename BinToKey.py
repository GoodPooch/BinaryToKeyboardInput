import usb.core
import keyboard
import usb.util
import time

dev=usb.core.find(idVendor=0x0b43,idProduct=0x0001)
ep=dev[0].interfaces()[0].endpoints()[0]
i=dev[0].interfaces()[0].bInterfaceNumber
dev.set_configuration()
eaddr=ep.bEndpointAddress
def get_input(value,valoo):
    if (value & (1 << 6)) != 0:
       
        keyboard.press("down")
    else:
        keyboard.release("down")
    if (value & (1 << 7)) != 0:
       
        keyboard.press("left")
    else:
        keyboard.release("left")
    if (value & (1 << 5)) != 0:
    
        keyboard.press("right")
    else:
        keyboard.release("right")
    if (value & (1 << 4)) != 0:
      
        keyboard.press("up")
    else:
        keyboard.release("up")
    if (value & (1 << 1)) != 0:
      
        keyboard.press("enter")
    else:
        keyboard.release("enter")
    if (value & (1 << 0)) != 0:
      
        keyboard.press("esc")
    else:
        keyboard.release("esc")
    if (valoo & (1 << 0)) != 0:
      
        keyboard.press("a")
    else:
        keyboard.release("a")
    if (valoo & (1 << 1)) != 0:
      
        keyboard.press("o")
    else:
        keyboard.release("o")
    if (valoo & (1 << 2)) != 0:
      
        keyboard.press("x")
    else:
        keyboard.release("x")
    if (valoo & (1 << 3)) != 0:
      
        keyboard.press("e")
    else:
        keyboard.release("e")
print("started")
while(True):
    try:
        
        get_input(dev.read(129,7,10000).tolist()[1],dev.read(129,7,10000).tolist()[0])
    except usb.core.USBError:
        print("dropped")

print("Program exited")

