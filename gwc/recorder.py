import collections
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008


# Software SPI configuration:
CLK  = 18
MISO = 23
MOSI = 24
CS   = 25
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

CHANNEL = 7
DURATION_SEC = 10

# Main program loop.
samples = collections.deque()
start_time = time.time()
while time.time() < (start_time + DURATION_SEC):
    # Read the ADC channel value.
    value = mcp.read_adc(CHANNEL)
    samples.append(value)

while True:
    try:
        print samples.pop()
    except IndexError:
        break
