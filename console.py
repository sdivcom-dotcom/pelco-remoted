from commands import *
import argparse


parser = argparse.ArgumentParser(description="")

parser.add_argument('-p', '--port',
                    dest='port',
                    help='Port CH341a',
                    default='/dev/ttyUSB0',
                    type=str)

parser.add_argument('-b', '--baud',
                    dest='baud',
                    help='baud rate camera',
                    default=2400,
                    type=int)

parser.add_argument('-a', '--address',
                    dest='address',
                    help='address camera',
                    default='01',
                    type=str)

parser.add_argument('-pr', '--protocol',
                    dest='protocol',
                    help='protocol camera',
                    default="p",
                    type=str)

parser.add_argument('-c', '--command',
                    dest='command',
                    help='command camera',
                    default='stop',
                    type=str) 

parser.add_argument('-sa', '--ssh_address',
                    dest='ssh_address',
                    help='ssh address',
                    default='192.168.11.54',
                    type=str) 

parser.add_argument('-su', '--ssh_user',
                    dest='ssh_user',
                    help='user camera server',
                    default='server',
                    type=str) 

parser.add_argument('-sp', '--ssh_password',
                    dest='ssh_password',
                    help='password camera server',
                    default='1qaz2wsx',
                    type=str) 

parser.add_argument('-t', '--transport',
                    dest='transport',
                    help='transport camera server',
                    default='ssh',
                    type=str) 

args = parser.parse_args()
command = args.command
port = args.port
baud = args.baud
address = args.address
protocol = args.protocol
ssh_address = args.ssh_address
ssh_user = args.ssh_user
ssh_password = args.ssh_password
transport = args.transport

if command == "up":
    if transport == "com":
        transport =="com"
        up(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport =="ssh"
        print(ssh_address)
        print(ssh_user)
        print(ssh_password)
        print(protocol)
        print(transport)
        up(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "down":
    if transport == "com":
        transport = "com"
        down(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        down(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "right":
    if transport == "com":
        transport = "com"
        right(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        right(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "left":
    if transport == "com":
        transport = "com"
        left(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        left(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "zoom_plus":
    if transport == "com":
        transport = "com"
        zoom_plus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        zoom_plus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "zoom_minus":
    if transport == "com":
        transport = "com"
        zoom_minus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        zoom_minus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "focus_plus":
    if transport == "com":
        transport = "com"
        focus_plus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        focus_plus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

elif command == "focus_minus":
    if transport == "com":
        transport = "com"
        focus_minus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    elif transport == "ssh":
        transport = "ssh"
        focus_minus(port, baud, address, protocol, ssh_address, ssh_user, ssh_password, transport)
    else:
        pass

else:
    print("Not command")