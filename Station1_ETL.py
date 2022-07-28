import pandas as pd

def Station1_ETL():
    """
    Extract, transform and load data, ensure the data integrity and quality
    :return: df cleansed dataset
    """
    # Load ASX dataset
    ASX200top10_xlsx = pd.ExcelFile('data/ASX200top10.xlsx')
    df_bloomberg_raw = pd.read_excel(ASX200top10_xlsx, 'Bloomberg raw');
    # Load client details
    ClientDetails_xlsx = pd.ExcelFile('data/Client_Details.xlsx')
    df_client_details = pd.read_excel(ClientDetails_xlsx, 'Data')
    # Note: Data is already cleaned 
    return df_bloomberg_raw, df_client_details

