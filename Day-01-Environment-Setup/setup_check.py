import arcpy

# Vérification du statut de la licence ArcGIS Pro
print(f"Statut de la licence : {arcpy.CheckProduct('ArcEditor')}")

# Activation de l'extension Spatial Analyst si disponible
if arcpy.CheckExtension("Spatial") == "Available":
    arcpy.CheckOutExtension("Spatial")
    print("Extension Spatial Analyst activée avec succès.")

# Affichage du nombre d'outils disponibles
tools = arcpy.ListTools()
print(f"Nombre d'outils de géotraitement accessibles : {len(tools)}")
