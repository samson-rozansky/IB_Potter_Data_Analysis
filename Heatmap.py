import geopandas as gpd
import matplotlib.pyplot as plt

geojson_path = 'North_Carolina.geojson'
gdf = gpd.read_file(geojson_path)

gdf.plot()
plt.title('Original GeoJSON Data')
plt.show()

fig, ax = plt.subplots(1,1, figsize=(10,10))
gdf.plot(ax=ax, cmap='Y10rRd', alpha = 0.5)
plt.title('Heatmap from GeoJSON Data')
plt.show()
