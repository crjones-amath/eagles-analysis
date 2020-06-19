# supplemental_wrf_testbed_scripts
Python scripts and jupyter notebooks relevant to WRF-LES testbed simulation workflow

The WRF-LES simulation workflow for testbed simulations follows a series of steps:
1. Retrieve ERA5 reanalysis (full model levels) for the desired region and date(s)
2. Use reanalysis to drive a WRF mesoscale simulation for the desired testbed location
3. Verify that WRF mesoscale simulations look reasonable
4. Use the WRF mesoscale simulation to generate forcings for WRF-LES testbed simulations
5. Run desired WRF-LES simulations

This repository consists of various scripts to aid in these steps, as further detailed below.

1. Retrieve ERA5 reanalysis (full model levels) for the desired region and date(s)
   - `scripts/retrieve_and_preprocess_era_for_wrf.py` provides code for retrieving ERA5
     for use in WRF and performs minimal preprocessing to use in the usual wrf workflow
2. Use reanalysis to drive a WRF mesoscale simulation for the desired testbed location
   - `wrf_run_details/namelist.input` provides WRF namelist for a sample case
3. Verify that WRF mesoscale simulations look reasonable
   - `preprocess_era5_to_compare_with_obs.ipynb` processes ERA5 reanalysis to facilitate
     easier comparison with both observations and WRF mesoscale runs. This includes changing 
     output names, and converting from model level to pressure and geopotential height
   - `ena/compare_era5_vs_wrf_vs_obs_ena.ipynb` performs simple comparison of reanalysis, 
      ARM observations, and WRF mesoscale simulations for sample case at the ACE-ENA location
   - `ena/ena_wrf_vs_obs_[yyyy]-[mm]-[dd].ipynb` does a simple comparison of ERA5 (inputs),
     WRF mesoscale simulations, and ARM obs for the ACE-ENA case for date yyyy-mm-dd
4. Use the WRF mesoscale simulation to generate forcings for WRF-LES testbed simulations
   - These scripts are in a seperate repository: `https://github.com/eagles-project/process_wrf_les_forcing`
5. Run desired WRF-LES simulations
   - `scripts/gen_wrf_timeseries_additions.ipynb` provides a template for code blocks to add 
     spectral bin microphysics (SBM) output to the single-column timeseries (`tslist`) output.
     These code blocks get copy/pasted into `wrf_timeseries.F` and `Registry.EM_COMMON` at the 
     appropriate spots. There almost certainly is a better way to do this ...
