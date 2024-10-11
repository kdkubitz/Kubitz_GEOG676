import arcpy, os

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
            displayName="Input Table",
            name="in_table",
            datatype="DETable",
            parameterType="Required",
            direction="Input"
        )

        param1 = arcpy.Parameter(
            displayName="CIS Service Info Layer",
            name="in_layer",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        )

        param2 = arcpy.Parameter(
            displayName="Name of Output Shapefile",
            name="out_shp_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param3 = arcpy.Parameter(
            displayName="Name of Output CSV",
            name="out_csv_name",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )

        param4 = arcpy.Parameter(
            displayName="Output Folder",
            name="out_folder",
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
            # Define project, map 
            p = arcpy.mp.ArcGISProject("CURRENT")
            m = p.listMaps('Map')[0]

            # Define inputs 
            in_table = parameters[0].valueAsText
            in_layer = parameters[1].valueAsText
            out_folder = parameters[4].valueAsText
            out_shp = os.path.join(out_folder, parameters[2].valueAsText + ".shp")
            out_csv = os.path.join(out_folder, parameters[3].valueAsText + ".csv")

            # Remove existing joins
            arcpy.management.RemoveJoin(in_layer)

            # Make a table view of the CIS layer's attribute table
            layer_table_view = "in_memory\\layer_table"
            arcpy.management.MakeTableView(in_layer, layer_table_view)

            # Perform the join
            joined_table = arcpy.management.AddJoin(layer_table_view, "Service ID", in_table, "ServLoc")

            # Select by attribute
            selection_query = "ServLoc IS NOT NULL"
            selected_rows = arcpy.management.SelectLayerByAttribute(joined_table, "NEW SELECTION", selection_query)

            # Export selection to shapefile
            arcpy.management.CopyFeatures(selected_rows, out_shp)

            # Add shapefile to map
            m.addDataFromPath(out_shp)

            # Calculate Geometry 
            arcpy.management.CalculateGeometryAttributes(out_shp, [["Latitude", "POINT_Y"], ["Longitude", "POINT_X"]])

            # Export table to CSV
            arcpy.conversion.TableToTable(out_shp, out_folder, out_csv)

            p.save()
        
        except arcpy.ExecuteError:
            messages.addErrorMessage(f"ArcPy error: {arcpy.GetMessages(2)}")

        return
 