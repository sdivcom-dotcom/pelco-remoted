import serial
import time

#commands PELCO-P
const_stop_p = "00000000"
const_up_p = "00080020"
const_down_p = "00100020"
const_left_p = "00042000"
const_right_p = "00022000"
const_zoom_plus_p = "00200000"
const_zoom_minus_p = "00400000"
const_focus_plus_p = "00800000"
const_focus_minus_p = "01000000"

#commands PELCO-D
const_stop_d = "00000000"
const_up_d = "00083F3F"
const_down_d = "00103F3F"
const_left_d = "00043F3F"
const_right_d = "00023F3F"
const_focus_plus_d = "00200000"
const_focus_minus_d = "00400000"
const_zoom_plus_d = "00800000"
const_zoom_minus_d = "01000000"

def pelco_p_data(address, command):
    address = str(address)
    command = str(command)
    start_byte = "A0"
    af_byte = "AF"
    checksum = "00"
    #data = "A0" + "ADDRESS" + "Data 1 to 4" + "ETX" + "xOR sum of Bytes 1 to 7"
    data = start_byte + address + command + af_byte + checksum
    return data


def pelco_d_data(address, command):
    address = str(address)
    command = str(command)
    start_byte = "FF"
    checksum = "00"
    #data = "A0" + "ADDRESS" + "Data 1 to 4" + "xOR sum of Bytes 1 to 7"
    data = start_byte + address + command + checksum
    return data

def write_command(port, baud, data, data_stop):
    ser = serial.Serial(port=port, baudrate=baud)
    data_hex = bytes.fromhex(data)
    data_stop_hex = bytes.fromhex(data_stop)
    ser.write(data_hex)
    time.sleep(0.4)
    ser.write(data_stop_hex)
    ser.close()


def up(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_up = const_up_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_up)
    elif procotol == "d":
        command_stop = const_stop_d
        command_up = const_up_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_up)
    else:
        pass
    write_command(port, baud, data, data_stop)


def down(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_down = const_down_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_down)
    elif procotol == "d":
        command_stop = const_stop_d
        command_down = const_down_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_down)
    else:
        pass
    write_command(port, baud, data, data_stop)


def left(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_left = const_left_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_left)
    elif procotol == "d":
        command_stop = const_stop_d
        command_left = const_left_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_left)
    else:
        pass
    write_command(port, baud, data, data_stop)


def right(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_right = const_right_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_right)
    elif procotol == "d":
        command_stop = const_stop_d
        command_right = const_right_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_right)
    else:
        pass
    write_command(port, baud, data, data_stop)


def zoom_plus(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_zoom_plus = const_zoom_plus_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_zoom_plus)
    elif procotol == "d":
        command_stop = const_stop_d
        command_zoom_plus = const_zoom_plus_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_zoom_plus)
    else:
        pass
    write_command(port, baud, data, data_stop)


def zoom_minus(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_zoom_minus = const_zoom_minus_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_zoom_minus)
    elif procotol == "d":
        command_stop = const_stop_d
        command_zoom_minus = const_zoom_minus_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_zoom_minus)
    else:
        pass
    write_command(port, baud, data, data_stop)

def focus_plus(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_focus_plus = const_focus_plus_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_focus_plus)
    elif procotol == "d":
        command_stop = const_stop_d
        command_focus_plus = const_focus_plus_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_zoom_plus)
    else:
        pass
    write_command(port, baud, data, data_stop)


def focus_minus(port, baud, address, procotol):
    if procotol == "p":
        command_stop = const_stop_p
        command_focus_minus = const_focus_minus_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command_focus_minus)
    elif procotol == "d":
        command_stop = const_stop_d
        command_focus_minus = const_focus_minus_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command_focus_minus)
    else:
        pass
    write_command(port, baud, data, data_stop)


def random_command(port, baud, address, protocol, command):
    if procotol == "p":
        command_stop = const_stop_p
        data_stop = pelco_p_data(address, command_stop)
        data = pelco_p_data(address, command)
    elif procotol == "d":
        command_stop = const_stop_d
        data_stop = pelco_d_data(address, command_stop)
        data = pelco_d_data(address, command)
    else:
        pass
    write_command(port, baud, data, data_stop)