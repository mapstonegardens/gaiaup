import numpy as np
import matplotlib.pyplot as plt

data = np.load('/home/agus/TEMP3D/shot3d.npy')


shot = []
for i in range(5):
    shot.extend(data[i,:,:].T)

shot = np.asarray(shot).T
shot = shot[:, :]
rmstr = shot[:, int(shot.shape[1] / 3):int(shot.shape[1] / 2)]
rms = np.std(rmstr - rmstr.mean(axis=0))

scale = 1

plt.suptitle('3D SHOT RECORD')
plt.imshow(shot, interpolation='bilinear', cmap='bwr', aspect='auto',  vmin=-rms*scale, vmax = rms*scale)
plt.show()

