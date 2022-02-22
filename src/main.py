#!/usr/bin/env python3

from datetime import time
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
    pass

def scan_compare():
    pass

def notify():
    pass


