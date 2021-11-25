import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.special

class Defines:

    # Sampling frequency
    FS = 10000
    # Number of samples
    N_SAMPLES = 5000


# Generates a sine wave
def generate_sine_wave(frequency, offset, amplitude):
    local_frequency = frequency
    DC = offset
    AMP = amplitude

    w = 2 * np.pi * local_frequency
    x = np.arange(Defines.N_SAMPLES)

    y = DC + AMP*np.sin(w * x / Defines.FS)

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


def save_file(name, y):
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


def main():

    data = generate_binary(2, 0, 5)
    #[plot_data_1, plot_data_2] = generate_PDF(10000, 2500, 200)
    # [plot_data_1, plot_data_2] = generate_EMGD(-8, 0.1, 0.3)
    # [plot_data_1, plot_data_2] = generate_SND(5)
    # [plot_data_1, plot_data_2] = generate_exponential()

    plt.plot(data)
    #plt.plot(plot_data_1, label="P dependent only")
    #plt.plot(plot_data_2, label="T and P dependent")
    #plt.plot(plot_data_1 + plot_data_2, label="sum of both")
    #plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1))
    #plt.ylim([0, 60000])
    #plt.xlim([0, 20000])
    plt.show()


    save_file("square_wave_fs_10k_f_2_dc0ac5v.txt", data)


if __name__ == "__main__":
    main()
