import matplotlib.pyplot as plt
import numpy as np
import rflib as rf
import scipy.special

class Defines:

    # Sampling frequency
    FS = 1E7
    # Number of samples
    N_SAMPLES = 10000


# Generates a sine wave
def generate_sine_wave(carrierFrequency, carrierOffset, carrierAmplitude, carrierPhase):
    cf = carrierFrequency
    co = carrierOffset
    ca = carrierAmplitude
    cp = rf.degree_to_rad(carrierPhase)

    w = 2 * np.pi * cf
    x = np.arange(Defines.N_SAMPLES)

    y = co + ca*np.sin((w * x / Defines.FS) + cp)

    return [x, y]

#reference: https://en.wikipedia.org/wiki/Amplitude_modulation
def generate_am_modulated_wave(messageFrequency, messageOffset, messageAmplitude, messagePhase, carrierFrequency, carrierOffset, carrierAmplitude, carrierPhase):

    fm = messageFrequency
    om = messageOffset
    ma = messageAmplitude
    mp = rf.degree_to_rad(messagePhase)

    cf = carrierFrequency
    co = carrierOffset
    ca = carrierAmplitude
    cp = rf.degree_to_rad(carrierPhase)

    x = np.arange(Defines.N_SAMPLES)

    # Message sine-wave
    wm = 2 * np.pi * fm
    message = ma*np.sin((wm * x / Defines.FS) + mp)

    # Carrier sine-wave
    wc = 2 * np.pi * cf
    carrier = ma*np.sin((wc * x / Defines.FS) + cp)

    # Moulated signal
    y = message*carrier

    return [x, y]

# Generates a PDF (Probability Density Function)
def generate_PDF(gain, center_position, standard_deviation):
    x = np.arange(Defines.N_SAMPLES)

    b = center_position
    c = standard_deviation
    a = gain / (c * np.sqrt(2 * np.pi))
    d = (-1/2)*np.square((x-b)/c)

    y = a * np.exp(d)

    return [x, y]


def save_file(name, details, y):
    file = open(name,"w")

    for local_index in range(0, len(y)):
        file.write(str(y[local_index]))
        file.write("\n")
    file.close()


# Generates an Exponentially modified gaussian distribution
def generate_EMGD(mean, variance, skew):
    x = np.arange(-10, 10, 0.001)

    m = mean
    v = variance
    s = skew

    a = (skew/2)
    b = a*(2*m + s*np.square(v)-2*x)
    c = (m + s*np.square(v)-x)/(np.square(2)*v)
    d = 1 - scipy.special.erf(c)

    y = a*np.exp(b)*d
    max_y = max(y)
    y = y/max_y

    return [x, y]

# Generates a skew normal distribution
def generate_SND(skew):
    x = np.arange(-10, 10, 0.001)

    s = skew

    a = (1/np.sqrt(2*np.pi))
    b = np.square(x)/2
    c = s*x/np.sqrt(2)
    d = (1/2)*(1 + scipy.special.erf(c))

    y = 2*a*np.exp(-b)*d
    max_y = max(y)
    y = y/max_y

    return [x, y]

def generate_exponential():
    x = np.arange(Defines.N_SAMPLES)

    Y1 = 3216.71869
    Y2 = 1615.88683
    R1 = -0.00058
    R2 = -2.02E-04
    A1 = -42031.31237
    A2 = -3523.87996

    T = 35.6

    y1 = Y1 + A1*np.exp(R1*x)
    y2 = T*(Y2 + A2*np.exp(R2*x))

    return [y1, y2]

def generate_binary(frequency, offset, amplitude):
    local_frequency = frequency
    DC = offset
    AMP = amplitude

    y = list()
    state = 0

    samplesPerCycles = Defines.FS/frequency

    for index in range(Defines.N_SAMPLES):
        if index % (samplesPerCycles/2) == 0:
            state = not state

        y.append(int(state))

    return y

def generate_pairs(x,y):

    pairs = []
    for index in range(0, len(x)):
        pairs.append((x[index], y[index]))
    return pairs

def main():

    [x, y] = generate_am_modulated_wave(10E3, 0, 0.1, 0, 100E3, 0, 1, 0)

    pairs = generate_pairs(x, y)
    np.savetxt('data.csv', pairs, delimiter=',')

    plt.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()
