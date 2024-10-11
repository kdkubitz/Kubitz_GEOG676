import arcpy, time

class Toolbox(object):
    def __init__(self):
        self.label = "Buffer Toolbox"
        self.alias = "buffer_toolbox"
        self.tools = [BufferTool]

class BufferTool(object):
    def __init__(self):
        self.label = "Buffer Creation Tool"
        self.description = "Creates a buffer around the input layer."
        self.canRunInBackground = False

    def getParameterInfo(self):

        # Input Layer
        param0 = arcpy.Parameter(
            displayName="Input Layer",
            name="input_layer",
            datatype="GPFeatureLayer",
            parameterType="Required",
            direction="Input"
        )

        # Buffer Distance
        param1 = arcpy.Parameter(
            displayName="Buffer Distance",
            name="buffer_distance",
            datatype="GPDouble",
            parameterType="Required",
            direction="Input"
        )
        
        # Buffer Units
        param2 = arcpy.Parameter(
            displayName="Buffer Units",
            name="buffer_units",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        param2.filter.type = "ValueList"
        param2.filter.list = ["Meters", "Kilometers", "Feet", "Miles"]

        # Output Layer
        param3 = arcpy.Parameter(
            displayName="Output Layer",
            name="output_layer",
            datatype="DEFeatureClass",
            parameterType="Required",
            direction="Output"
        )
        
        params = [param0, param1, param2, param3]
        return params

    def isLicensed(self):
        return True

    def execute(self, parameters, messages):

        # Define inputs
        in_layer = parameters[0].valueAsText
        buff_dist = parameters[1].valueAsText
        buff_unit = parameters[2].valueAsText
        out_layer = parameters[3].valueAsText

        try:
            arcpy.SetProgressor("step", "Initializing...", 0, 100, 33)

            # Progressor Step 1
            arcpy.AddMessage("Initializing...")
            arcpy.SetProgressorPosition(33)

            # Create buffer 
            arcpy.analysis.Buffer(in_layer, out_layer, f"{buff_dist} {buff_unit}")
            
            # Progressor Step 2
            arcpy.SetProgressorLabel("Adding Buffer...")
            arcpy.SetProgressorPosition(66)

        except arcpy.ExecuteError as e:
            messages.addErrorMessage(f"ArcPy error: {arcpy.GetMessages(2)}")

        except Exception as e:
            messages.addErrorMessage(f"An error occurred: {e}")

        else:
            arcpy.AddMessage("Process completed successfully.")
            
        finally:
            # Progressor Step 3
            arcpy.SetProgressorLabel("Finalizing...")
            arcpy.SetProgressorPosition(100)

        return
