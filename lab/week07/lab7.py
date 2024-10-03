import arcpy

# Definitions
source = "C:/DevSource/676_L7"
gdb = "C:/DevSource/676_L7/676_L7.gdb"
band1 = arcpy.sa.Raster(source + "/band1.TIF") # blue
band2 = arcpy.sa.Raster(source + "/band2.TIF") # green
band3 = arcpy.sa.Raster(source + "/band3.TIF") # red
band4 = arcpy.sa.Raster(source + "/band4.TIF") # NIR

# Composite
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "/combined.tif")

# Hillshade
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(source + "/DEM.tif", gdb + "/tx_hillshade", azimuth, altitude, shadows, z_factor)

# Slope
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(source + "/DEM.tif", gdb + "/tx_dem_slopes", output_measurement, z_factor, method, z_unit)

print("Success!")
