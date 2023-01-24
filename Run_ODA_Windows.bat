@REM @set OPENDARUNSCRIPTSPATH=p:\kalman-filter-dflow-fm\OpenDA_Bins\bin20230113\
@set OPENDARUNSCRIPTSPATH=p:\kalman-filter-dflow-fm\openda_test\bin20220922\
set OPENDADIMRPATH=p:\d-hydro\dimrset\2022\2022.03\

@REM Run Openda
@REM %OPENDARUNSCRIPTSPATH%\oda_run_batch_Tammo.bat SequentialStochasticSimulation.oda
%OPENDARUNSCRIPTSPATH%\oda_run_batch.bat SequentialStochasticSimulation.oda

@REM Average observations afterwards
@REM TODO
pause