import arcpy
import os

class Toolbox(object):
    def __init__(self):
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [Converter]

class Converter(object):
    def __init__(self):
        self.label = "KML to Feature Class"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Input KML
        param0 = arcpy.Parameter(
            displayName="Input KML",
            name="in_kml",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
        )
        # Output Feature Class Name
        param1 = arcpy.Parameter(
            displayName="Output Feature Class",
            name="out_feature",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        # Output GDB
        param2 = arcpy.Parameter(
            displayName="Output GDB",
            name="out_gdb",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        ) 
        params = [param0, param1, param2]
        return params

    def execute(self, parameters, messages):
        try: 
            project = arcpy.mp.ArcGISProject("CURRENT")
            current_map = project.listMaps('Map')[0]

            in_kml = parameters[0]
            out_name = parameters[1]
            out_gdb = parameters[2]

            arcpy.KMLToLayer_conversion(in_kml, os.path.dirname(out_gdb), out_name)

            current_map.addDataFromPath(out_name)

            project.save()
        
        except Exception as e:
            messages.addErrorMessage(f"An error occurred: {e}")

