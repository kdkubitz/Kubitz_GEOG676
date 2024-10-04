import arcpy
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
        # input .xlsx table (is it possible to use .slk?)
        param0 = arcpy.Parameter(
        displayName="Input CSV Table",
        name="inputTable",
        datatype="DETable",
        parameterType="Required",
        direction="Input"
        )
        param1 = arcpy.Parameter(
        displayName="CIS Service Info Layer",
        name="CISLayer",
        datatype="GPLayer",
        parameterType="Required",
        direction="Input"
        )

        params = [param0, param1]
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
    
        # Take input table, add to project
        current_map.addTable(input_table)
        
        # Conduct join on CIS feature class
        CIS_join_field = "Service ID"
        table_join_field = "ServLoc"
        arcpy.management.AddJoin(CIS, CIS_join_field, input_table, table_join_field)

        # Perform Select by Attributes on resulting joined table

        # Export results to shapefile, add to project

        # Calculate Geometry on Lat / Long (is it possible to swap fields?)

        # Export new table as .csv

        project.save()
        return
 