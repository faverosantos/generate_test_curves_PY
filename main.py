import matplotlib.pyplot as plt
import numpy as np

class Defines:

    # Sampling frequency
    FS = 50000
    # Number of samples
    N_SAMPLES = 20000

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

def main():

    #[plot_data_1, plot_data_2] = generate_sine_wave(1000, 1.65, 1.65)
    [plot_data_1, plot_data_2] = generate_PDF(120000, 5000, 600)
    #[plot_data_1, plot_data_2] = generate_exponential()

    plt.plot(plot_data_1, plot_data_2)
    #plt.plot(plot_data_1, label="P dependent only")
    #plt.plot(plot_data_2, label="T and P dependent")
    #plt.plot(plot_data_1 + plot_data_2, label="sum of both")
    #plt.legend(loc='upper right', bbox_to_anchor=(1, 1.1))
    #plt.ylim([0, 60000])
    #plt.xlim([0, 20000])
    plt.show()

    #save_file("gauss_pdf_V00_R02.txt", plot_data[1])


if __name__ == "__main__":
    main()
