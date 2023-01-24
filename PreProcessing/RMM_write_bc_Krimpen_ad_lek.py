# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 10:02:06 2022

@author: veenstra
"""

import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
from netCDF4 import date2num
from hydrolib.core.io.bc.models import (
    ForcingModel,
    QuantityUnitPair,
    VerticalPositionType,
    TimeInterpolation,
    TimeSeries,
)

# input parameters
tstart_dt = dt.datetime(2017,12,1) #period begins with Gecontroleerd and ends with Ongecontroleerd for HOEKVHLD
# tstop_dt = dt.datetime(2019,1,1)
tzone = 'UTC+01:00'

#Load waterlevels from hisfile
His = xr.open_dataset(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\2018_Validation_run_1_entire_period\results\RMM_VZM_0000_wl_his.nc')

#Select waterlevels from station Krimpen ad Lek
waterlevel_df = His['waterlevel'].sel(stations='LE_988.7_R_LMW-H_Krimpen-aan-de-Lek-g6').resample({'time': '10min'}).mean().to_dataframe()
# waterlevel_df.index = waterlevel_df.index + pd.Timedelta('1H')
waterlevel_df = pd.DataFrame(waterlevel_df['waterlevel'])

refdate_str = f"minutes since {tstart_dt.strftime('%Y-%m-%d %H:%M:%S')} {tzone[3:]}"
waterlevel_df.loc[:,'datenum'] = date2num(waterlevel_df.index.to_pydatetime(),units=refdate_str,calendar='standard')
waterlevel_df = waterlevel_df.loc[:,['datenum', 'waterlevel' ]]
datablock_incltime = waterlevel_df.values




# datablock_incltime = np.concatenate([timevar_sel_rel[:,np.newaxis],waterlevel_df.values[:,np]],axis=1)

ForcingModel_object = ForcingModel()
for pli_PolyObject_name_num in ['boundary_KrimpenadLek_0001']:
    ts_one = TimeSeries(name=pli_PolyObject_name_num,
                        quantityunitpair=[QuantityUnitPair(quantity="time", unit=refdate_str),
                                          QuantityUnitPair(quantity='waterlevelbnd', unit='m')],
                        timeinterpolation=TimeInterpolation.linear,
                        datablock=datablock_incltime.tolist(),
                        )
    ForcingModel_object.forcing.append(ts_one)
ForcingModel_object.save(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\stochModel\input_dflowfm\boundary_KrimpenadLek.bc')