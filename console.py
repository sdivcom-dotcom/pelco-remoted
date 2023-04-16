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

parser.add_argument('-prot', '--protocol',
                    dest='protocol',
                    help='protocol camera',
                    default="p",
                    type=str)

parser.add_argument('-c', '--command',
                    dest='command',
                    help='command camera',
                    default='stop',
                    type=str)

args = parser.parse_args()
command = args.command
port = args.port
baud = args.baud
address = args.address
protocol = args.protocol

if command == "up":
    up(port, baud, address, protocol)

elif command == "down":
    down(port, baud, address, protocol)

elif command == "right":
    right(port, baud, address, protocol)

elif command == "left":
    left(port, baud, address, protocol)

elif command == "zoom_plus":
    zoom_plus(port, baud, address, protocol)

elif command == "zoom_minus":
    zoom_minus(port, baud, address, protocol)

elif command == "focus_plus":
    focus_plus(port, baud, address, protocol)

elif command == "focus_minus":
    focus_minus(port, baud, address, protocol)

else:
    print("Not command")