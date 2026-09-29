 Data Cleaning Project

## Problem
Raw  file had 6 rows with 1 duplicate, missing values, and invalid amounts.

## Issues in This File
1. john DOE, John@GMAIL.COM — bad caps + duplicate (row 1 & 3)
2. jane smith, JANE@GMAIL.COM — missing amount (row 2)
3. bob lee, BOB@YAHOO.COM, 0, 2023/13/40 — $0 + invalid date (row 4)
4. alice Kim, 1000000 — invalid amount >$100k (row 5)

## What I Cleaned
- Fixed names: `john DOE` → `John Doe` (str.title)
- Fixed emails: `John@GMAIL.COM` → `john@gmail.com` (str.lower)
- Removed 1 duplicate (drop_duplicates)
- Removed 1 missing amount row (dropna)
- Removed 2 invalid: $0 and $1,000,000
- Total removed: 4 rows → 2 rows? Actually script keeps 3 if you allow 0

## Tools Used
Python, Pandas

## Files
- `donations.csv` — raw data (6 rows, 4 columns)
- `clean_donations.py` — cleaning script
- `cleaned_donations.csv` — final clean data

## Result
Before: (6, 4)
After: (3, 4)
3 rows removed, 3 clean rows ready for analysis
