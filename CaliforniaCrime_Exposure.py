#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 08:37:23 2020

@author: ivnagpal
"""
import pandas as pd
import numpy as np
import os 
import gspread
from oauth2client.service_account import ServiceAccountCredentials
path = r'/Users/ivnagpal/Desktop/SFDA Work/Cal-Felony-Sentencing'
os.chdir(path) 
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('cal-felony-data-2f21ba70d813.json', scope)
client = gspread.authorize(credentials)
work_sheet = client.open('California-Felony-Exposure-Dataset').get_worksheet(1)
data = work_sheet.get_all_records()

#Create Exposure Data Frame
exposure_df = pd.DataFrame(data)
exposure_df['Statutory_Code'] = exposure_df['Statutory_Code'].astype(str)
path = os.getcwd() + '/calexposure_df.csv'
exposure_df.to_csv (path, index = False, header=True)

 