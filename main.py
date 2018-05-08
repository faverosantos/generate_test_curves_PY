import matplotlib.pyplot as plt
import numpy as np

class Defines:

    # Sampling frequency
    FS = 50000
    # Number of samples
    N_SAMPLES = 10000

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

def main():

    #generate_sine_wave(1000, 1.65, 1.65)
    plot_data = generate_PDF(120000, 5000, 600)

    plt.plot(plot_data[0], plot_data[1])
    plt.show()

    save_file("gauss_pdf_V00_R02.txt", plot_data[1])


if __name__ == "__main__":
    main()
