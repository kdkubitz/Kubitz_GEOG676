import arcpy
arcpy.env.workspace = "C:/DevSource/676_L4/676_L4.gdb"

# Reading Text File
with open("C:/DevSource/Kubitz_GEOG676/lab/week04/garages.csv", "r") as file:
        for line in file:
                lines = line.strip().split(",")
                OID = lines[0]
                CIT_CODE = lines[1]
                FAC_CODE = lines[2]
                LotName = lines[3]
                AggieMap = lines[4]
                Name = lines[5]
                LotType = lines[6]
                ORIG_FID = lines[7]
                X = lines[8]
                Y = lines[9]
                # print(X, Y)

        # Creating a GDB
        # garages_path = "C:/DevSource/676_L4"
        # arcpy.CreateFileGDB_management(garages_path, "Garages.gdb")
        # Adding Coordinate Layer
        # garages = arcpy.management.MakeXYEventLayer("C:/DevSource/Kubitz_GEOG676/lab/week04/garages.csv", "X", "Y", "grgs")
        # arcpy.FeatureClassToGeodatabase_conversion(garages, "C:/DevSource/676_L4/Garages.gdb")

grgsGDB = "C:/DevSource/676_L4/Garages.gdb"

# Creating a Buffer
buffer_distance = float(input("Please enter the buffer distance in meters: ")) # User Input for Buffer
spatial_ref = arcpy.SpatialReference(6343) # UTM Zone 14N
arcpy.Project_management(grgsGDB + "/grgs", grgsGDB + "/grgs_proj", spatial_ref) # Projecting to Meters
arcpy.Buffer_analysis(grgsGDB + "/grgs_proj", grgsGDB + "/grgs_buff", buffer_distance)

# Creating an Intersection
arcpy.Intersect_analysis([grgsGDB + "/grgs_buff", grgsGDB + "/Structures"], grgsGDB + "/intersect", "ALL")

# Outputting the Intersection Table
arcpy.TableToTable_conversion(grgsGDB + "/intersect.dbf", "C:/DevSource/676_L4", "L4_intersect.csv")

