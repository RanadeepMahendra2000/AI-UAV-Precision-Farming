import geopandas as gpd
from shapely.geometry import Point

# ------------------ STEP 6: Geospatial Mapping ------------------

def export_to_shapefile(gps_data, output_file):
    """Convert NDVI data to a geospatial shapefile."""
    gdf = gpd.GeoDataFrame(geometry=[Point(lon, lat) for lat, lon in gps_data])
    gdf.to_file(output_file)

# Example GPS data
gps_data = [(17.3850, 78.4867), (17.3860, 78.4877), (17.3870, 78.4887)]

# Export NDVI data to shapefile
export_to_shapefile(gps_data, "processed_data/ndvi_farm_map.shp")

print("✅ NDVI Geospatial Export Completed Successfully!")
