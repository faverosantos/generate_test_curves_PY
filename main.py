import matplotlib.pyplot as plt
import numpy as np

class Defines:

    # Sampling frequency
    FS = 50000
    N_SAMPLES = 10000



def main():

    # Nova alteração

    local_frequency = 1000
    w = 2 * np.pi * local_frequency

    x = np.arange(Defines.N_SAMPLES)
    DC = 1.65
    AMP = 1.65

    y = DC + AMP*np.sin(w * x / Defines.FS)

    plt.plot(x, y)
    plt.xlabel('sample(n)')
    plt.ylabel('voltage(V)')
    plt.show()

    duration = (len(x) - 1)/Defines.FS
    print(duration)

    #file = open("signal.txt","w")
    #for local_index in range(0, len(y)):
    #    file.write(str(y[local_index]))
    #    file.write("\n")
    #file.close()

if __name__ == "__main__":
    main()
