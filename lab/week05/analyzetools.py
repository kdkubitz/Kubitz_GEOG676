import arcpy

arcpy.management.AnalyzeToolsForPro("C:\Users\kkubitz\OneDrive - City of Georgetown\Documents\GitHub\Kubitz_GEOG676\lab\week05\lab5.pyt",
"C:/DevSource/analyze_report.txt")

print(arcpy.GetMessages(1))
