from Autodesk.Revit import DB
doc = __revit__.ActiveUIDocument.Document
projectInfo = doc.ProjectInformation
message = "Project information:"
message += "\nName: " + projectInfo.Name
message += "\nNumber: " + projectInfo.Number
message += "\nStatus: " + projectInfo.Status
message += "\nAddress: " + projectInfo.Address
message += "\nClient Name: " + projectInfo.ClientName
print(message)