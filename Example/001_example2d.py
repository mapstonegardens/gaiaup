from gaiaup import seismic2d
import numpy as np
import matplotlib.pyplot as plt

xmax = 2100.0  # x - model width (m)
zmax = 1000.0  # z - model width (m)
tmax = 1.2     # recording time (s)
t0   = 0.1     # source time shift (s)
xsrc = 1050.0   # x-source location (m)
zsrc = 20.0    # z-source location (m)
dx   = 5.0     # x-grid  interval (m)
dz   = dx      # z-grid  interval (m)
sr   = 4       # acquisition sampling rate in msec
f0   = 60.0    # centre frequency of the source wavelet (Hz)
recint = 25    # receiver interval (m)
buff = 300     # buffer zone (m)
savewf = 1     # save wavefield 1=YES 0=NO

nx = int(xmax / dx)  # number of grid points in x-direction
nz = int(zmax / dz)  # number of grid points in z-direction

model = np.ones((nx,nz))*2000 # # LAYER  1
model[0:nx, 50:100]  = np.ones((nx, 50)) * 3000  # LAYER  2
model[0:nx, 100:150] = np.ones((nx, 50)) * 2500  # LAYER  3
model[0:nx, 150:200] = np.ones((nx, 50)) * 4500  # LAYER  4


path = '/home/dickyaz/TEMP2D' #path for storing results
np.save('%s/velocity'% path, model)


seismic2d(xmax, zmax, dx, dz, xsrc, zsrc, tmax, t0, sr, f0, model, path, recint, buff, savewf)

shot = np.load('%s/shot2d.npy' % path)
plt.imshow(shot[15:None,:], aspect='auto', interpolation='bilinear', cmap='bwr', vmin=-0.0000001, vmax=0.0000001)
plt.suptitle('2D SHOT RECORD')
plt.show()

fig = plt.figure(figsize=(7, 7))
plt.tight_layout()
extent = [0.0, xmax, zmax, 0.0]
vel = np.load('%s/velocity.npy' % path)
plt.imshow(vel.T, cmap='jet', interpolation='bilinear', extent=extent, alpha=1)
p = np.zeros((nx, nz))
image = plt.imshow(p.T, animated=True, cmap="Greys", extent=extent, interpolation='bilinear', vmin=-0.000001, vmax=0.000001,alpha=0.5)
plt.title('2D Wavefield')
plt.xlabel('x [m]')
plt.ylabel('z [m]')
plt.ion()
plt.show(block=False)

for i in range(300):
    p = np.load('%s/wavefield_%s.npy' % (path, int(i+1)))
    image.set_data(p.T)
    fig.canvas.draw()
