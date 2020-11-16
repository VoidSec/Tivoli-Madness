#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
JamoDat – TSMManager Viewer, python client
Paolo Stagno aka VoidSec - https://voidsec.com
"""
import struct
import socket
import sys
import argparse

parser = argparse.ArgumentParser(prog="TSM_Client.py", description="Pyhton Client for JamoDat – TSMManager by VoidSec")
parser.add_argument("-t", "--target", default="127.0.0.1", dest="target", help="Target IP Address")
parser.add_argument("-p", "--port", default=1955, type=int, dest="port", help="Target TCP Port")
args = parser.parse_args()

target = args.target
port = args.port

""" GetVersion

> Request:
00000000  09 00 00 00 00 00 00 00  ff 00 63 00               ........ ..c.
0000000C  4f 07 07 4c 07 07 07 07  07                        O..L.... .

> Response:
00000000  09 00 00 00 00 00 00 00  ff 00 63 00               ........ ..c.
0000000C  36 2e 33 2e 30 2e 32 33  00                        6.3.0.23 .
"""
GetVersion = bytearray(b"\x09\x00\x00\x00\x00\x00\x00\x00\xff\x00\x63\x00\x4f\x07\x07\x4c\x07\x07\x07\x07\x07")


def connection(target, port, method):
    """
    :param target: target IP Address
    :param port: target TCP Port
    :param method: method to use
    :return data: return data received from the socket
    """
    data = ""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.send(method)
        data=s.recv(1024)
        s.close()
    except socket.error as e:
        print(e)
        quit()

    return data


data = connection(target, port, GetVersion)
print("TSMManager Collector Reported Version: {}".format(data[12:19]))