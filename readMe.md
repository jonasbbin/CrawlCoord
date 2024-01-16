
# CrawlCoord
Given the Swisscoordinates of location. finds the corresponding Community/Canton/Country. This Application is designed for Excel sheets, where it can be applied. The functionality to do the search manually is also provided.

When given an Excelsheet with coordinates, it will create a new sheet. The output file is written to the same directory. 

We use the [swissBOUNDARIES3D](https://www.swisstopo.admin.ch/en/geodata/landscape/boundaries3d.html) dataset for the current boundaries of the different communities/cantons. The repsective GPKG must be manually downloaded.

The programme can be called with:
`python CrawlCoord.py`
## Dependecies 

- pandas
- numpy
- shapely
- geopandas
- PyQt5

