import numpy as np
import matplotlib.pyplot as plt

T_half_U238 = 4.468e9
T_half_Th234 = 24.1 / 365
T_half_Pa234 = 6.7 / (365 * 24)
lambda1 = np.log(2) / T_half_U238
lambda2 = np.log(2) / T_half_Th234
lambda3 = np.log(2) / T_half_Pa234

def decay_chain(N, t):
 N1, N2, N3 = N
 dN1dt = -lambda1 * N1
 dN2dt = lambda1 * N1 - lambda2 * N2
 dN3dt = lambda2 * N2 - lambda3 * N3
 return np.array([dN1dt, dN2dt, dN3dt])

def rk4_step(func, N, t, dt):
 k1 = func(N, t)
 k2 = func(N + 0.5 * dt * k1, t + 0.5 * dt)
 k3 = func(N + 0.5 * dt * k2, t + 0.5 * dt)
 k4 = func(N + dt * k3, t + dt)
 return N + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

N0 = np.array([1e6, 0, 0])
t_max = 1e6
dt = 1e3
time = np.arange(0, t_max, dt)
results = np.zeros((len(time), 3))
results[0] = N0

for i in range(1, len(time)):
 results[i] = rk4_step(decay_chain, results[i-1], time[i-1], dt)

plt.plot(time, results[:,0], label='U-238')
plt.plot(time, results[:,1], label='Th-234')
plt.plot(time, results[:,2], label='Pa-234')
plt.xlabel('Time (years)')
plt.ylabel('Number of Nuclei')
plt.legend()
plt.grid(True)
plt.show()