import serial
import os, time

# Enable Serial Communication
port = serial.Serial("/dev/ttyAMA0", baudrate=115200, timeout=1)

# Transmitting AT Commands to the Modem
# '\r\n' indicates the Enter key

port.write('AT'+'\r\n')
rcv = port.read(10)
print rcv
