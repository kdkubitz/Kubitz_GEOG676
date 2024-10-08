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
        # define project, map, input table
        project = arcpy.mp.ArcGISProject("CURRENT")
        current_map = project.listMaps('Map')[0]
        input_table = parameters[0].valueAsText
        CIS = parameters[1].valueAsText

        try: 
            # Add input table to project
            current_map.addDataFromPath(input_table)

            # Conduct join on CIS feature class
            CIS_join_field = "Service ID"
            table_join_field = "ServLoc"
            join_output = "in_memory\\CIS_join"
            arcpy.management.AddJoin(CIS, CIS_join_field, input_table, table_join_field)

            # Perform Select by Attributes on resulting joined table
            selection_query = "ServLoc IS NOT NULL"
            arcpy.management.SelectLayerByAttribute(join_output, "NEW SELECTION", selection_query)

            # Export results to shapefile
            output_shapefile = parameters[2].valueAsText
            arcpy.management.CopyFeatures(join_output, output_shapefile)

            # Add new shapefile to map
            current_map.addDataFromPath(output_shapefile)

            # Calculate Geometry on Lat / Long (is it possible to swap fields?)
            lat_field = "Latitude"
            long_field = "Longitude"
            arcpy.management.CalculateGeometryAttributes(output_shapefile, [
                [lat_field, "POINT_Y"],
                [long_field, "POINT_X"]
            ])

            # Export new table as .csv
            csv_output = parameters[3].valueAsText
            arcpy.conversion.TableToTable(output_shapefile, "placeholder directory", csv_output)

            # Clean up in-memory data
            arcpy.management.Delete(join_output)

            project.save()
        
        except Exception as e:
            messages.addErrorMessage(f"An error occurred: {e}")

        return
 