# Calibrated data
Delayed mode files
Delayed mode profile files are the same as the real time profile files, except their file names on the GDACs all contain a “D” before the WMO number (e.g. D5900400_001.nc, BD5904179_001.nc). These profile files contain delayed mode adjusted data, which are recorded in the variable <PARAM>_ADJUSTED. The variable DATA_MODE will record ‘D’. Two other variables are also filled in delayed mode, which are <PARAM>_ADJUSTED_QC and <PARAM>_ADJUSTED_ERROR, which record the delayed mode quality control flags and the delayed mode adjustment uncertainty.

Core Argo delayed mode files are available 1 – 2 years after a profile is taken; sometimes earlier. These have been subjected to detailed scrutiny by oceanographic experts and the adjusted salinity has been estimated by comparison with high quality ship-based CTD data and Argo climatologies using the process described by Wong et al, 2003; Böhme and Send, 2005; Owens and Wong, 2009; Cabanes et al, 2016.

For BGC parameters, delayed mode files can be available within 5 – 6 cycles after deployment.  This is because the BGC sensors often return data that are out of calibration, but early adjustment methodologies exist that can significantly improve their accuracy.  Additional delayed mode quality control occurs when a longer record of float data is available.

To learn more about delayed mode quality control, read the papers on the methods linked above or see the ADMT documentation page for core Argo and BGC-Argo quality control documentation.




