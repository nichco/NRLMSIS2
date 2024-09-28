import numpy as np
import matplotlib.pyplot as plt

# new model for temp and density through 300 km

rho = np.array([1.295E-03,3.976E-04,8.152E-05,1.546E-05,3.150E-06,8.166E-07,2.234E-07,5.589E-08,1.247E-08,
                2.693E-09,5.440E-10,8.380E-11,1.717E-11,6.279E-12,3.127E-12,1.814E-12,1.150E-12,7.706E-13,
                5.368E-13,3.844E-13,2.811E-13,2.090E-13,1.574E-13,1.199E-13,9.218E-14,7.147E-14,5.583E-14,
                4.390E-14,3.472E-14,2.761E-14,2.207E-14]) * 1E6 / 1000 # kg/m^3


T = np.array([269.5,212.9,207.3,216.4,247.2,254.8,238.8,222.8,214.6,205.1,186.3,
              230.8,380.6,525.5,629.6,703.9,756.9,794.8,821.9,841.3,855.2,865.2,
              872.4,877.5,881.2,883.9,885.8,887.2,888.2,888.9,889.5]) # K

h = np.array([0,10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,
              210,220,230,240,250,260,270,280,290,300])



T_100 = np.array([269.5,244.1,212.9,213.1,207.3,208.6,216.4,233.0,247.2,258.1,254.8,247.2,238.8,230.1,222.8,216.3,214.6,211.0,205.1,195.6,186.3]) # K

h_100 = np.array([0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100])


# R = 287.05
# P = rho * R * T

# density model:
deg = 16
p = np.polyfit(h, rho, deg)
# print(p)

x = np.linspace(0, 300, 100)
rfun = 0
for i in range(deg + 1): rfun += p[i] * x**(deg - i)
rfun = (rfun**2)**0.5
# print(rfun)

# plt.grid(color='lavender')
# plt.plot(h, rho)
# plt.plot(x, rfun)
# plt.xlabel('altitude (km)')
# plt.ylabel('density (kg/m^3)')
# plt.legend(['NRLMSIS2', 'fun'])
# plt.show()


# pressure model:
# deg = 18
# p = np.polyfit(h, P, deg)
# # print(p)

# x = np.linspace(0, 300, 100)
# pfun = 0
# for i in range(deg + 1): pfun += p[i] * x**(deg - i)
# pfun = (pfun**2)**0.5
# print(pfun)

# plt.grid(color='lavender')
# plt.plot(h, P)
# plt.plot(x, pfun)
# plt.xlabel('altitude (km)')
# plt.ylabel('pressure (Pa)')
# plt.legend(['NRLMSIS2', 'fun'])
# plt.show()



# temperature model:
deg = 20
p = np.polyfit(h_100, T_100, deg)
# print(p)

x = np.linspace(0, 100, 100)
tfun = 0
for i in range(deg + 1): tfun += p[i] * x**(deg - i)
# tfun = (tfun**2)**0.5
# print(tfun)


# tfun = pfun / (R * rfun)
plt.grid(color='lavender')
plt.plot(h_100, T_100)
plt.plot(x, tfun)
plt.xlabel('altitude (km)')
plt.ylabel('temperature (K)')
plt.legend(['NRLMSIS2', 'fun'])
plt.show()