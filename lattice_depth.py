import numpy as np

k_b = 1.38064852*1e-23                  # Boltzmann constant m^2 Kg s^-2 K^-1
m_p = 1.6726219*1e-27                   # mass of Proton  Kg
u = 1.66053906660e-27                   # atomic mass unit  Kg
h = 6.626070150*1e-34                   # Planck Constant  J-s
hbar = h/(2*np.pi)                      # (1/(2*pi))*Planck Constant  J-s
c = 2.99792458*1e8                      # velocity of light   m/s
k = 2*np.pi/(813.428*1e-9)
epsilon = 8.854187817*1e-12             # Vacuum permittivity F?m?1
Gamma = 2*np.pi*6e-3                    # 3Po spontaneous decay  frequency
Omega = 2*np.pi*c/(813.428*1e-9)        # lattice laser
Omega_0 = 2*np.pi*c/(698.4*1e-9)        # 3P0-1S0
Delta = Omega_0 - Omega                 # Detuning of lattice laser
Alpha = 286*1.648777*1e-41              # polarizability   C m2/V

w0 = 40e-6                              # focussed beam waist of lattice laser
P0 = 0.63                                # Lattice power in watt

E_r = ((hbar)**2)*(k**2)/(2*87.91*m_p)          # Recoil energy
V0 = (Alpha*4*P0)/(epsilon*c*np.pi*(w0**2))     #Trap depth
T0 =1e6*V0/k_b                                  # Trap depth in temperature
s=V0/E_r                                        # Trap depth in E_r

f_rad = (1/(np.pi*w0))*np.sqrt(V0/(87.91*u))                 # radial trapping frequency
f_axi = (1/(813.428*1e-9))*np.sqrt(2*V0/(87.91*u))           # axial trapping frequency

print("Radial trapping frequency (Hz):", f_rad)
print("Axial trapping frequency (Hz):", f_axi)