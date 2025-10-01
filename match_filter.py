import numpy as np

def compute_threshold(s, h):
    print("\nComputing threshold...")

    s_energy = np.sum(np.square(s))
    h_energy = np.sum(np.square(h))

    sum = s_energy - h_energy

    return sum / 2



def matched_filter(s, h):
    # Compute the Fourier transform of padded_input and padded_filter
    S = np.fft.fft(s)
    H = np.fft.fft(h)

    # Compute the convolution of the two Fourier transforms
    Y = S * H

    # Compute the inverse Fourier transform of Y to obtain the time-domain output signal y
    y = np.fft.ifft(Y)

    return y