# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 19:30:14 2023

@author: zijlker
"""

import dfm_tools as dfmt
import xarray as xr
from pathlib import Path
import matplotlib.pyplot as plt
plt.close('all')
cm = 1/2.54
output_dir = Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\Experiment_Outputs\Simulation_Discharge_Noise_20\Figures')
his_filepaths = {'Reference run' : Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\Experiment_Outputs\Simulation_Discharge_Noise_0\work0\results\full_RMM_VZM_his.nc') ,
                 'Truth run'     : Path(r'p:\11208053-004-kpp2022-rmm1d2d\C_Work\09_Validatie2018_2020\dflowfm2d-rmm_vzm-j19_6-v2d\computations\validation\KalmanFilterDischarge\Experiment_Outputs\Simulation_Discharge_Noise_20\work0\results\full_RMM_VZM_his.nc')}
his_files = {}
for runname, filepath in his_filepaths.items():
    his_files[runname] = xr.open_mfdataset(filepath, preprocess = dfmt.preprocess_hisnc)

plot_stations = ['LE_971_6_R_LMW-H_Schoonhoven', 
                 'LE_947_1_R_LMW-H_Hagestein-beneden',
                 'LE_950_00']

for station in plot_stations:
    fig, ax1 = plt.subplots(1,1, figsize = (14*cm, 7*cm))
    for runname, hisfile in his_files.items():
        hisfile['waterlevel'].sel(stations=station).plot(ax=ax1, label=runname)
    ax1.set_ylabel('Waterlevel [m]')
    ax1.set_xlabel('')

    
    #Make a difference plot
    ax2 = ax1.twinx()
    waterlevel_diff = his_files['Truth run']['waterlevel'] - his_files['Reference run']['waterlevel']
    waterlevel_diff.sel(stations=station).resample({'time': '1D'}).mean().plot(linestyle = 'solid',
                                                                               marker = '+', 
                                                                               ax=ax2, 
                                                                               label='Average difference')
    ax2.set_ylabel('Waterlevel diff [m]')
    # ax2.set_ylim([-0.3 , 0.3])
    ax1.set_title(station)
    ax2.set_title('')
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_dir / f'Waterlevel_{station}_comparison_reference.png', dpi=400)