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

Constant_Noise = 20.0

# input parameters
tstart = dt.datetime(2018,1,1) #period begins with Gecontroleerd and ends with Ongecontroleerd for HOEKVHLD
tstop  = dt.datetime(2019,1,1)
tzone = 'UTC+01:00'
tzone_correction = -1* pd.Timedelta('1H')

refdate_str = refdate_str = f"minutes since {tstart.strftime('%Y-%m-%d %H:%M:%S')} {tzone[3:]}"
boundary_noise = pd.DataFrame({'datetime_UTC': pd.date_range(tstart, tstop, freq = '1H') + tzone_correction})
boundary_noise.loc[:, 'datenum'] = date2num(boundary_noise['datetime_UTC'].dt.to_pydatetime(),units=refdate_str,calendar='standard')
boundary_noise.loc[:, 'discharge_noise'] = Constant_Noise 

datablock_incltime = boundary_noise.loc[:, ['datenum', 'discharge_noise']].values

ForcingModel_object = ForcingModel()
for pli_PolyObject_name_num in ['Lek_0001']:
    ts_one = TimeSeries(name=pli_PolyObject_name_num,
                        quantityunitpair=[QuantityUnitPair(quantity="time", unit=refdate_str),
                                          QuantityUnitPair(quantity='dischargebnd', unit='m')],
                        timeinterpolation=TimeInterpolation.linear,
                        datablock=datablock_incltime.tolist(),
                        )
    ForcingModel_object.forcing.append(ts_one)
ForcingModel_object.save(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\stochModel\input_dflowfm\discharge_noise_lek_constant_20.bc')