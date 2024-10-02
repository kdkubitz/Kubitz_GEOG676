import arcpy

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
        # 0 = input .xlsx table (is it possible to use .slk?)
        params = None
        return params

    def isLicensed(self):
        return True

    def updateParameters(self, parameters):
        return

    def updateMessages(self, parameters):
        return

    def execute(self, parameters, messages):
        # Take input table, add to project
        
        # Conduct join on Customers feature class

        # Perform Select by Attributes on resulting joined table

        # Export results to shapefile, add to project

        # Calculate Geometry on Lat / Long (is it possible to swap fields?)

        # Export new table as .csv
        
        return
