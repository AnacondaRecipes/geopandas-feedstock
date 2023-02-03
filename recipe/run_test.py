import os
import geopandas
import fiona


RECIPE_DIR = os.environ['RECIPE_DIR']

fname_shp = os.path.join(RECIPE_DIR, 'test_data', 'test.shp')
geopandas.read_file(fname_shp, encoding='utf-8')

fname_dbf = os.path.join(RECIPE_DIR, 'test_data', 'test.dbf')
geopandas.read_file(fname_dbf, encoding='utf-8')

fname_shx = os.path.join(RECIPE_DIR, 'test_data', 'test.shx')
geopandas.read_file(fname_shx, encoding='utf-8')

