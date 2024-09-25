import arcpy

class Toolbox(object):
    def __init__(self):
        # Define the toolbox (the name of the toolbox is the name of the .pyt file). 
        self.label = "Toolbox"
        self.alias = "PythonToolbox"
        self.tools = [GarageProximity]

class GarageProximity(object):
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = "GarageProximity"
        self.description = "Determines which buildings on TAMU Campus are within a specified distance of a parking garage."
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define parameter definitions.
        param0 = arcpy.Parameter(
            displayName="GDB Folder",
            name="GDBfolder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
            )
        param1 = arcpy.Parameter(
            displayName="GDB Title",
            name="GDBtitle",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
            )
        param2 = arcpy.Parameter(
            displayName="Garage Data File",
            name="garageData",
            datatype="DEFile",
            parameterType="Required",
            direction="Input"
            )
        param3 = arcpy.Parameter(
            displayName="Name of Garage Layer",
            name="garageLayer",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
            )
        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="campusGDB",
            datatype="DEfolder",
            parameterType="Required",
            direction="Input"
            )
        param5 = arcpy.Parameter(
            displayName="Buffer Radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
            )
        return [param0, param1, param2, param3, param4, param5]

    def execute(self, parameters, messages):
        # The source code of the tool.
        arcpy.env.workspace = parameters[0].valueAsText
        grgsGDB = parameters[1].valueAsText

        # Gathering Buffer Distance from Parameters
        buffer_distance = parameters[5].valueAsText

        # Projecting to Meters
        arcpy.Project_management(grgsGDB + "/grgs", grgsGDB + "/grgs_proj", arcpy.SpatialReference(6343))

        # Creating a Buffer
        arcpy.Buffer_analysis(grgsGDB + "/grgs_proj", grgsGDB + "/grgs_buff", buffer_distance)

        # Creating an Intersection
        arcpy.Intersect_analysis([grgsGDB + "/grgs_buff", grgsGDB + "/Structures"], grgsGDB + "/intersect", "ALL")

        # Add Data to Map
        aprx = arcpy.mp.ArcGISProject("CURRENT")
        map = aprx.listMaps()[0]
        buff = r"C:/DevSource/676_L4/Garages.gdb/grgs_buff"
        inter = r"C:/DevSource/676_L4/Garages.gdb/intersect"
        map.addDataFromPath(buff)
        map.addDataFromPath(inter)
