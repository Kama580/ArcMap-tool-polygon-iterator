import arcpy

###Define parameters###
Layer_Name=arcpy.GetParameterAsText(0)

###Add float fields###
arcpy.AddField_management(Layer_Name, 'FromH', 'DOUBLE', '#', '#', '#', '#', 'NULLABLE', 'NON_REQUIRED', '#')
arcpy.AddField_management(Layer_Name, 'ToH', 'DOUBLE', '#', '#', '#', '#', 'NULLABLE', 'NON_REQUIRED', '#')
arcpy.AddField_management(Layer_Name, 'Height', 'DOUBLE', '#', '#', '#', '#', 'NULLABLE', 'NON_REQUIRED', '#')

###Add int field###
arcpy.AddField_management(Layer_Name, 'Level', 'LONG', '#', '#', '#', '#', 'NULLABLE', 'NON_REQUIRED', '#')

###Add text field###
arcpy.AddField_management(Layer_Name, 'LevelName', 'TEXT', '#', '#', '20', '#', 'NULLABLE', 'NON_REQUIRED', '#')
arcpy.AddField_management(Layer_Name, 'Row', 'TEXT', '#', '#', '20', '#', 'NULLABLE', 'NON_REQUIRED', '#')
