# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 21:08:06 2023

@author: zijlker
"""
from pathlib import Path
from hydrolib.core.io.bc.models import (
    ForcingModel,
    QuantityUnitPair,
    VerticalPositionType,
    TimeInterpolation,
    TimeSeries,
)
import dfm_tools as dfmt
import xarray as xr

RunFolder = Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\output\work0')

River_DischargeFile = Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\boundary_conditions\rmm_rivdis_meas_20171101_20210102_MET.bc')

Boundary_noisefile = RunFolder / 'discharge_noise_lek.bc'

forcing_noise = ForcingModel(Boundary_noisefile)
forcing_discharge_noise_xr = dfmt.forcinglike_to_Dataset(forcing_noise.forcing[0], convertnan=True)

forcing_river = ForcingModel(River_DischargeFile)
forcing_discharge_river_xr = dfmt.forcinglike_to_Dataset(forcing_river.forcing[0], convertnan=True)