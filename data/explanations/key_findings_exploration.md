
### Summary of Key Findings for Data Cleaning

1. **Missing Values**
- Shipping costs: 5 missing values
- Customer demographics: 6 missing values

2. **Data Type Issues**
- Availability appears to be stored as string
- Needs conversion to integer

3. **Duplicate Rows**
- 1 duplicated row detected

4. **Outliers**
- Shipping times contains a negative value (-5)
- Defect rates includes an extreme value of 100

5. **Inconsistent Categories**
- Transportation modes: lowercase values (e.g. "road")
- Shipping carriers: extra spaces (e.g. "DHL ")

6. **Potential Redundant Columns**
- Lead time and Lead times have the same number of unique values – further check needed
