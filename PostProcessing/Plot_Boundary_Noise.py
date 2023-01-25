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
import matplotlib.pyplot as plt
plt.close('all')
cm=1/2.54
RunFolder = Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\stochModel/input_dflowfm')

River_DischargeFile = Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\boundary_conditions\rmm_rivdis_meas_20171101_20210102_MET.bc')

Boundary_noisefile = RunFolder / 'discharge_noise_lek.bc'

forcing_noise = ForcingModel(Boundary_noisefile)
forcing_discharge_noise_xr = dfmt.forcinglike_to_Dataset(forcing_noise.forcing[0], convertnan=True)

forcing_river = ForcingModel(River_DischargeFile)
forcing_discharge_river_xr = dfmt.forcinglike_to_Dataset(forcing_river.forcing[0], convertnan=True)

fig, ax1 = plt.subplots(1,1, figsize = (14*cm, 7*cm))
forcing_discharge_river_xr['dischargebnd'].sel(time='2018-01').plot()
ax1.set_ylabel('Discharge Hagestein [m$^3$/s]')
ax1.set_xlabel('')


#Make a difference plot
ax2 = ax1.twinx()
# waterlevel_diff = his_files['Truth run']['waterlevel'] - his_files['Reference run']['waterlevel']
# waterlevel_diff.sel(stations=station).resample({'time': '1D'}).mean().plot(linestyle = 'solid',
#                                                                            marker = '+', 
#                                                                            ax=ax2, 
#                                                                            label='Average difference')
# ax2.set_ylabel('Waterlevel diff [m]')
# # ax2.set_ylim([-0.3 , 0.3])
# ax1.set_title(station)
# ax2.set_title('')
# plt.legend()
# plt.tight_layout()
# plt.savefig(output_dir / f'Waterlevel_{station}_comparison_reference.png', dpi=400)