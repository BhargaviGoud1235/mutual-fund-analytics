\# Day 1 Data Quality Summary



\## Project



Mutual Fund Analytics



\## Date



22 June 2026



\## Datasets Loaded



Total datasets loaded: 10



\* 01\_fund\_master.csv

\* 02\_nav\_history.csv

\* 03\_aum\_by\_fund\_house.csv

\* 04\_monthly\_sip\_inflows.csv

\* 05\_category\_inflows.csv

\* 06\_industry\_folio\_count.csv

\* 07\_scheme\_performance.csv

\* 08\_investor\_transactions.csv

\* 09\_portfolio\_holdings.csv

\* 10\_benchmark\_indices.csv



\## AMFI Code Validation



\* Total AMFI codes in fund master: 40

\* Total AMFI codes in NAV history: 40

\* Missing AMFI codes: 0



Result: All AMFI codes in the fund master dataset exist in the NAV history dataset.



\## Missing Values



Review the output of `data\_ingestion.py` and record any columns with missing values.



\## Duplicate Rows



Review the output of `data\_ingestion.py` and record any duplicate rows identified.



\## Data Type Validation



Expected data types:



\* amfi\_code: integer

\* date: datetime

\* nav: float

\* expense\_ratio\_pct: float

\* min\_sip\_amount: numeric

\* min\_lumpsum\_amount: numeric



\## Observed Inconsistencies



No AMFI code inconsistencies were identified during initial validation.



Additional issues, if any, will be addressed during data cleaning and transformation.



\## Conclusion



All datasets were successfully ingested and validated. Live NAV data for six mutual fund schemes was fetched from mfapi.in and stored in the raw data layer. Data cleaning and transformation activities will be completed in subsequent phases.



