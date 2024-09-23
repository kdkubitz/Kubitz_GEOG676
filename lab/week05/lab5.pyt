import arcpy
arcpy.env.workspace = "C:/DevSource/676_L4/676_L4.gdb"

class Toolbox(object):
    def __init__(self):
        # Define the toolbox (the name of the toolbox is the name of the .pyt file). 
        self.label = "Custom"
        self.alias = ""

        # List of tool classes associated with this toolbox
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
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        param1 = arcpy.Parameter(
            displayName="GDB Title",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        param2 = arcpy.Parameter(
            displayName="Garage Data",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        param3 = arcpy.Parameter(
            displayName="Garage Layer Name",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        param4 = arcpy.Parameter(
            displayName="Campus GDB",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        param5 = arcpy.Parameter(
            displayName="Buffer Radius",
            name="bufferRadius",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"   )
        params = [param0, param1, param2, param3, param4, param5]
        return [params]
    
    def isLicensed(self):
        # Set whether the tool is licensed to execute.
        return True

    def updateParameters(self, parameters):
        # Modify the values and properties of parameters before internal validation is performed.  
        # This method is called whenever a parameter has been changed. 
        return

    def updateMessages(self, parameters):
        # Modify the messages created by internal validation for each tool parameter. 
        # This method is called after internal validation.
        return

    def execute(self, parameters, messages):
        # The source code of the tool.
        grgsGDB = "C:/DevSource/676_L4/Garages.gdb"
        spatial_ref = arcpy.SpatialReference(6343) # UTM Zone 14N

        # Gathering Buffer Distance from Parameters
        buffer_distance = parameters[0].valueAsText

        # Projecting to Meters
        arcpy.Project_management(grgsGDB + "/grgs", grgsGDB + "/grgs_proj", spatial_ref)

        # Creating a Buffer
        arcpy.Buffer_analysis(grgsGDB + "/grgs_proj", grgsGDB + "/grgs_buff", buffer_distance)

        # Creating an Intersection
        arcpy.Intersect_analysis([grgsGDB + "/grgs_buff", grgsGDB + "/Structures"], grgsGDB + "/intersect", "ALL")

        return "Success!"
    