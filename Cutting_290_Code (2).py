#Creating code for hail that was tornadic/non-tornadic from the days I picked (10 days in total)
#I have neither given or recieved nor have I tolerated others' peoples use of unauthorized aid -KC

#Import Modules 
import geopandas as gpd 
import matplotlib.pyplot as pp
import cartopy.crs as ccrs 
import cartopy.feature as cfeature 

#read in SPC risk analysis 
spc_url ='https://www.spc.noaa.gov/products/outlook/archive/2024/day1otlk_20240521_1200-shp.zip'
risk = gpd.read_file(spc_url)
print(risk)

#create SPC risk proj
spc_crs=ccrs.PlateCarree()

#create fig 
fig,ax= pp.subplots(subplot_kw={'projection':spc_crs})

#add map decorations
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.STATES)
ax.add_feature(cfeature.OCEAN)
ax.add_feature(cfeature.COASTLINE)
ax.set_extent([-135,-60,20,55], crs=spc_crs)

#loop over dataframe and add geometires 
for row in risk.itertuples():
    ax.add_geometries([row.geometry], spc_crs, edgecolor=row.stroke, facecolor=row.fill, alpha=0.7)
    #add ghost point for legend purposes
    ax.scatter(0,0,c=row.stroke,marker='s', label=row.LABEL,alpha=0.7)

ax.legend()

pp.savefig('cutting_spc_risk_map_20240521.png')
pp.close()