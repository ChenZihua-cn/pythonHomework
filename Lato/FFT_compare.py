import numpy as np
import matplotlib.pyplot as plt

# Parameters
time = np.linspace(0, 10, 10000)  # Time array
omega_p = 2 * np.pi * 1.5         # Driving frequency

# Rigid Model (single frequency response)
rigid_motion = np.sin(omega_p * time)
rigid_spectrum = np.fft.fft(rigid_motion)
rigid_freqs = np.fft.fftfreq(len(rigid_motion), d=time[1] - time[0])

# Elastic Model (multiple frequency response with harmonics)
elastic_motion = np.sin(omega_p * time) + 0.3 * np.sin(2 * omega_p * time) + 0.1 * np.sin(3 * omega_p * time)
elastic_spectrum = np.fft.fft(elastic_motion)
elastic_freqs = np.fft.fftfreq(len(elastic_motion), d=time[1] - time[0])

# Plotting
plt.figure(figsize=(12, 6))

# Rigid Model Frequency Spectrum
plt.subplot(1, 2, 1)
plt.plot(rigid_freqs[:len(rigid_freqs)//2], 
         np.abs(rigid_spectrum[:len(rigid_spectrum)//2]), color='blue', label='Rigid Model')
plt.title("Frequency Spectrum of Rigid Model")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.yscale('log')
plt.legend()

# Elastic Model Frequency Spectrum
plt.subplot(1, 2, 2)
plt.plot(elastic_freqs[:len(elastic_freqs)//2], 
         np.abs(elastic_spectrum[:len(elastic_spectrum)//2]), color='red', label='Elastic Model')
plt.title("Frequency Spectrum of Elastic Model")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")
plt.yscale('log')
plt.legend()

plt.tight_layout()
plt.show()
