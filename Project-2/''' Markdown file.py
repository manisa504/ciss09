'''  Markdown file
 Import Modules
 I started by importing the necessary modules:
 import pandas as pd
 from pandas import merge

 Data Preparation
 then proceeded to read the files from a local folder and display the details of the file:
 df_model = pd.read_csv("models.csv")
 df_region = pd.read_csv("region.csv")
 df_field = pd.read_csv("fields.csv")
 df_vendor = pd.read_csv("vendors.csv")
 df_power = pd.read_csv("powergeneration.csv")
 df_power.info()

 merge the files into a single dataset, preserving as much data as possible, and drop any repeated columns: 
 df_power_field = df_power.merge(df_field, how='left', left_on='field',right_on='fieldtxt')
df_power_field = df_power_field.drop('fieldtxt',axis=1)

df_power_field_model = df_power_field.merge(df_model, how='left', left_on='model_cd',right_on='modelcd')
df_power_field_model = df_power_field_model.drop('model_cd',axis=1)

df_power_field_model_vendor = df_power_field_model.merge(df_vendor, how='left', left_on='vendor', right_on='CIK')
df_power_field_model_vendor = df_power_field_model_vendor.drop('CIK',axis=1)

df_power_field_model_vendor_region = df_power_field_model_vendor.merge(df_region, how='left', left_on='region_cd', right_on='regioncd')
df_power_field_model_vendor_region = df_power_field_model_vendor_region.drop('regioncd',axis=1)

We create a copy of the resulting dataframe and fill any missing values with 0:

df = df_power_field_model_vendor_region.copy()
df = df.fillna(0)
Computations
We then create the following computational columns:

Revenue per kilowatt:
df['rev_per_kw'] = df['RevenueProduced'] / df['kilowatt_production']
Net profit for the first year of installation:


df['net_profit_per_yr'] = df['RevenueProduced'] - df['yearlyupkeep']
Hours per year of operation:


df['hr_per_yr_op'] = df['HoursPerWeekOfOperation'] * 52
Maintenance cost per year:


df['annualy_mntn_cost'] = df['yearlyupkeep'] / df['hr_per_yr_op']
Efficiency:


def eff(df):
    if (df.annualy_mntn_cost > 1 and df.kilowatt_production < 3):
        return 'high'
    elif (df.annualy_mntn_cost < 1 and df.annualy_mntn_cost > 0.5 and df.kilowatt_production > 3 and df.kilowatt_production < 6):
        return 'high'
    elif (df.kilowatt_production > 6 and df.kilowatt_production < 9):
        return 'high'
    else: 
        return 'Low'
        
df['efficiency'] = df.apply(eff, axis=1)
Vendor quality:


def ven_quality(df):
    if (df.hasroads == 'Yes' and df.haseasement == 'Yes' and df.AreaOfExpertise == 'High Capacity'):
        return 'Good'
    elif (df.hasroads == 'Yes' and df.haseasement == 'Yes' and df.AreaOfExpertise == 'High Efficiency'):
        return 'Good'
    else:
        return 'Bad' '''