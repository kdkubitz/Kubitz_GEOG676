import arcpy

class Toolbox(object):
    def __init__(self):
        # Define the toolbox (the name of the toolbox is the name of the .pyt file).
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [OrangeMaker]

class OrangeMaker(object):
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = "OrangeMaker"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        # Define parameter definitions
        param0 = arcpy.Parameter(
            displayName="Input Layer",
            name="inputLayer",
            datatype="GPLayer",
            parameterType="Required",
            direction="Input"
        ) 
        param1 = arcpy.Parameter(
            displayName="Field on which to base Symbology",
            name="symbologyName",
            datatype="Field",
            parameterType="Required",
            direction="Input"
        ) 
        params = [param0, param1]
        return params

    #def updateParameters(self, parameters):
        # Modify the values and properties of parameters before internal
        # validation is performed.  This method is called whenever a parameter
        # has been changed.
    #    return

    #def updateMessages(self, parameters):
        # Modify the messages created by internal validation for each tool
        # parameter.  This method is called after internal validation.
    #    return

    def execute(self, parameters, messages):
        # The source code of the tool.
        # Reference to our .aprx
        project = arcpy.mp.ArcGISProject("CURRENT")
        currentgdb = "C:/DevSource/676_L4"

        # Grab the first map in the .aprx
        currentmap = project.listMaps('Map')[0]

        # Loop through available layers in the map
        for layer in currentmap.listLayers():
        
            # Check if layer is a feature layer
            if layer.isFeatureLayer:

                # Obtain a copy of the layer's symbology
                symbology = layer.symbology

                # Check if it has a 'renderer' attribute
                if hasattr(symbology, 'renderer'):

                    # Check if the layer's name is User Input
                    if layer.name == parameters[1]:

                        # Update the copy's renderer to be 'GraduatedColorsRenderer'
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        # Tell arcpy which field we want to base our choropleth off of
                        symbology.renderer.classificationField = parameters[2]

                        # Set how many classes we'll have 
                        symbology.renderer.breakCount = 5

                        # Set the color ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Oranges (5 Classes)')[0]

                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology 

                    else:
                        print("NOT Valid Layer")
            
            project.saveACopy(currentgdb + "/copy")

