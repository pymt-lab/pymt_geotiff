"""An example of running the babelized GeoTiff library through its BMI."""

import numpy as np

from pymt_geotiff import GeoTiff

config_file = "bmi-geotiff.yaml"


# Instatiate and initialize the model.
m = GeoTiff()
print(m.get_component_name())
m.initialize(config_file)

# List the model's exchange items.
print("Number of input vars:", m.get_input_item_count())
for var in m.get_input_var_names():
    print(" - {}".format(var))
print("Number of output vars:", m.get_output_item_count())
for var in m.get_output_var_names():
    print(" - {}".format(var))

# Get info about the raster variable, including its grid id.
var_name = "gis__raster_data"
print("Variable: {}".format(var_name))
print(" - variable type:", m.get_var_type(var_name))
print(" - units:", m.get_var_units(var_name))
print(" - itemsize:", m.get_var_itemsize(var_name))
print(" - nbytes:", m.get_var_nbytes(var_name))
grid_id = m.get_var_grid(var_name)
print(" - grid id:", grid_id)

# Get grid info for the variable.
print(" - grid type:", m.get_grid_type(grid_id))
grid_rank = m.get_grid_rank(grid_id)
print(" - rank:", grid_rank)
grid_shape = np.empty(grid_rank, dtype=np.int32)
m.get_grid_shape(grid_id, grid_shape)
print(" - shape:", grid_shape)
grid_size = m.get_grid_size(grid_id)
print(" - size:", grid_size)
grid_x = np.empty(grid_shape[-1], dtype=float)
m.get_grid_x(grid_id, grid_x)
print(" - x:", grid_x[0:5])
grid_y = np.empty(grid_shape[-2], dtype=float)
m.get_grid_y(grid_id, grid_y)
print(" - y:", grid_y[0:5])

# Get time information from the model.
print("Start time:", m.get_start_time())
print("End time:", m.get_end_time())
print("Current time:", m.get_current_time())
print("Time step:", m.get_time_step())
print("Time units:", m.get_time_units())

# Get the initial variable values.
val = np.empty(grid_size, dtype=float)
m.get_value(var_name, val)
print(" - initial values (gridded):")
print(val.reshape(np.roll(grid_shape, 1)))

# Finalize the model.
m.finalize()
print("Done!")
