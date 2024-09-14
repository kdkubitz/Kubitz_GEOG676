import arcpy
arcpy.env.workspace = "C:/DevSource/676_L4/676_L4.gdb"


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
                print(X, Y)



# garages_path = "C:/DevSource/676_L4"
# arcpy.CreateFileGDB_management(garages_path, "Garages.gdb")
