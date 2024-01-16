
# CrawlCoord
Finds the corresponding Community/Canton/Country, given the Swisscoordinates of location. This application is designed for Excel sheets, where it can be applied. The functionality to search manually is also provided.

Creates a new Excel sheet, when given an Excelsheet with coordinates. The output file is written to the same directory. The application comes with tooltips that explain the different features.

We use the [swissBOUNDARIES3D](https://www.swisstopo.admin.ch/en/geodata/landscape/boundaries3d.html) dataset for the current boundaries of the different communities/cantons. The repsective GPKG must be manually downloaded.

The application can be called with:
`python CrawlCoord.py`

<img width="449" alt="Layout_of_the_application" src="https://github.com/jonasbbin/CrawlCoord/assets/126403545/3728d227-8c78-4b1c-b463-b3d69a3a5df2">

## Dependecies 
- pandas
- numpy
- shapely
- geopandas
- PyQt5

