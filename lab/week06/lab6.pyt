import arcpy, time

class Toolbox(object):
    def __init__(self):
        # Define the toolbox (the name of the toolbox is the name of the .pyt file).
        self.label = "Toolbox"
        self.alias = ""
        self.tools = [GreenMaker]

class GreenMaker(object):
    def __init__(self):
        # Define the tool (tool name is the name of the class).
        self.label = "GreenMaker"
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
            displayName="Field on which to calculate Graduations",
            name="symbologyName",
            datatype="Field",
            parameterType="Required",
            direction="Input"
        ) 
        params = [param0, param1]
        return params

    def updateMessages(self, parameters):
        # Modify the messages created by internal validation for each tool
        # parameter.  This method is called after internal validation.
        return

    def execute(self, parameters, messages):
        # The source code of the tool.
        readTime = 2
        start = 0
        max = 100
        step = 33

        # Progressor Step 1
        arcpy.SetProgressor("step", "Initializing...", start, max, step)
        time.sleep(readTime)
        arcpy.AddMessage("Initializing...")

        # Reference to our .aprx
        project = arcpy.mp.ArcGISProject("CURRENT")

        # Grab the first map in the .aprx
        currentmap = project.listMaps('Map')[0]

        # Progressor Step 2
        arcpy.SetProgressorPosition(start + step)
        arcpy.SetProgressorLabel("Searching for Layer...")
        time.sleep(readTime)
        arcpy.AddMessage("Searching for Layer")

        # Loop through available layers in the map
        for layer in currentmap.listLayers():
        
            # Check if layer is a feature layer
            if layer.isFeatureLayer:

                # Obtain a copy of the layer's symbology
                symbology = layer.symbology

                # Check if it has a 'renderer' attribute
                if hasattr(symbology, 'renderer'):

                    # Check if the layer's name is User Input
                    if layer.name == parameters[0].valueAsText:

                        # Progressor Step 3
                        arcpy.SetProgressorPosition(start + step*2)
                        arcpy.SetProgressorLabel("Classifying...")
                        time.sleep(readTime)
                        arcpy.AddMessage("Classifying...")

                        # Update the copy's renderer to be 'GraduatedColorsRenderer'
                        symbology.updateRenderer('GraduatedColorsRenderer')

                        # Tell arcpy which field we want to base our choropleth off of
                        symbology.renderer.classificationField = parameters[1].valueAsText

                        # Set how many classes we'll have 
                        symbology.renderer.breakCount = 5

                        # Set the color ramp
                        symbology.renderer.colorRamp = project.listColorRamps('Greens (5 Classes)')[0]

                        # Set the layer's actual symbology equal to the copy's
                        layer.symbology = symbology 

                    else:
                        print("NOT Valid Layer")

            # Progressor Step 4
            arcpy.SetProgressorPosition(start + step*3)
            arcpy.SetProgressorLabel("Finishing...")
            time.sleep(readTime)
            arcpy.AddMessage("Finishing...")

            project.save()
            return
