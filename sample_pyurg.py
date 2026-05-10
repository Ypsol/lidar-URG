#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pyurg
import time
import numpy as np

# For initializing.

# Connect to the URG device.
# If could not conncet it, get False from urg.connect()


# Get length datas and timestamp.
# If missed, get [] and -1 from urg.capture()


# Print lengths.

# while True:
#     data, timestamp = urg.capture()
#     ligne = "  ".join(str(length) for length in data)
#     print(f"\r{ligne}   ", end="", flush=True)
#     time.sleep(0.1)


urg = pyurg.UrgDevice()
if not urg.connect():
    print('Could not connect.')
    exit()
data, timestamp = urg.capture()

# data = np.random.rand(276,1)*3000

angles = np.linspace(0, 360, len(data), endpoint=False)

# Create a vector with two components: data and angle
vector = np.array(list(zip(data, angles)))

print(vector[:, 0])