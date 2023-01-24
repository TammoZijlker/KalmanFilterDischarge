export DFLOWFMDIR=/p/d-hydro/dimrset/2022/2022.03
if [ -z $1 ]; then
    echo ERROR: no dimr configuration file is specified
    exit 1
fi
if [ -z $DFLOWFMDIR ]; then
    echo $DFLOWFMDIR
    echo ERROR: No installation directory of D-Flow FM specified.
    exit 1
fi
if [ ! -d $DFLOWFMDIR ]; then
    echo ERROR: D-Flow FM installation directory does not exist: $DFLOWFMDIR
    exit 1
fi
export dimr=$DFLOWFMDIR/lnx64/bin/run_dimr.sh
if [ ! -f $dimr ]; then
    echo ERROR in ./stochModel/bin/start_dimr.sh:
    echo File not found: $dimr
    exit 1
fi
$dimr -m $1
#  > start dimr.log 2>&1
