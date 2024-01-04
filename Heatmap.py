import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

# Load the GeoJSON file of North Carolina counties
nc_counties_path = 'North_Carolina.geojson'
nc_counties_gdf = gpd.read_file(nc_counties_path)

# Load your CSV file with data
data_path = 'North Carolina Drug Deaths - Sheet1.csv'
data_df = pd.read_csv(data_path)

# Merge the GeoDataFrame with the data
merged_gdf = nc_counties_gdf.merge(data_df, how='left', left_on='County', right_on='County')

# Plot the heatmap
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
merged_gdf.plot(column='Average Drug Death Rate 2015-2022', cmap='YlOrRd', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)

# Add county labels
for x, y, label in zip(merged_gdf.geometry.centroid.x, merged_gdf.geometry.centroid.y, merged_gdf['County']):
    ax.text(x, y, label, fontsize=8, ha='center', va='center')

# Add a title
plt.title('North Carolina Heatmap')

# Show the plot
plt.show()
