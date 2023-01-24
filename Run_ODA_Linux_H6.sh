#Specify ODA definition file
ODAFile="EnKF.oda"

#Specify number of computational cores
Nodes=2

# Load netcdf module
module load netcdf

# Activate right python directory
source activate venv

export pwd=$PWD
# export OPENDARUNSCRIPTSPATH=/p/kalman-filter-dflow-fm/OpenDA_Bins/MostRecent/bin/
export OPENDARUNSCRIPTSPATH=/p/kalman-filter-dflow-fm/openda_test/bin20220922
# export OPENDADIR=/p/kalman-filter-dflow-fm/OpenDA_Bins/MostRecent/bin/
export OPENDADIR=/p/kalman-filter-dflow-fm/openda_test/bin20220922
export OPENDADIMRPATH=p/d-hydro/dimrset/2022/2022.03/

cd $OPENDARUNSCRIPTSPATH

source settings_local.sh linux

echo 'This is OPENDADIR:' $OPENDADIR 
cd $pwd
echo 'executing: qsub -cwd -q normal-e3-c7 -V -pe distrib ' $Nodes '-N '${PWD##*/} $OPENDADIR'/oda_run_tammo.sh '$ODAFile

export ODA_JAVAOPTS='-Xmx2048m'
# $OPENDADIR/oda_run_tammo.sh SSKF.oda

# qsub -cwd -q normal-e3-c7 -V -pe distrib $Nodes -N ${PWD##*/} $OPENDADIR/oda_run_tammo.sh $ODAFile