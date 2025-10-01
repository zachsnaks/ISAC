import match_filter as matf
import numpy as np
import matplotlib.pyplot as plt
import time
import sys


#Constants
c = 3e8 # Speed of light
k = 1.38e-23 # Boltzmanns constant
T = 290 # Standard temperature in Kelvin

def print_value(name):
    try:
        value = locals().get(name) or globals().get(name)
        if value is not None:
            print(f"{value}")
    except:
        print(f"Error: {name} not found")

# Input Parameters
fc = 3.5e9  # Carrier Frequency in Hz
bandwidth = 10e6 # Bandwidth in Hz
theta_i = 0 # incidence angle in degrees
sigma = 1 # Target radar cross section in m^2
Pt = 1e3 # Peak transmit power in W
Gt = 10 # Transmit gain
Gr = 10 # Receive gain
R = 1000 # Range to target in m


tau = 2*R/c
L = 10*np.log10(1.5) # System loss in dB
Omega = np.cos(np.deg2rad(theta_i)) 
lam = c/fc # Wavelength in m

Pr = (Pt*Gt*Gr*lam**2*sigma*Omega)/( (4*np.pi)**3 * R**4 * L )
Pn = k*T*bandwidth

SNR = 10*np.log10(Pr/Pn)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print_value(sys.argv[1])

