# SLR Observatory Data Pipeline
This package can be used by Satellite Laser Ranging observatories to download and archive ephemerides data. 

## Downloading Ephemerides
This program downloads ephemerides from the international IRLS datacenter via ftps connection. It connects to the IRLS website and retrieves all the current epehemerides, except the ones that are mentioned in the BlackList.txt. Each day the satellite names on the IRLS website are different and written in the following format 'Name of Satellite-Date-Time'. The program strips date and time and finds satellites by name only. Then, it downloads Sentinela A and B satellites from separate ftps connection (access to these satellites is restricted to few observatories) and finally all the ephemerides are combined into one single file. 

## Catalogue Clearing
This program archives and deleates  directories with the observational data. It finds and selects specific extensions (.oga; .esa etc.), archives them, and deleates old directories. It detects whether a flashdrive is inserted and if it isn't the program will not start. This is done to make sure that data on the observatory flash drive is wiped out as well. 

## About 
This software was developed for the Satellite Laser Ranging Observatory located in Kyiv, Ukraine. It is actively used to download and archive data. 
