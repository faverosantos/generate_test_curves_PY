import matplotlib.pyplot as plt
import numpy as np

class Defines:

    # Sampling frequency
    FS = 50000
    N_SAMPLES = 10000

def generate_sine_wave(frequency, offset, amplitude):
    local_frequency = frequency
    DC = offset
    AMP = amplitude

    w = 2 * np.pi * local_frequency
    x = np.arange(Defines.N_SAMPLES)

    y = DC + AMP*np.sin(w * x / Defines.FS)



    duration = (len(x) - 1) / Defines.FS
    #print(duration)

    #file = open("signal.txt","w")
    #for local_index in range(0, len(y)):
    #    file.write(str(y[local_index]))
    #    file.write("\n")
    #file.close()

# Generates a PDF: Probability Density Function
def generate_PDF(gain, center_position, standard_deviation):
    x = np.arange(Defines.N_SAMPLES)
    a = gain
    b = center_position
    c = standard_deviation

    a = 1/(c*np.sqrt(2*np.pi))
    d = (-1/2)*np.square((x-b)/c)

    y = a * np.exp(d)

    plt.plot(x,y)
    plt.show()
    return [x, y]


def main():

    #generate_sine_wave(1000, 1.65, 1.65)
    plot_data = generate_PDF(100, 5000, 50)

    #plt.plot(plot_data[0], plot_data[1])
    #plt.show()

if __name__ == "__main__":
    main()
