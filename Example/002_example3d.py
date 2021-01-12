from gaiaup import seismic3d, wavefield3d
import numpy as np
xmax = 2100.0  # x - model width (m)
ymax = 4400.0  # y - model width (m)
zmax = 1000.0  # z - model width (m)
tmax = 1.2     # recording time (s)
t0   = 0.1     # source time shift (s)
xsrc = 1050.0   # x-source location (m)
ysrc = 2200.0   # y-source location (m)
zsrc = 20.0   # z-source location (m)
dx   = 5.0     # x-grid  interval (m)
dy   = dx      # y-grid  interval (m)
dz   = dx      # z-grid  interval (m)
sr   = 4       # acquisition sampling rate in msec
f0   = 60.0    # centre frequency of the source wavelet (Hz)
recint = 25    # receiver interval (m)
sourceline_int = 300  # source line interval (m)
buff = 300  # buffer zone (m)
savewf = 1  #save wavefield 1=YES 0=NO

nx = int(xmax / dx)  # number of grid points in x-direction
ny = int(ymax / dy)  # number of grid points in y-direction
nz = int(zmax / dz)  # number of grid points in z-direction

model = np.ones((nx,ny,nz))*2000 # # LAYER  1
model[0:nx, 0:ny, 50:100]  = np.ones((nx, ny, 50)) * 3000  # LAYER  2
model[0:nx, 0:ny, 100:150] = np.ones((nx, ny, 50)) * 2500  # LAYER  3
model[0:nx, 0:ny, 150:200] = np.ones((nx, ny, 50)) * 4500  # LAYER  4

path = '/home/dickyaz/TEMP3D' #path for storing results
np.save('%s/velocity'% path, model)

# wavefield only
# wavefield3d(xmax, ymax, zmax, dx, dy, dz, xsrc, ysrc, zsrc, tmax, t0, sr, f0, model, path, buff)

#shot and/or wavefield
seismic3d(xmax, ymax, zmax, dx, dy, dz, xsrc, ysrc, zsrc, tmax, t0, sr, f0, model, path, recint, sourceline_int, buff, savewf)