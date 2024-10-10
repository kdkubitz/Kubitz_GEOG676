import arcpy
import arcpy.conversion
import arcpy.management

class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [CNIM]

class CNIM(object):
    def __init__(self):
        self.label = "CNIM"
        self.description = "Automates the Customers Not In Model Process in Milsoft WindMil."
        self.canRunInBackground = False

    def getParameterInfo(self):
        param0 = arcpy.Parameter(
            displayName="Input CSV Table",
            name="input_table",
            datatype=["DETable", "DEFile"],
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="CIS Service Info Layer",
            name="cis_layer",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Name of Output Shapefile",
            name="output_shapefile",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Name of Output CSV",
            name="output_csv",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param4 = arcpy.Parameter(
            displayName="Output Folder",
            name="output_folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        )

        params = [param0, param1, param2, param3, param4]

        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        try: 
            # Define project, map, input table
            gdb = "C:/Users/kkubitz/OneDrive - City of Georgetown/Documents/ArcGIS/Projects/676_Final_CNIM/676_Final_CNIM.gdb"
            project = arcpy.mp.ArcGISProject("CURRENT")
            current_map = project.listMaps('Map')[0]
            in_table = parameters[0].valueAsText
            

            # Add input table to project
            gdb_table_result = arcpy.TableToGeodatabase_conversion(in_table, gdb)
            gdb_table = gdb_table_result.getOutput(0)
            current_map.addDataFromPath(gdb_table)

            # Add CIS layer to project
            sde = "C:/Users/kkubitz/OneDrive - City of Georgetown/Documents/ArcGIS/Projects/676_Final_CNIM/Editor.sde"
            in_feature = parameters[1].valueAsText
            CIS = {sde}/{in_feature}
            # CIS = arcpy.MakeFeatureLayer_management(in_feature, "CIS_layer")

            # Conduct join on CIS feature class
            arcpy.env.qualifiedFieldNames = False
            CIS_join_field = "Service ID"
            table_join_field = "ServLoc"
            join_output = arcpy.management.AddJoin(CIS, CIS_join_field, gdb_table, table_join_field)

            # Perform selection on resulting joined table
            selection_query = "ServLoc IS NOT NULL"
            arcpy.management.SelectLayerByAttribute(join_output, "NEW SELECTION", selection_query)

            # Export results to shapefile
            out_feature = parameters[2].valueAsText
            result = arcpy.management.CopyFeatures(join_output, out_feature)

            # Add new shapefile to map
            # current_map.addDataFromPath(out_feature)

            # Calculate Geometry 
            lat_field = "Latitude"
            long_field = "Longitude"
            arcpy.management.CalculateGeometryAttributes(result, [
                [lat_field, "POINT_Y"],
                [long_field, "POINT_X"]
            ])

            # Export new table as .csv
            out_table = parameters[3].valueAsText
            out_folder = parameters[4].valueAsText
            arcpy.conversion.TableToTable(out_feature, out_folder, out_table)

            project.save()
        
        except arcpy.ExecuteError:
            messages.addErrorMEssage(f"ArcPy error: {arcpy.GetMessages(2)}")

        return
 