This is a debug case for surface-sampling related issues for [blastAMR][]
(See [Issue 10 here](https://github.com/STFS-TUDa/blastAMR/issues/10))
in the form of a "parameter variation" on the number of processors.

The objective is to make sure there will be no segfaults for any
parallel configuration using `hierarchical` decomposition while
surface sampling is happening.

## Parameters to change

- Parameter variation settings:
  - In [`config.yaml`](config.yaml):
    1. `meta.n_trials` sets the number of cases to run with
       different number of processors.
    1. `problem.parameters.nProcs.values` should define the range of
       "number of processors" to be tried.
- Case parameters:
  - In [`tscas/system/controlDict`](tscas/system/controlDict):
    1. `endTime` should be set to higher than 0.01 if segfaults are suspected
       later in the run.

## Run the parameter variation

Requirements:
1. Git and Python >= 3.8
1. OpenFOAM (Tested with v2406, but anything >= v2212 should work)
1. [blastAMR][] compiled from `hotfix/sampling` branch

To run this parameter variation on the provided case:
```bash
git clone https://github.com/FoamScience/surface-sampling-bamr-debug
cd surface-sampling-bamr-debug
python -m venv .venv
source .venv/bin/activate
pip install foambo
openfoam2406 # or any other version >= 2212
# THIS IS IMPORTANT, replace with actual path on your machine
export AMRLB_PROJECT=</path/to/blastAMR>
foamBO
```

[blastAMR]: https://github.com/STFS-TUDa/blastAMR "blastAMR"
