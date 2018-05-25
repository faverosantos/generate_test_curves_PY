# Generates some test curves
Generates some test curves using Python 3.0

# How to convert number of samples to time?
NS = SD*FS + 1 \
SD being signal duration in [s] \
FS being sampling frequency in [Hz] \
NS being number of samples \
\
For example:

Sample0 is at 0 us; \
Sample1 is at 20 us; \
Sample2 is at 40 us; \
Sample3 is at 60 us. \
So TS is 20 us and FS = 50 kHz.

Sample2 is at 40 us, then: \
NS = SD * FS + 1 \
NS = 40u * 50k + 1 \
NS = 2 + 1 \
NS = 3 -> Sample2 is at position 3.

# Specs
Made with Python 3.6.1 \
Depends on: numpy 1.12.1 and matplotlib 2.0.2