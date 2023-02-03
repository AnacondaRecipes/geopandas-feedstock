import os
import geopandas


fname_shp = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.shp')
geopandas.read_file(fname_shp)

fname_cpg = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.cpg')
geopandas.read_file(fname_cpg)

fname_dbf = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.dbf')
geopandas.read_file(fname_dbf)

fname_shx = os.path.join(os.environ['RECIPE_DIR'], 'test_data', 'test.shx')
geopandas.read_file(fname_shx)

