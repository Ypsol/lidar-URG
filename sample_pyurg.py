#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyurg
import time

# For initializing.
urg = pyurg.UrgDevice()

# Connect to the URG device.
# If could not conncet it, get False from urg.connect()
if not urg.connect():
    print('Could not connect.')
    exit()

# Get length datas and timestamp.
# If missed, get [] and -1 from urg.capture()


# Print lengths.

while True:
    data, timestamp = urg.capture()
    ligne = "  ".join(str(length) for length in data)
    print(f"\r{ligne}   ", end="", flush=True)
    time.sleep(0.1)

