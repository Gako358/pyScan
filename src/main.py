#!/usr/bin/env python3

from datetime import time, datetime
from pathlib import Path
from colorama import Fore, Back, Style
from crontab import CronTab
from getpass import getpass
import time
import nmap
import sys
import os


# Setting up the nmap variables
Options = "-sS -F -T4 -n -vv"

# System
Home = str(Path.home())
Date = datetime.today().strftime('%d-%m-%Y')
POSIXPath = r"/tmp/net_monitor"
POSIXDIRPath = os.path.isdir(POSIXPath)

def setUp():
    time.sleep(1)
    global Network

    Network = input("Enter the IP address and CIDR of the network (Example: 10.0.0.1\\8, 192.168.1.0\\16)\n")

    os.mkdir(POSIXPath)
    os.chdir(POSIXPath)
    OGState = sys.stdout
    with open(r"/tmp/net_monitor/base_scan", 'w+') as linuxScan:
        sys.stdout = linuxScan
        Mapper = nmap.PortScanner()
        Mapper.scan(Network, arguments=Options)
        print(Mapper.csv())

        sys.stdout = OGState
    print(Fore.GREEN + "Network Baseline has been generated!")
    print(Style.RESET_ALL)

def nmscan():
    OGState = sys.stdout
    with open("/tmp/net_monitor/{}_net_scan".format(Date), "w+") as linuxScan:
        sys.stdout = linuxScan
        Mapper = nmap.PortScanner()
        Mapper.scan(Network, arguments=Options)
        print(Mapper.csv())
        sys.stdout = OGState

def scan_compare():
    with open(r"/tmp/net_monitor/base_scan", "r") as Baseline, open("/tmp/net_monitor/{}_net_scan".format(Date), 'r') as newScan:
        Baseline = Baseline.readlines()
        newScan = newScan.readlines()

    with open(r"/tmp/net_monitor/net_alert", 'w') as outFile:
        for line in newScan:
            if line not in Baseline:
                outFile.write(line)


def notify():
    pass

if POSIXDIRPath == False:
    setUp()

elif POSIXDIRPath == True:
    nmscan()
    scan_compare()

