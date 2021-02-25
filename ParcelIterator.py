import arcpy

###Define parameters###
Layer_Name=arcpy.GetParameterAsText(0)
Input_FromH=arcpy.GetParameter(1)
Input_Height=arcpy.GetParameter(2)
Gap=arcpy.GetParameter(3)
Input_NumOfLevels=arcpy.GetParameter(4)

###Validate input###
#arcpy.AddMessage(Layer_Name)
#arcpy.AddMessage(Input_FromH)
#arcpy.AddMessage(Input_Height)
#arcpy.AddMessage(Input_NumOfLevels)
#arcpy.AddMessage(Gap)

###Variables for script###
fields = ["SHAPE@","FromH","ToH","Height", "Level", "Row"]
Input_ToH=Input_FromH+Input_Height

###Update existing rows according to input###
with arcpy.da.UpdateCursor(Layer_Name, fields) as Ucursor:
    for row in Ucursor:
        row[1]=Input_FromH
        row[2]=Input_ToH
        row[3]=Input_Height
        row[4]=1
        Ucursor.updateRow(row)


###Iterate Parcels###
with arcpy.da.SearchCursor(Layer_Name, ["SHAPE@", "Row"]) as Scursor:
    for row in Scursor:
        for i in range(1,Input_NumOfLevels):
            Icursor = arcpy.da.InsertCursor(Layer_Name, fields)
            ValFromH = (Input_ToH+(Input_Height*(i-1))+(Gap*i))
            ValToH = (ValFromH + Input_Height)
            ValList = [row[0], ValFromH, ValToH, Input_Height, i+1, row[1]]
            Icursor.insertRow(ValList)


###End###
