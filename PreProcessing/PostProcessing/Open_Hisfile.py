# -*- coding: utf-8 -*-
"""
Created on Sat Jan 21 23:18:38 2023

@author: zijlker
"""

import dfm_tools as dfmt
import xarray as xr

his = xr.open_mfdataset(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\output\work0\results\RMM_VZM_his.nc',
                        preprocess = dfmt.preprocess_hisnc)