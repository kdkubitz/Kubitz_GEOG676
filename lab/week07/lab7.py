import arcpy

# Definitions
source = r"D:/DevSource/Tamu/GeoInnovation/_GISProgramming/data/modules/28/LS7/"
band1 = arcpy.sa.Raster(source + "B1.TIF") # blue
band2 = arcpy.sa.Raster(source + "B2.TIF") # green
band3 = arcpy.sa.Raster(source + "B3.TIF") # red
band4 = arcpy.sa.Raster(source + "B4.TIF") # NIR

# Composite
composite = arcpy.CompositeBands_management([band1, band2, band3, band4], source + "combined.tif")

# NDVI
esri_ndvi = ((band4 - band3) / (band4 + band3)) * 100 + 100
esri_ndvi.save(source + "esri_ndvi.tif")
ndvi = ((band4 - band3) / (band4 + band3))
ndvi.save(source + "ndvi.tif")

# Hillshade
import arcpy
gdb = "c:/Users/aaron/documents/ArcGIS/Projects/Mod27/Mod27.gdb"
azimuth = 315
altitude = 45
shadows = "NO_SHADOWS"
z_factor = 1
arcpy.ddd.HillShade(gdb + "/tx_dem", gdb + "/tx_hillshade", azimuth, altitude, shadows, z_factor)

# Slope
import arcpy
gdb = "c:/Users/aaron/documents/ArcGIS/Projects/Mod27/Mod27.gdb"
output_measurement = "DEGREE"
z_factor = 1
method = "PLANAR"
z_unit = "METER"
arcpy.ddd.Slope(gdb + "/tx_dem", gdb + "/tx_dem_slopes", output_measurement, z_factor, method, z_unit)
