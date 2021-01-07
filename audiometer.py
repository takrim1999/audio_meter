import pyaudio
import struct
import numpy as np
import time
# import matplotlib.pyplot as plt



CHUNK = 1600
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
p = pyaudio.PyAudio()

stream = p.open(
    format = FORMAT,
    channels = CHANNELS,
    rate = RATE,
    input = True,
    output= True,
    frames_per_buffer= CHUNK
)

while True:
    data = stream.read(CHUNK)
    data_int = struct.unpack(str(2 * CHUNK) + "B" , data)
    print("/"*(round(sum(data_int)/len(data_int)) - 80))
    