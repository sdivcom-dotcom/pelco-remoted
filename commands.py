import serial
import time

import paramiko

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

delay_run = 0.37
delay_optic = 0.05
ssh_port = 22

def pelco_p_data(address, command):
    address = str(address)
    command = str(command)
    start_byte = "A0"
    af_byte = "AF"
    checksum = "00"
    data = start_byte + address + command + af_byte + checksum
    #print(data)
    return data


def pelco_d_data(address, command):
    address = str(address)
    command = str(command)
    start_byte = "FF"
    checksum = "00"
    data = start_byte + address + command + checksum
    return data


def write_com_command(port, baud, data, data_stop, delay):
    ser = serial.Serial(port=port, baudrate=baud)
    data_hex = bytes.fromhex(data)
    data_stop_hex = bytes.fromhex(data_stop)
    ser.write(data_hex)
    time.sleep(delay)
    ser.write(data_stop_hex)
    ser.close()

 
def write_ssh_command(address, user, password, command, procotol, cam_address):
    ssh_command = "python3 pelco-remoted/console.py -pr " + procotol + " -t com " + " -c " + command
    print(ssh_command)
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(address, ssh_port, user, password)
        stdin, stdout, stderr = ssh.exec_command(ssh_command)
        stdin.close()
        
        lines = stdout.readlines()
        print(lines,type(lines))
    except Exception as e:
        print("Error: ", e)
    finally:
        ssh.close()


def up(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_run
    ssh_command = "up"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def down(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_run
    ssh_command = "down"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass


def left(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_run
    ssh_command = "left"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def right(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_run
    ssh_command = "right"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def zoom_plus(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_optic
    ssh_command = "zoom_plus"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def zoom_minus(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_optic
    ssh_command = "zoom_minus"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def focus_plus(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_optic
    ssh_command = "focus_plus"
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
    if transport == "com":
        transport == "com"
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def focus_minus(port, baud, address, procotol, ssh_address, ssh_user, ssh_password, transport):
    delay = delay_optic
    ssh_command = "focus_minus"
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
    if transport == "com":
        write_com_command(port, baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, ssh_command, procotol, address)
    else:
        pass



def random_command(com_port, com_baud, address, protocol, command, ssh_address, ssh_user, ssh_password, transport):
    delay = 0.5
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
    if transport == "com":
        write_com_command(com_port, com_baud, data, data_stop, delay)
    elif transport == "ssh":
        write_ssh_command(ssh_address, ssh_user, ssh_password, command, procotol, address)
    else:
        pass

