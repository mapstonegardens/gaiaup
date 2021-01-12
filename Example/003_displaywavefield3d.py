import pyvista as pv
import numpy as np


i = 190
values = np.load('/home/dickyaz/TEMP3D/wavefield_%s.npy'%i )
values = values[:,:,::-1] #upside-down

vs = values.shape

slice = values[:,int(vs[1]/2),:]
vmin = np.min(slice)
vmax = np.max(slice)


grid = pv.UniformGrid()
grid.dimensions = values.shape
grid.origin = (0, 0, 0)  # The bottom left corner of the data set
grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis
grid.point_arrays["Amplitudes"] = values.flatten(order="F")  # Flatten the array!
slices1 = grid.slice_orthogonal(x=int(vs[0]/2), y=int(vs[1]/2), z=int(vs[2]/2))


values = np.load('/home/agus/TEMP3D/velocity.npy')
values = values[:,:,::-1] #upside-down
grid = pv.UniformGrid()
grid.dimensions = values.shape
grid.origin = (0, 0, 0)  # The bottom left corner of the data set
grid.spacing = (1, 1, 1)  # These are the cell sizes along each axis
grid.point_arrays["Velocity"] = values.flatten(order="F")  # Flatten the array!
slices2 = grid.slice_orthogonal(x=int(vs[0]/2), y=int(vs[1]/2), z=int(vs[2]/2))

p = pv.Plotter()
sc = 0.2

sargs = dict(height=np.nan, vertical=True, position_x=np.nan, position_y=np.nan)
p.add_mesh(slices1,cmap='Greys', opacity=0.96, clim=[sc*vmin, sc*vmax], scalar_bar_args=sargs)

sargs = dict(height=0.25, vertical=True, position_x=0.05, position_y=0.05)
p.add_mesh(slices2,cmap='jet', opacity=0.96, clim=[1000, 5000], scalar_bar_args=sargs)
p.set_background('black', top=None)
p.show()



