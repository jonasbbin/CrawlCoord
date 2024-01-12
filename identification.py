from difflib import *
#import numpy as np
import geopandas as gpd
from shapely.geometry import Point
import os


class Identifier():
    """
    Class to identify given strings to a matching item in the list
    i.e. locations, coordinates, plantnames
    """
    def __init__(self) -> None:
        """
        only_SG: Only looks at locations that in or near the border of SG, AI, AR
        """
        base_dir = os.path.dirname(__file__)
        file_path = os.path.join(base_dir, './swissBOUNDARIES3D_1_5_LV95_LN02.gpkg')
        self.geo_data = gpd.read_file(file_path, layer='TLM_HOHEITSGEBIET' )  # Replace with your file path
        self.geo_data = self.geo_data[self.geo_data.objektart=="Gemeindegebiet"]

        self.canton_dict = {
    1 : "ZH",
    2 : "BE",
    3 : "LU",
    4 : "UR",
    5 : "SZ",
    6 : "OW",
    7 : "NW",
    8 : "GL",
    9 : "ZG",
    10: "FR",
    11: "SO",
    12: "BS",
    13: "BL",
    14: "SH",
    15: "AR",
    16: "AI",
    17: "SG",
    18: "GR",
    19: "AG",
    20: "TG",
    21: "TI",
    22: "VD",
    23: "VS",
    24: "NE",
    25: "GE",
    26: "JU"
}     
    
    def get_gemeinde_region_canton(self, x, y):
        """
        Gets nearest community, canton, country given the coordinates.
        """
        try:
            if x== "" or y== "":
                return "", "", ""
            point = Point(x, y)  # Create a Shapely Point object
            for index, row in self.geo_data.iterrows():
                if row['geometry'].contains(point):
                
                    return row['name'], self.canton_dict[int(row["kantonsnummer"])], row['icc'] # Replace 'Canton' with the column containing canton names
            return "", "", ""
    
        except Exception as e:
            
            return "", "", ""

if __name__ == '__main__':
    identifier = Identifier()
    print(identifier.get_gemeinde_region_canton(12310, 4502))
    