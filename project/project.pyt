import arcpy, os

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
            displayName="Output File Name",
            name="out_feature",
            datatype="GPString",
            parameterType="Required",
            direction="Input"
        )
        # Output Folder
        param2 = arcpy.Parameter(
            displayName="Output Folder",
            name="out_folder",
            datatype="DEFolder",
            parameterType="Required",
            direction="Input"
        ) 
        params = [param0, param1, param2]
        return params

    def execute(self, parameters, messages):
        try: 
            arcpy.ResetEnvironments()
            project = arcpy.mp.ArcGISProject("CURRENT")
            current_map = project.listMaps('Map')[0]

            in_kml = parameters[0].valueAsText
            out_name = parameters[1].valueAsText
            out_folder = parameters[2].valueAsText

            arcpy.KMLToLayer_conversion(in_kml, out_folder, out_name)
            
            out_feature = os.path.join(out_folder, out_name, "Placemarks")
            out_path = r"{}".format(out_feature)

            arcpy.MakeFeatureLayer_management(out_path, "temp_layer")
            current_map.addLayer(arcpy.mp.Layer("temp_layer"))

            project.save()
        
        except arcpy.ExecuteError:
            messages.addErrorMessage(f"ArcPy error: {arcpy.GetMessages(2)}")
        
        return None
