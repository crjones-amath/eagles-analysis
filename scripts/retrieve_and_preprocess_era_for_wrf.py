#!/usr/bin/env python
import cdsapi
import subprocess
c = cdsapi.Client()

retrieve_surface = False
retrieve_model_levels = False

# Retrieve from server: 
date_range = '2018-01-16/to/2018-01-26'
date = [''.join(d.split('-')) for d in date_range.split('/to/')]
area = '45/-35/35/-20' # N/W/S/E

# filename convention
surf_file = f'ERA5_ENA_{date[0]}-{date[1]}_sfc.grb'
ml_file = f'ERA5_ENA_{date[0]}-{date[1]}_ml.grb'

# surface data
if retrieve_surface:
    c.retrieve('reanalysis-era5-complete',
            {'class':'ea',
                'date': '2018-01-16/to/2018-01-26',
                'area': area,
                'expver':'1',
                'levtype':'sfc',
                'param':'msl/sp/skt/2t/10u/10v/2d/z/lsm/sst/ci/sd/stl1/stl2/stl3/stl4/swvl1/swvl2/swvl3/swvl4', 
                'stream':'oper',
                'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',
                'type':'an',
                'grid':"0.25/0.25"}, 
            surf_file) 
    print('surface success!')

# model level data
if retrieve_model_levels:
    c.retrieve('reanalysis-era5-complete',                                                                                                                          
            {'class':'ea',                                                                                                                                       
                'date': '2018-01-16/to/2018-01-26',                                                                                                                 
                'area': area,                                                                                                                                       
                'expver': '1',                                                                                                                                      
                'levelist': '1/to/137',                                                                                                                             
                'levtype': 'ml',                                                                                                                                    
                'param': '129/130/131/132/133/152',        
                'stream': 'oper',                                                                                                                                   
                'time': '00:00:00/01:00:00/02:00:00/03:00:00/04:00:00/05:00:00/06:00:00/07:00:00/08:00:00/09:00:00/10:00:00/11:00:00/12:00:00/13:00:00/14:00:00/15:00:00/16:00:00/17:00:00/18:00:00/19:00:00/20:00:00/21:00:00/22:00:00/23:00:00',                                                                                 
                'type': 'an',                                                                                                                                       
                'grid': "0.25/0.25"},                                                                                                                               
            ml_file)
    print('model layer success!')

# post-processing

# prep surface file
# output looks like: ecmf_yyyymmdd_an_srf_0.grib1
subprocess.run(['grib_filter', 'split.rule', surf_file])

# prep model layer file(s)
# output looks like: ecmf_yyyymmdd_an_ml_0.grib1
subprocess.run(['grib_set', '-s', 'deletePV=1,edition=1',
                ml_file, ml_file.replace('.grb', '.grib1')])
subprocess.run(['grib_filter', 'split.rule', ml_file.replace('.grb', '.grib1')])

# provided these are successful, the next step is to run ungrib.exe, metgrid.exe, geogrid.exe ans usual