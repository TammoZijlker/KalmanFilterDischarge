@echo off
rem This script requires one input argument i.e. file name of the dimr_config.xml
rem To use this script, set DFLOWFMDIR to the installation directory of D-Flow FM.
rem set DFLOWFMDIR=d:\Project\FEWS-NZ\FEWS-Noordzee\202102\Noordzee_SA_MO-47\Modules\dimr_2022.03\
rem set DFLOWFMDIR=p:\d-hydro\dimrset\2022\2022.03\
set DFLOWFMDIR=%OPENDADIMRPATH%
if "%DFLOWFMDIR%"=="" goto error_not_defined

set dimr="%DFLOWFMDIR%\x64\dimr\scripts\run_dimr.bat"
rem set dimr="%DFLOWFMDIR%\plugins\DeltaShell.Dimr\run_dimr.bat"
rem 
rem check if dimr is available
rem
if not exist %dimr% goto error_dimr_not_found

rem
rem start DIMR for D-Flow FM 
rem 
%dimr% %1
goto eof

rem
rem error messages
rem

:error_not_defined
echo ERROR in ./stochModel/bin/start_dimr.bat:
echo No installation directory of D-Flow FM specified.
goto eof

:error_dimr_not_found
echo ERROR in ./stochModel/bin/start_dimr.bat:
echo File not found: %dimr%
goto eof

:eof
exit /B %ERRORLEVEL%
