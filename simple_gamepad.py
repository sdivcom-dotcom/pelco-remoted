import hid
import time
#0x0079:0x0011
for device in hid.enumerate():
    print(f"0x{device['vendor_id']:04x}:0x{device['product_id']:04x} {device['product_string']}")

gamepad = hid.device()
gamepad.open(0x0079, 0x0011)
gamepad.set_nonblocking(True)
while True:
    report = gamepad.read(16)
    if report:
        #print(report)
        if report[3] == 0:
            print("left")
            time.sleep(0.4)
        elif report[3] == 255:
            print("right")
            time.sleep(0.4)
        elif report[4] == 0:
            print("up")
            time.sleep(0.4)
        elif report[4] == 255:
            print("down")
            time.sleep(0.4)
        elif report[6] == 16:
            print("select")
            time.sleep(0.6)
        elif report[6] == 32:
            print("start")
            time.sleep(0.6)
        elif report[5] == 31:
            print("1 button")
            time.sleep(0.4)
        elif report[5] == 47:
            print("2 button")
            time.sleep(0.4)
        elif report[5] == 79:
            print("3 button")
            time.sleep(0.4)
        elif report[5] == 143:
            print("4 button")
            time.sleep(0.4)
        elif report[6] == 1:
            print("left 1")
            time.sleep(0.4)
        elif report[6] == 4:
            print("left 2")
            time.sleep(0.4)
        elif report[6] == 2:
            print("right 1")
            time.sleep(0.4)
        elif report[6] == 8:
            print("right 2")
            time.sleep(0.4)