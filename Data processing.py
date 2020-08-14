#!/usr/bin/env python
# coding: utf-8

# In[99]:


import pandas as pd
import numpy as np


# In[453]:


get_ipython().run_line_magic('pinfo', 'pd.read_excel')


# In[100]:


get_ipython().run_line_magic('matplotlib', 'notebook')

import matplotlib.pyplot as plt


# In[117]:


TNdata = pd.read_excel('11112019063252TVS_Output_Quantta-Emerald.xlsx', sheet_name="TN Data", header=0)


# In[118]:


TNdata['age'] = pd.DatetimeIndex(TNdata['cl_dob']).year


# In[119]:


from datetime import date
TNdata['age'] = date.today().year - TNdata['age']
TNdata['age']


# In[104]:


colist = TNdata.columns


# In[105]:


for i in range(len(colist)):
    print("'"+colist[i]+"'"+",")


# In[120]:


TNdata = TNdata[['cl_CITY','cl_pincode',
'cl_TALUKA',
'cl_TOWN','age','hh_tot',
'hh_good',
'hh_liv',
'hh_dilap',
'RF_other',
'rf_bt_brick',
'rf_stone_sl',
'rf_metal_asb',
'rf_con',
'hh_size_one',
'hh_size_two',
'hh_size_three',
'hh_size_four',
'hh_size_five',
'hh_size_six_eight',
'hh_size_nine_plus',
'status_owned',
'status_rented',
'status_other',
'mcouple_none',
'mcouple_one',
'mcouple_two',
'mcouple_three',
'mcouple_four',
'mcouple_fiveplus',
'lig_electricity',
'avail_bank_srv',
'ava_radio',
'ava_tv',
'as_comp_wt_inet',
'as_comp_wo_inet',
'as_ll_only',
'as_mob_only',
'as_tele_mob_both',
'as_bicycle',
'as_twowheeler',
'as_fourwheeler',
'as_all',
'as_no',
'TOT_P',
'TOT_M',
'TOT_F',
'P_06',
'M_06',
'F_06',
'P_SC',
'P_ST',
'P_LIT',
'M_LIT',
'F_LIT',
'P_ILL',
'M_ILL',
'F_ILL',
'TOT_WORK_P',
'TOT_WORK_M',
'TOT_WORK_F',
'MAINWORK_P',
'MAINWORK_M',
'MAINWORK_F',
'MAIN_CL_P',
'MAIN_CL_M',
'MAIN_CL_F',
'MAIN_AL_P',
'MAIN_AL_M',
'MAIN_AL_F',
'MAIN_HH_P',
'MAIN_HH_M',
'MAIN_HH_F',
'MAIN_OT_P',
'MAIN_OT_M',
'MAIN_OT_F',
'MARGWORK_P',
'MARGWORK_M',
'MARGWORK_F',
'MARG_CL_P',
'MARG_AL_P',
'MARG_HH_P',
'MARG_OT_P',
'MARGWORK_3_6_P',
'MARGWORK_3_6_M',
'MARGWORK_3_6_F',
'MARGWORK_0_3_P',
'MARGWORK_0_3_M',
'MARGWORK_0_3_F',
'NON_WORK_P',
'NON_WORK_M',
'NON_WORK_F',
'Income_VL',
'Income_L',
'Income_M',
'Income_H',
'Income_VH',
'BPL_count',
'Airport',
'Commercial_area',
'Commercial_Complex',
'Forest',
'Industry',
'Other',
'Parks_Play_Grounds',
'Residential_area',
'Residential_complex',
'Residential_congested_area',
'Slums',
'Under_Construction_Area',
'Vacant_Land',
'Water_Body',
'Hotel_Star_Null-2',
'hotel_star_3',
'hotel_star_4',
'hotel_star_5',
'hotel_price_0_2k',
'hotel_price_2_4k',
'hotel_price_4_max',
'rest_blw_2.5',
'rest_2.5_3.5',
'rest_3.5_4.5',
'rest_abv_4.5',
'restaurant_rs_0_500',
'restaurant_rs_500_1500',
'restaurant_rs_1500_3000',
'restaurant_rs_3000_5000',
'sale_property_0_20l',
'Sale_Property_20_50L',
'Sale_Property_50_80L',
'Sale_Property_80L_1.25Cr',
'sale_property_1.25cr_20cr',
'Sale_Property_Below3K',
'Sale_Property_3k-5k',
'Sale_Property_5k-8k',
'Sale_Property_8k-13k',
'Sale_Property_13k_Abv',
'Rent_Property_Lessthan_5K',
'Rent_Property_5K_16K',
'rent_property_16k_30k',
'rent_property_30k_60k',
'rent_property_60k_90k',
'Rent_Property_90_1.5L',
'rental_per_sqft_blw_15',
'rental_per_sqft_15-30',
'rental_per_sqft_30-50',
'rental_per_sqft_50-100',
'rental_per_sqft_100_abv',
'airport',
'atm',
'bank',
'clinic',
'education_institute',
'hospital',
'hotel',
'industry',
'mall',
'medical_specialist',
'msme',
'nbfc',
'park',
'pharmacy',
'post_office',
'recreation',
'retail_store',
'school',
'service_centers',
'service_providers',
'special_economic_zone',
'tourism',
'traffic_junctions',
'Rural_urban _classification',
'buddhist',
'christian',
'hindu',
'jain',
'muslim',
'sikh']]


# In[121]:


TNdata.shape[1]


# In[122]:


TNdata.head()


# In[204]:


tndata = TNdata[(TNdata['cl_CITY']=='Chennai') | (TNdata['cl_CITY']=='Kanchipuram')]
tndata.head()


# In[142]:


tndata.columns


# In[205]:


tndata.shape


# In[988]:


quantta=(TNdata.groupby('cl_pincode')['cl_CITY',
'cl_TALUKA',
'cl_TOWN','age','hh_tot',
'hh_good',
'hh_liv',
'hh_dilap',
'RF_other',
'rf_bt_brick',
'rf_stone_sl',
'rf_metal_asb',
'rf_con',
'hh_size_one',
'hh_size_two',
'hh_size_three',
'hh_size_four',
'hh_size_five',
'hh_size_six_eight',
'hh_size_nine_plus',
'status_owned',
'status_rented',
'status_other',
'mcouple_none',
'mcouple_one',
'mcouple_two',
'mcouple_three',
'mcouple_four',
'mcouple_fiveplus',
'lig_electricity',
'avail_bank_srv',
'ava_radio',
'ava_tv',
'as_comp_wt_inet',
'as_comp_wo_inet',
'as_ll_only',
'as_mob_only',
'as_tele_mob_both',
'as_bicycle',
'as_twowheeler',
'as_fourwheeler',
'as_all',
'as_no',
'TOT_P',
'TOT_M',
'TOT_F',
'P_06',
'M_06',
'F_06',
'P_SC',
'P_ST',
'P_LIT',
'M_LIT',
'F_LIT',
'P_ILL',
'M_ILL',
'F_ILL',
'TOT_WORK_P',
'TOT_WORK_M',
'TOT_WORK_F',
'MAINWORK_P',
'MAINWORK_M',
'MAINWORK_F',
'MAIN_CL_P',
'MAIN_CL_M',
'MAIN_CL_F',
'MAIN_AL_P',
'MAIN_AL_M',
'MAIN_AL_F',
'MAIN_HH_P',
'MAIN_HH_M',
'MAIN_HH_F',
'MAIN_OT_P',
'MAIN_OT_M',
'MAIN_OT_F',
'MARGWORK_P',
'MARGWORK_M',
'MARGWORK_F',
'MARG_CL_P',
'MARG_AL_P',
'MARG_HH_P',
'MARG_OT_P',
'MARGWORK_3_6_P',
'MARGWORK_3_6_M',
'MARGWORK_3_6_F',
'MARGWORK_0_3_P',
'MARGWORK_0_3_M',
'MARGWORK_0_3_F',
'NON_WORK_P',
'NON_WORK_M',
'NON_WORK_F',
'Income_VL',
'Income_L',
'Income_M',
'Income_H',
'Income_VH',
'BPL_count',
'Airport',
'Commercial_area',
'Commercial_Complex',
'Forest',
'Industry',
'Other',
'Parks_Play_Grounds',
'Residential_area',
'Residential_complex',
'Residential_congested_area',
'Slums',
'Under_Construction_Area',
'Vacant_Land',
'Water_Body',
'Hotel_Star_Null-2',
'hotel_star_3',
'hotel_star_4',
'hotel_star_5',
'hotel_price_0_2k',
'hotel_price_2_4k',
'hotel_price_4_max',
'rest_blw_2.5',
'rest_2.5_3.5',
'rest_3.5_4.5',
'rest_abv_4.5',
'restaurant_rs_0_500',
'restaurant_rs_500_1500',
'restaurant_rs_1500_3000',
'restaurant_rs_3000_5000',
'sale_property_0_20l',
'Sale_Property_20_50L',
'Sale_Property_50_80L',
'Sale_Property_80L_1.25Cr',
'sale_property_1.25cr_20cr',
'Sale_Property_Below3K',
'Sale_Property_3k-5k',
'Sale_Property_5k-8k',
'Sale_Property_8k-13k',
'Sale_Property_13k_Abv',
'Rent_Property_Lessthan_5K',
'Rent_Property_5K_16K',
'rent_property_16k_30k',
'rent_property_30k_60k',
'rent_property_60k_90k',
'Rent_Property_90_1.5L',
'rental_per_sqft_blw_15',
'rental_per_sqft_15-30',
'rental_per_sqft_30-50',
'rental_per_sqft_50-100',
'rental_per_sqft_100_abv',
'airport',
'atm',
'bank',
'clinic',
'education_institute',
'hospital',
'hotel',
'industry',
'mall',
'medical_specialist',
'msme',
'nbfc',
'park',
'pharmacy',
'post_office',
'recreation',
'retail_store',
'school',
'service_centers',
'service_providers',
'special_economic_zone',
'tourism',
'traffic_junctions',
'Rural_urban _classification',
'buddhist',
'christian',
'hindu',
'jain',
'muslim',
'sikh'].agg(lambda x:x.value_counts().idxmax()))


# In[989]:


quantta


# In[990]:


final


# In[991]:


quantta=quantta.reset_index()
quantta


# In[993]:


final1=final.merge(quantta,on='cl_pincode',how='left')
final1


# In[994]:


final1.to_excel('final1.xlsx')


# In[996]:


FINAL=pd.read_excel('final1.xlsx')
FINAL


# In[414]:


col = tp.index
col


# In[416]:


ls = [
       ('Ambattur Ind.Estate (NorthWest Region)', 600058),
       ('Aminijkarai (NorthWest Region)', 600029),
       ('Anna Nagar (NorthWest Region)', 600101),
       ('Anna Salai (SouthEast Region)', 600002),
       ('Ayanavaram (NorthWest Region)', 600023),
       ('Besant Nagar (SouthEast Region)', 600090),
       ('Chetpet (NorthWest Region)', 600031),
       ('Chromepet (SouthWest Region)', 600044),
       ('Dr Algappa Road (NorthEast Region)', 600084),
       ('Egmore (NorthEast Region)', 600008),
       ('Gopalapuram (SouthEast Region)', 600086),
       ('Gowriwakkam (SouthWest Region)', 600073),
       ('K.K Nagar (SouthWest Region)', 600078),
       ('Kilpauk (NorthWest Region)', 600010),
       ('Kodambakkam (SouthWest Region)', 600024),
       ('Madipakkam (SouthWest Region)', 600091),
       ('Mandaveli (SouthEast Region)', 600004),
       ('Medavakkam (SouthEast Region)', 600010),
       ('Mylapore (SouthEast Region)', 600004),
       ('Nandambakam (SouthWest Region)', 600089),
       ('Nanganallur (SouthWest Region)', 600061),
       ('Nungambakkam (NorthWest Region)', 600034),
       ('Perambur (NorthWest Region)', 600011),
       ('R A Puram (SouthEast Region)', 600028),
       ('Roya Puram (NorthEast Region)', 600013),
       ('Royapettah (SouthEast Region)', 600014),
       ('Saidapet (SouthWest Region)', 600015),
       ('T. Nagar (SouthWest Region)', 600017),
       ('Tambaram (SouthWest Region)', 600045),
       ('Thirumangalam (NorthWest Region)', 600040),
       ('Thiruvanmiyur (OMR) (OMR-1)', 600041),
       ('Vadapalani (SouthWest Region)', 600026),
       ('Velachery (SouthEast Region)', 600042),
       ('Vepery (NorthEast Region)', 600007),
       ('Virugambakkam (SouthWest Region)', 600092),
       ('Adyar (SouthEast Region)', 600020),
       ('Adambakam (SouthWest Region)', 600088),
       ('Padi (NorthWest Region)', 600050),
       ('Perungudi (OMR) (OMR-1)', 600096),
       ('Mogappair (NorthWest Region)', 600037),
       ('Ashok Nagar (SouthWest Region)', 600083),
       ('MRC Nagar (SouthEast Region)', 600028),
       ('Strahans Road (NorthEast Region)', 600012),
       ('East Coast Road (ECR) (SouthEast Region)', 600119),
       ('Pallavaram (SouthWest Region)', 600043),
       ('Ramapuram (SouthWest Region)', 600089),
       ('Nanmangalam (SouthWest Region)', 600117),
       ('Thoraipakkam (OMR) (OMR-1)', 600097),
       ('Porur (SouthWest Region)', 600116),
       ('Padur (OMR) (OMR-3)', 603103),
       ('Thalambur (SouthEast Region)', 603103),
       ('Neelankarai (SouthEast Region)', 600041),
       ('Kasturba Nagar (SouthEast Region)', 600020),
       ('Alandur (SouthWest Region)', 600016),
       ('Mambalam (SouthWest Region)', 600033),
       ('Choolaimedu (SouthWest Region)', 600094),
       ('Tondiarpet (NorthEast Region)', 600081),
       ('Saligramam (SouthWest Region)', 600093),
       ('Maraimalai Nagar (SouthWest Region)', 603209),
       ('Keelakattalai (SouthWest Region)', 600117),
       ('Koyambedu (NorthWest Region)', 600107),
       ('Injambakkam (SouthEast Region)', 600115),
       ('Poonamalle (SouthWest Region)', 600056),
       ('Madhavaram (NorthWest Region)', 600060),
       ('Mahabalipuram (SouthEast Region)', 600097),
       ('Indira Nagar (OMR) (OMR-1)', 600020),
       ('Sholinganallur (OMR) (OMR-2)', 600119),
       ('Kotturpuram (SouthEast Region)', 600085),
       ('Tiruvallur (NorthWest Region)', 600062),
       ('Pallikaranai (SouthEast Region)', 600100),
       ('Guindy (SouthWest Region)', 600032),
       ('Rajakilpakkam (SouthWest Region)', 600073),
       ('Navalur (OMR) (OMR-2)', 600130),
       ('GST Road (SouthWest Region)', 603210),
       ('Manapakkam (SouthWest Region)', 603111),
       ('Valasaravakkam (SouthWest Region)', 600087),
       ('Kalpakkam (SouthEast Region)', 603102),
       ('Egattur (OMR) (OMR-3)', 603103),
       ('Perungalathur (SouthWest Region)', 600063),
       ('Kancheepuram (SouthWest Region)', 600091),
       ('Chengalpattu (SouthWest Region)', 603001),
       ('Kelambakkam (OMR) (OMR-3)', 631606),
       ('Sriperumbudur (SouthWest Region)', 600116),
       ('Vengaivasal Main RD (SouthWest Region)', 603202),
       ('Guduvancheri (SouthWest Region)', 603202),
       ('Tharamani (OMR) (OMR-1)', 600096),
       ('Vayalur (SouthEast Region)', 603102),
       ('Minjur (NorthEast Region)', 601203),
       ('Urapakkam (SouthWest Region)', 603210),
       ('Vinayagapuram (NorthWest Region)', 600081),
       ('NH-5 (NorthWest Region)', 600095),
       ('Thiruverkkadu (SouthWest Region)', 600077),
       ('Purasawalkam (NorthEast Region)', 600084),
       ('Korattur (NorthWest Region)', 600080),
       ('Semmancherry (OMR) (OMR-2)', 600119),
       ('Pudupakkam (SouthEast Region)', 600014),
       ('Balaji Nagar (NorthWest Region)', 600101),
       ('Siruseri SIPCOT (OMR) (OMR-3)', 603103),
       ('Cenotaph Road (SouthEast Region)', 600018),
       ('Kalavakkam (OMR) (OMR-3)', 600086),
       ('Villivakkam (NorthWest Region)', 600049),
       ('Vandalur (SouthWest Region)', 600048),
       ('Padappai (SouthWest Region)', 603210),
       ('Oragadam (SouthWest Region)', 600053),
       ('Nallambakkam (SouthEast Region)', 600048),
       ('Potheri (SouthWest Region)', 603203),
       ('Poonamallee High Road (NorthWest Region)', 600106),
       ('Vanagaram (SouthWest Region)', 600095),
       ('Camp Road (SouthWest Region)', 600073),
       ('Palavakkam (SouthEast Region)', 600041),
       ('Teynampet (SouthEast Region)', 600018),
       ('Maduravoyal (SouthWest Region)', 600095),
       ('Shantosapuram (SouthWest Region)', 600100),
       ('Avadi (NorthWest Region)', 600054),
       ('Ambattur (NorthWest Region)', 600054),
       ('Ekkatuthangal (SouthWest Region)', 600032),
       ('Kattupakkam (SouthWest Region)', 600056),
       ('Thiruvidandhai (SouthEast Region)', 603112),
       ('Perumbakkam (SouthEast Region)', 600100),
       ('Mambakkam (SouthEast Region)', 600048),
       ('Manikandan Nagar (SouthWest Region)', 600117),
       ('Chembarambakkam (SouthWest Region)', 600069),
       ('Nellikuppam (SouthEast Region)', 603202),
       ('Arasankazhani (OMR) (OMR-2)', 600119),
       ('Uthandi (SouthEast Region)', 600119),
       ('karapakkam (OMR) (OMR-2)', 600119),
       ('Pattabiram (NorthWest Region)', 600072),
       ('Santhome (SouthEast Region)', 600004),
       ('Tiruvottiyur (NorthEast Region)', 600019),
       ('Singaperumal Koil (SouthWest Region)', 603204),
       ('Iyappanthangal (SouthWest Region)', 600122),
       ('Aynambakkam (NorthWest Region)', 600095),
       ('Thiruporur (OMR) (OMR-3)', 603110),
       ('kottivakkam (SouthEast Region)', 600041),
       ('Kovilambakkam (SouthEast Region)', 600129),
       ('Manimangalam (SouthWest Region)', 600117),
       ('Thiruninravur (NorthWest Region)', 600072),
       ('Anakaputhur (SouthWest Region)', 600070),
       ('Kolathur (NorthWest Region)', 600099),
       ('Vedanthangal (SouthWest Region)', 603314),
       ('Muttukadu (SouthEast Region)', 603112),
       ('Sithalapakkam (SouthWest Region)', 600131),
       ('Madambakkam (SouthWest Region)', 600126),
       ('Uthiramerur (SouthWest Region)', 603107),
       ('Ponneri (NorthWest Region)', 601204),
       ('Thirumudivakkam (SouthWest Region)', 600069),
       ('Perur (SouthEast Region)', 603104),
       ('Thirumazhisai (SouthWest Region)', 600072),
       ('Kovur (SouthWest Region)', 600122),
       ('Sunguvarchatram (SouthWest Region)', 602106),
       ('Kovalam (SouthEast Region)', 603112),
       ('Mangadu (SouthWest Region)', 600122),
       ('Kundrathur (SouthWest Region)', 600069),
       ('Periyapalayam (NorthWest Region)', 601102),
       ('Mahindra World City (SouthWest Region)', 600002),
       ('Mannivakkam (SouthWest Region)', 600048),
       ('Ponmar (SouthEast Region)', 600048),
       ('Walajabad (SouthWest Region)', 631605),
       ('Rathinamangalam (SouthWest Region)', 600048),
       ('Gerugambakkam (SouthWest Region)', 600074),
       ('Polachery (SouthWest Region)', 600048),
       ('Kolapakkam (SouthWest Region)', 600074),
       ('Lakshmipuram (NorthWest Region)', 600017),
       ('Ayappakkam (NorthWest Region)', 600053),
       ('Mudichur (SouthWest Region)', 600048),
       ('Selaiyur (SouthWest Region)', 600073),
       ('Ottiambakkam (SouthEast Region)', 600024),
       ('Thirumullaivoyal (NorthWest Region)', 600116)]


# In[961]:


open_stock_units = pd.read_excel('file2.xlsx',sheet_name='Opening Stock',header=1,index_col=[1,2],skipfooter=178)

open_stock_units=open_stock_units.drop(columns='Unnamed: 0')

open_stock_units=open_stock_units.groupby(pd.PeriodIndex(open_stock_units.columns,freq='Q'),axis=1).sum()

open_stock_units


# In[962]:


osu = open_stock_units.T


# In[963]:


coldel = open_stock_units.index.values[1:]


# In[964]:


osu=osu.drop(columns=coldel)

osu.columns = ['open_stock_units']

osu['Micromarket']='Alwarpet (SouthEast Region)'

osu['cl_pincode']=600018

osu = osu.reset_index()

for i in range(len(coldel)):
    for k in range(len(col)):
        osu=osu.append(pd.Series([col[k],open_stock_units.loc[coldel[i]][k],coldel[i][0],coldel[i][1]], index=osu.columns), ignore_index=True)
        
osu


# In[493]:


open_stock_sqft = pd.read_excel('file2.xlsx',sheet_name='Opening Stock',header=1,index_col=[1,2],skiprows=173,skipfooter=5)

open_stock_sqft=open_stock_sqft.drop(columns='Unnamed: 0')

open_stock_sqft=open_stock_sqft.groupby(pd.PeriodIndex(open_stock_sqft.columns,freq='Q'),axis=1).sum()

open_stock_sqft


# In[494]:


osf = open_stock_sqft.T

osf=osf.drop(columns=coldel)

osf.columns = ['open_stock_mnsqft']

osf['Micromarket']='Alwarpet (SouthEast Region)'

osf['cl_pincode']=600018

osf = osf.reset_index()

osf


# In[495]:


for i in range(len(coldel)):
    for k in range(len(col)):
        osf=osf.append(pd.Series([col[k],open_stock_sqft.loc[coldel[i]][k],coldel[i][0],coldel[i][1]], index=osf.columns), ignore_index=True)
        
osf


# In[496]:


final = osu.copy()


# In[469]:


get_ipython().run_line_magic('pinfo', 'pd.merge')


# In[499]:


final=final.merge(osf,on=['index','Micromarket','cl_pincode'])


# In[503]:


final = final[['Micromarket','cl_pincode','index','open_stock_units','open_stock_mnsqft']]


# In[511]:


overhang = pd.read_excel('file2.xlsx',sheet_name='Overhang',header=1,index_col=[1,2],skipfooter=173)

overhang = overhang.drop(columns='Unnamed: 0')

overhang=overhang.groupby(pd.PeriodIndex(overhang.columns,freq='Q'),axis=1).sum()

overhang

cdel = overhang.index.values[1:]


# In[512]:


ov = overhang.T

ov=ov.drop(columns=cdel)

ov.columns = ['overhang']

ov['Micromarket']='Alwarpet (SouthEast Region)'

ov['cl_pincode']=600018

ov = ov.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        ov=ov.append(pd.Series([col[k],overhang.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=ov.columns), ignore_index=True)
        
ov


# In[513]:


final=final.merge(ov,on=['index','Micromarket','cl_pincode'])

final


# In[520]:


pricesft = pd.read_excel('file2.xlsx',sheet_name='Price',header=1,index_col=[1,2],skipfooter=351)

pricesft = pricesft.drop(columns='Unnamed: 0')

pricesft=pricesft.groupby(pd.PeriodIndex(pricesft.columns,freq='Q'),axis=1).mean()

pricesft


# In[525]:


cdel = pricesft.index.values[1:]

psft = pricesft.T

psft=psft.drop(columns=cdel)

psft.columns = ['New Launch Wt Average Price (/Sqft)']

psft['Micromarket']='Alwarpet (SouthEast Region)'

psft['cl_pincode']=600018

psft = psft.reset_index()



for i in range(len(cdel)):
    for k in range(len(col)):
        psft=psft.append(pd.Series([col[k],pricesft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=psft.columns), ignore_index=True)
        
psft


# In[530]:


final=final.merge(psft,on=['index','Micromarket','cl_pincode'],how='left')

final


# In[531]:


priceabsft = pd.read_excel('file2.xlsx',sheet_name='Price',header=1,index_col=[1,2],skiprows=171,skipfooter=178)

priceabsft=priceabsft.drop(columns='Unnamed: 0')

priceabsft=priceabsft.groupby(pd.PeriodIndex(priceabsft.columns,freq='Q'),axis=1).mean()

priceabsft


# In[532]:


cdel = priceabsft.index.values[1:]

pabsft = priceabsft.T

pabsft=pabsft.drop(columns=cdel)

pabsft.columns = ['Wt. Average Price Absorbed unit (INR/Sft)']

pabsft['Micromarket']='Alwarpet (SouthEast Region)'

pabsft['cl_pincode']=600018

pabsft = pabsft.reset_index()



for i in range(len(cdel)):
    for k in range(len(col)):
        pabsft=pabsft.append(pd.Series([col[k],priceabsft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=pabsft.columns), ignore_index=True)
        
pabsft


# In[533]:


final=final.merge(pabsft,on=['index','Micromarket','cl_pincode'])

final


# In[534]:


priceavsft = pd.read_excel('file2.xlsx',sheet_name='Price',header=1,index_col=[1,2],skiprows=344,skipfooter=5)

priceavsft=priceavsft.drop(columns='Unnamed: 0')

priceavsft=priceavsft.groupby(pd.PeriodIndex(priceavsft.columns,freq='Q'),axis=1).mean()

priceavsft


# In[535]:


cdel = priceavsft.index.values[1:]

pavsft = priceavsft.T

pavsft=pavsft.drop(columns=cdel)

pavsft.columns = ['Wt. Average Price Available unit (INR/Sft)']

pavsft['Micromarket']='Alwarpet (SouthEast Region)'

pavsft['cl_pincode']=600018

pavsft = pavsft.reset_index()



for i in range(len(cdel)):
    for k in range(len(col)):
        pavsft=pavsft.append(pd.Series([col[k],priceavsft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=pavsft.columns), ignore_index=True)
        
pavsft


# In[536]:


final=final.merge(pavsft,on=['index','Micromarket','cl_pincode'])

final


# In[555]:


final=final.rename(columns={'quarters':'index'})


# In[548]:


final.to_excel('final.xlsx')


# In[556]:


final


# In[550]:


launch_absorption_units = pd.read_excel('file2.xlsx',sheet_name='New Launch Absorption',header=1,index_col=[1,2],skipfooter=178)

launch_absorption_units = launch_absorption_units.drop(columns='Unnamed: 0')

launch_absorption_units=launch_absorption_units.groupby(pd.PeriodIndex(launch_absorption_units.columns,freq='Q'),axis=1).sum()

launch_absorption_units

cdel = launch_absorption_units.index.values[1:]


# In[552]:


lau = launch_absorption_units.T

lau=lau.drop(columns=cdel)

lau.columns = ['New Launch Absorption in Units']

lau['Micromarket']='Alwarpet (SouthEast Region)'

lau['cl_pincode']=600018

lau = lau.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        lau=lau.append(pd.Series([col[k],launch_absorption_units.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=lau.columns), ignore_index=True)
        
lau


# In[557]:


final=final.merge(lau,on=['index','Micromarket','cl_pincode'])

final


# In[561]:


launch_absorption_sqft = pd.read_excel('file2.xlsx',sheet_name='New Launch Absorption',header=1,index_col=[1,2],skiprows=173,skipfooter=5)

launch_absorption_sqft = launch_absorption_sqft.drop(columns='Unnamed: 0')

launch_absorption_sqft=launch_absorption_sqft.groupby(pd.PeriodIndex(launch_absorption_sqft.columns,freq='Q'),axis=1).sum()

cdel = launch_absorption_sqft.index.values[1:]

las = launch_absorption_sqft.T

las=las.drop(columns=cdel)

las.columns = ['New Launch Absorption in Mn Sqft']

las['Micromarket']='Alwarpet (SouthEast Region)'

las['cl_pincode']=600018

las = las.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        las=las.append(pd.Series([col[k],launch_absorption_sqft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=las.columns), ignore_index=True)
        
las

final=final.merge(las,on=['index','Micromarket','cl_pincode'])

final


# In[567]:


total_absorption_units = pd.read_excel('file2.xlsx',sheet_name='Total Absorptiom',header=1,index_col=[1,2],skipfooter=178)

total_absorption_units = total_absorption_units.drop(columns='Unnamed: 0')

total_absorption_units=total_absorption_units.groupby(pd.PeriodIndex(total_absorption_units.columns,freq='Q'),axis=1).sum()

cdel = total_absorption_units.index.values[1:]

tau = total_absorption_units.T

tau=tau.drop(columns=cdel)

tau.columns = ['Total Absorption in units']

tau['Micromarket']='Alwarpet (SouthEast Region)'

tau['cl_pincode']=600018

tau = tau.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        tau=tau.append(pd.Series([col[k],total_absorption_units.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=tau.columns), ignore_index=True)

final=final.merge(tau,on=['index','Micromarket','cl_pincode'])

final


# In[569]:


total_absorption_sqft = pd.read_excel('file2.xlsx',sheet_name='Total Absorptiom',header=1,index_col=[1,2],skiprows=173,skipfooter=5)

total_absorption_sqft = total_absorption_sqft.drop(columns='Unnamed: 0')

total_absorption_sqft=total_absorption_sqft.groupby(pd.PeriodIndex(total_absorption_sqft.columns,freq='Q'),axis=1).sum()

cdel = total_absorption_sqft.index.values[1:]

tas = total_absorption_sqft.T

tas=tas.drop(columns=cdel)

tas.columns = ['Total Absorption in Mn Sqft']

tas['Micromarket']='Alwarpet (SouthEast Region)'

tas['cl_pincode']=600018

tas = tas.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        tas=tas.append(pd.Series([col[k],total_absorption_sqft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=tas.columns), ignore_index=True)
        
final=final.merge(tas,on=['index','Micromarket','cl_pincode'])

final


# In[570]:


unsold_units = pd.read_excel('file2.xlsx',sheet_name='Unsold',header=1,index_col=[1,2],skipfooter=178)

unsold_units = unsold_units.drop(columns='Unnamed: 0')

unsold_units=unsold_units.groupby(pd.PeriodIndex(unsold_units.columns,freq='Q'),axis=1).sum()

cdel = unsold_units.index.values[1:]

uu = unsold_units.T

uu=uu.drop(columns=cdel)

uu.columns = ['Unsold in units']

uu['Micromarket']='Alwarpet (SouthEast Region)'

uu['cl_pincode']=600018

uu = uu.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        uu=uu.append(pd.Series([col[k],unsold_units.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=uu.columns), ignore_index=True)

final=final.merge(uu,on=['index','Micromarket','cl_pincode'])

final


# In[571]:


unsold_sqft = pd.read_excel('file2.xlsx',sheet_name='Unsold',header=1,index_col=[1,2],skiprows=173,skipfooter=5)

unsold_sqft = unsold_sqft.drop(columns='Unnamed: 0')

unsold_sqft=unsold_sqft.groupby(pd.PeriodIndex(unsold_sqft.columns,freq='Q'),axis=1).sum()

cdel = unsold_sqft.index.values[1:]

us = unsold_sqft.T

us=us.drop(columns=cdel)

us.columns = ['Unsold in Mn Sqft']

us['Micromarket']='Alwarpet (SouthEast Region)'

us['cl_pincode']=600018

us = us.reset_index()

for i in range(len(cdel)):
    for k in range(len(col)):
        us=us.append(pd.Series([col[k],unsold_sqft.loc[cdel[i]][k],cdel[i][0],cdel[i][1]], index=us.columns), ignore_index=True)
        
final=final.merge(us,on=['index','Micromarket','cl_pincode'])

final


# In[572]:


final.to_excel('final_updated.xlsx')


# In[1009]:


try1 = pd.read_excel('4june.xlsx',sheet_name='New Launch and its Absorption',header=1,usecols='B:L',skipfooter=2)

try1


# In[1010]:


quarters = try1['quarter'].copy()

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]
    
quarters

try1['index']=quarters
try1


# In[1001]:


try6 = FINAL.copy()


# In[1002]:


markets = try6['Micromarket'].copy()


markets


# In[1003]:


bracs =[]
for i in range(len(markets)):
    bracs.append(markets[i].index('(')-1)
bracs


# In[1004]:


data = []
for i in range(len(markets)):
    data.append(markets[i][:bracs[i]])

data


# In[1005]:


try6['MicroMarket'] = pd.Series(data)
try6


# In[1006]:


try6 = try6.drop(columns='Micromarket')
try6.columns


# In[1017]:


locs = try1['MicroMarket'].copy()

locs


# In[1021]:


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))
        
bracs1



data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

data1


# In[1025]:


try1['MicroMarket'] = pd.Series(data1)
try1


# In[1026]:


try1 = try1[['MicroMarket', 'index', 'tsw_new_units_<=30', 'tsw_new_units_30-40',
       'tsw_new_units_40-50', 'tsw_new_units_50-60', 'tsw_new_units_60-70',
       'tsw_new_units_70-80', 'tsw_new_units_80-90', 'tsw_new_units_90-1',
       'tsw_new_units_>1']]
try1


# In[1028]:


try7 = try6.merge(try1,on=['MicroMarket','index'],how='left')
try7


# In[1029]:


try7[try7['MicroMarket']=='Alwarpet']


# In[1030]:


try2 = pd.read_excel('4june.xlsx',sheet_name='New Launch and its Absorption',header=1,usecols='N:X',skipfooter=2)

try2


# In[1031]:


try2=try2.rename(columns={'MicroMarket ':'MicroMarket'})


# In[1032]:


quarters = try2['quarter.1'].copy()

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]

try2['index']=quarters

locs = try2['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try2['MicroMarket'] = pd.Series(data1)
try2


# In[1033]:


try2 = try2[['MicroMarket', 'index', 'tsw_new_mnsqft_<=30',
       'tsw_new_mnsqft_30-40', 'tsw_new_mnsqft_40-50', 'tsw_new_mnsqft_50-60',
       'tsw_new_mnsqft_60-70', 'tsw_new_mnsqft_70-80', 'tsw_new_mnsqft80-90',
       'tsw_new_mnsqft_90-1', 'tsw_new_mnsqft_>1']]


# In[1034]:


try7 = try7.merge(try2,on=['MicroMarket','index'],how='left')
try7


# In[1036]:


try3 = pd.read_excel('4june.xlsx',sheet_name='New Launch and its Absorption',header=1,usecols='Z:AJ',skipfooter=2)

try3


# In[1037]:


try3=try3.rename(columns={'MicroMarket.1':'MicroMarket'})

quarters = try3['quarter.2'].copy()

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]
    

try3['index']=quarters


locs = try3['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try3['MicroMarket'] = pd.Series(data1)
try3


# In[1038]:


try3 = try3[['MicroMarket', 'index', 'new_abs_units_<=30', 'new_abs_units_30-40',
       'new_abs_units_40-50', 'new_abs_units_50-60', 'new_abs_units_60-70',
       'new_abs_units_70-80', 'new_abs_units_80-90', 'new_abs_units_90-1',
       'new_abs_units_>1']]
try3


# In[1039]:


try7 = try7.merge(try3,on=['MicroMarket','index'],how='left')
try7


# In[1040]:


try4 = pd.read_excel('4june.xlsx',sheet_name='New Launch and its Absorption',header=1,usecols='AL:AV',skipfooter=2)

try4


# In[1041]:


try4=try4.rename(columns={'MicroMarket.2':'MicroMarket'})

quarters = try4['quarter.3'].copy()

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]
    
try4['index']=quarters

locs = try4['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try4['MicroMarket'] = pd.Series(data1)
try4


# In[1042]:


try4 = try4[['MicroMarket', 'index', 'new_abs_mnsqft_<=30',
       'new_abs_mnsqft_30-40', 'new_abs_mnsqft_40-50', 'new_abs_mnsqft_50-60',
       'new_abs_mnsqft_60-70', 'new_abs_mnsqft_70-80', 'new_abs_mnsqft_80-90',
       'new_abs_mnsqft_90-1', 'new_abs_mnsqft_>1']]


# In[1043]:


try7 = try7.merge(try4,on=['MicroMarket','index'],how='left')


# In[1044]:


try7


# In[1045]:


try8 = pd.read_excel('4june.xlsx',sheet_name='Total Absorption',header=2,usecols='B:L')

try8


# In[1046]:


quarters = try8['Quarter'].copy()

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]

try8['index']=quarters

locs = try8['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try8['MicroMarket'] = pd.Series(data1)
try8


# In[1047]:


try8 = try8[['MicroMarket', 'index', 'tsw_ta_units_<=30', 'tsw_ta_units_30-40',
       'tsw_ta_units_40-50', 'tsw_ta_units_50-60', 'tsw_ta_units_60-70',
       'tsw_ta_units_70-80', 'tsw_ta_units_80-90', 'tsw_ta_units_90-1',
       'tsw_ta_units_>1']]
try8


# In[998]:


FINAL


# In[1048]:


try7 = try7.merge(try8,on=['MicroMarket','index'],how='left')


# In[1061]:


try7


# In[1050]:


try9 = pd.read_excel('4june.xlsx',sheet_name='Total Absorption',header=2,usecols='O:Y')

try9


# In[1051]:


quarters = try9['Quarter.1'].copy()
try9 = try9.rename(columns={'MicroMarket.1':'MicroMarket'})

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]

try9['index']=quarters

locs = try9['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try9['MicroMarket'] = pd.Series(data1)
try9


# In[1053]:


try9 = try9[['MicroMarket', 'index', 'tsw_ta_mnsqft_<=30', 'tsw_ta_mnsqft_30-40',
       'tsw_ta_mnsqft_40-50', 'tsw_ta_mnsqft_50-60', 'tsw_ta_mnsqft_60-70',
       'tsw_ta_mnsqft_70-80', 'tsw_ta_mnsqft_80-90', 'tsw_ta_mnsqft_90-1',
       'tsw_ta_mnsqft_>1']]
try9


# In[1054]:


try7 = try7.merge(try9,on=['MicroMarket','index'],how='left')


# In[1056]:


try10 = pd.read_excel('4june.xlsx',sheet_name='Unsold',header=1,usecols='A:K')

try10


# In[1057]:


quarters = try10['quarter'].copy()
#try9 = try9.rename(columns={'MicroMarket.1':'MicroMarket'})

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]

try10['index']=quarters

locs = try10['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try10['MicroMarket'] = pd.Series(data1)
try10


# In[1059]:


try10 = try10[['MicroMarket', 'index', 'tsw_un_units_<=30', 'tsw_un_units_30-40',
       'tsw_un_units_40-50', 'tsw_un_units_50-60', 'tsw_un_units_60-70',
       'tsw_un_units_70-80', 'tsw_un_units_80-90', 'tsw_un_units_90-1',
       'tsw_un_units_>1']]
try10


# In[1060]:


try7 = try7.merge(try10,on=['MicroMarket','index'],how='left')


# In[1062]:


try11 = pd.read_excel('4june.xlsx',sheet_name='Unsold',header=1,usecols='M:W')

try11


# In[1063]:


quarters = try11['quarter.1'].copy()
try11 = try11.rename(columns={'MicroMarket.1':'MicroMarket'})

for i in range(len(quarters)):
    quarters[i]=quarters[i][3:]+quarters[i][:2]

try11['index']=quarters

locs = try11['MicroMarket'].copy()


bracs1 = []

for i in range(len(locs)):
    if '(' in locs[i]:
        bracs1.append(locs[i].index('(')-1)
    else:
        bracs1.append(len(locs[i]))

data1 = []
for i in range(len(locs)):
    data1.append(locs[i][:bracs1[i]])

try11['MicroMarket'] = pd.Series(data1)
try11


# In[1065]:


try11 = try11[['MicroMarket', 'index', 'tsw_un_mnsqft_<=30', 'tsw_un_mnsqft_30-40',
       'tsw_un_mnsqft_40-50', 'tsw_un_mnsqft_50-60', 'tsw_un_mnsqft_60-70',
       'tsw_un_mnsqft_70-80', 'tsw_un_mnsqft_80-90', 'tsw_un_mnsqft_90-1',
       'tsw_un_mnsqft_>1']]
try11


# In[1066]:


try7 = try7.merge(try11,on=['MicroMarket','index'],how='left')


# In[1067]:


try7


# In[1068]:


try7.to_excel('FINAL_updated.xlsx')


# In[1069]:


df = pd.read_excel('final_updated.xlsx')
df


# In[1099]:


get_ipython().run_line_magic('pinfo', 'df.fillna')


# In[1078]:


miss = pd.read_excel('final_updated.xlsx')
miss


# In[1089]:


fillm = miss.columns[15:87]


# In[1092]:


miss[fillm] = miss[fillm].fillna(0)


# In[1094]:


miss[miss['MicroMarket']=='Alwarpet'][fillm]


# In[1097]:


fillm = miss.columns[6:9]
fillm


# In[1101]:


missc = miss.copy()


# In[1102]:


missc[fillm] = missc.groupby('MicroMarket')[fillm].fillna(method='ffill')
missc


# In[1106]:


missc[missc['MicroMarket']=='Aminijkarai'][missc.columns[15:87]]


# In[1107]:


missc.to_excel('final2.xlsx')


# In[1108]:


dataset = missc.copy()


# In[1110]:


dataset.columns[87:]


# In[1111]:


dataset.columns[:87]


# In[1114]:


dataset.dtypes


# In[1115]:


TNdata


# In[1125]:


TNdata[['cl_pincode','hospital']].groupby('cl_pincode')['hospital'].value_counts().idxmax()


# In[1118]:


quantta.dtypes


# In[1135]:


re = TNdata[['cl_pincode','BPL_count',
'Airport',
'Commercial_area',
'Commercial_Complex',
'Forest',
'Industry',
'Other',
'Parks_Play_Grounds',
'Residential_area',
'Residential_complex',
'Residential_congested_area',
'Slums',
'Under_Construction_Area',
'Vacant_Land',
'Water_Body',
'Hotel_Star_Null-2',
'hotel_star_3',
'hotel_star_4',
'hotel_star_5',
'hotel_price_0_2k',
'hotel_price_2_4k',
'hotel_price_4_max',
'sale_property_0_20l',
'Sale_Property_20_50L',
'Sale_Property_50_80L',
'Sale_Property_80L_1.25Cr',
'sale_property_1.25cr_20cr',
'Sale_Property_Below3K',
'Sale_Property_3k-5k',
'Sale_Property_5k-8k',
'Sale_Property_8k-13k',
'Sale_Property_13k_Abv',
'Rent_Property_Lessthan_5K',
'Rent_Property_5K_16K',
'rent_property_16k_30k',
'rent_property_30k_60k',
'rent_property_60k_90k',
'Rent_Property_90_1.5L',
'rental_per_sqft_blw_15',
'rental_per_sqft_15-30',
'rental_per_sqft_30-50',
'rental_per_sqft_50-100',
'rental_per_sqft_100_abv',
'airport',
'atm',
'bank',
'clinic',
'education_institute',
'hospital',
'hotel',
'industry',
'mall',
'medical_specialist',
'msme',
'nbfc',
'park',
'pharmacy',
'post_office',
'recreation',
'retail_store',
'school',
'service_centers',
'service_providers',
'special_economic_zone',
'tourism',
'traffic_junctions',
'buddhist',
'christian',
'hindu',
'jain',
'muslim',
'sikh']].copy()
re


# In[1136]:


re = re.fillna(0)


# In[1141]:


re2 = re.groupby('cl_pincode')[re.columns[1:]].agg(lambda x: x.value_counts().idxmax())
re2


# In[1142]:


re2.columns


# In[1143]:


dataset.columns[87:]


# In[1146]:


dataset = dataset.merge(re2,on='cl_pincode')


# In[1149]:


dataset.to_excel('final3.xlsx')


# In[1150]:


dataset = dataset.drop(columns='cl_CITY')


# In[1237]:


dset = pd.read_excel('final3.xlsx')
dset


# In[1238]:


toadd = quantta[['cl_pincode','Rural_urban _classification']]
toadd


# In[1239]:


dset = dset.merge(toadd,on='cl_pincode')
dset


# In[1299]:


dset1 = dset.copy()


# In[1300]:


dummies = pd.get_dummies(dset1['Rural_urban _classification'])
dummies.columns


# In[1301]:


dset1[['rural', 'semi_urban', 'urban']]=dummies


# In[1302]:


dset1.to_excel('final4.xlsx')


# In[1308]:


dset1=pd.read_excel('final4.xlsx')


# In[1309]:


dset1 = dset1.dropna(axis=0)


# In[1310]:


dset1


# In[1311]:


X = dset1.iloc[:,3:-2]


# In[1312]:


X


# In[1313]:


y = dset1.iloc[:,-2]
y


# In[1314]:


from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression


# In[1315]:


from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linreg = LinearRegression().fit(X_train_scaled, y_train)

print('linear model coeff (w): {}'
     .format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test_scaled, y_test)))


# In[1317]:


coeff_df = pd.DataFrame(linreg.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1335]:


from sklearn.linear_model import Ridge
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                   random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linridge = Ridge(alpha=10.0).fit(X_train_scaled, y_train)

print('ridge regression linear model intercept: {}'
     .format(linridge.intercept_))
print('ridge regression linear model coeff:\n{}'
     .format(linridge.coef_))
print('R-squared score (training): {:.3f}'
     .format(linridge.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linridge.score(X_test_scaled, y_test)))
print('Number of non-zero features: {}'
     .format(np.sum(linridge.coef_ != 0)))


# In[1267]:


print('Ridge regression: effect of alpha regularization parameter\n')
for this_alpha in [0, 1, 10, 20, 50, 100, 1000]:
    linridge = Ridge(alpha = this_alpha).fit(X_train_scaled, y_train)
    r2_train = linridge.score(X_train_scaled, y_train)
    r2_test = linridge.score(X_test_scaled, y_test)
    num_coeff_bigger = np.sum(abs(linridge.coef_) > 1.0)
    print('Alpha = {:.2f}\nnum abs(coeff) > 1.0: {}, r-squared training: {:.2f}, r-squared test: {:.2f}\n'
         .format(this_alpha, num_coeff_bigger, r2_train, r2_test))


# In[1336]:


coeff_df = pd.DataFrame(linridge.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1339]:


from sklearn.linear_model import Lasso

linlasso = Lasso(alpha=0.1, max_iter = 10000).fit(X_train_scaled, y_train)
print('lasso regression linear model intercept: {}'
     .format(linlasso.intercept_))
print('lasso regression linear model coeff:\n{}'
     .format(linlasso.coef_))
print('Non-zero features: {}'
     .format(np.sum(linlasso.coef_ != 0)))
print('R-squared score (training): {:.3f}'
     .format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}\n'
     .format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero weight (sorted by absolute magnitude):')

for e in sorted (list(zip(list(X), linlasso.coef_)),
                key = lambda e: -abs(e[1])):
    if e[1] != 0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))


# In[1210]:


print('Lasso regression: effect of alpha regularization\nparameter on number of features kept in final model\n')

for alpha in [0.1, 0.5, 1, 2, 3, 5, 10, 20, 50]:
    linlasso = Lasso(alpha, max_iter = 10000).fit(X_train_scaled, y_train)
    r2_train = linlasso.score(X_train_scaled, y_train)
    r2_test = linlasso.score(X_test_scaled, y_test)
    
    print('Alpha = {:.2f}\nFeatures kept: {}, r-squared training: {:.2f}, r-squared test: {:.2f}\n'
         .format(alpha, np.sum(linlasso.coef_ != 0), r2_train, r2_test))


# In[1340]:


coeff_df = pd.DataFrame(linlasso.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1231]:


from sklearn.model_selection import cross_val_score

clf = LinearRegression()

cv_scores = cross_val_score(clf, X, y, cv=5)

print('Cross-validation scores (3-fold):', cv_scores)
print('Mean cross-validation score (3-fold): {:.3f}'
     .format(np.mean(cv_scores)))


# In[1269]:


from sklearn.ensemble import RandomForestRegressor


# In[1341]:


clf = RandomForestRegressor(max_features=210, random_state=0).fit(X_train, y_train)
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[1342]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False)


# In[1343]:


from sklearn.ensemble import GradientBoostingRegressor


# In[1344]:


clf = GradientBoostingRegressor(random_state=0).fit(X_train, y_train)
print('Accuracy of GBDT classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of GBDT classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[1295]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False)


# # Without absorption columns

# In[1351]:


dset2 = dset1.copy()
dset2.columns[49:67]


# In[1357]:


dset2 = dset2.drop(columns=dset2.columns[49:67])
dset2


# In[1358]:


X = dset2.iloc[:,3:-2]
y = dset2.iloc[:,-2]


# In[1359]:


X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 0)

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

linreg = LinearRegression().fit(X_train_scaled, y_train)

print('linear model coeff (w): {}'
     .format(linreg.coef_))
print('linear model intercept (b): {:.3f}'
     .format(linreg.intercept_))
print('R-squared score (training): {:.3f}'
     .format(linreg.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linreg.score(X_test_scaled, y_test)))


# In[1360]:


coeff_df = pd.DataFrame(linreg.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1361]:


linridge = Ridge(alpha=10.0).fit(X_train_scaled, y_train)

print('ridge regression linear model intercept: {}'
     .format(linridge.intercept_))
print('ridge regression linear model coeff:\n{}'
     .format(linridge.coef_))
print('R-squared score (training): {:.3f}'
     .format(linridge.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}'
     .format(linridge.score(X_test_scaled, y_test)))
print('Number of non-zero features: {}'
     .format(np.sum(linridge.coef_ != 0)))


# In[1362]:


print('Ridge regression: effect of alpha regularization parameter\n')
for this_alpha in [0, 1, 10, 20, 50, 100, 1000]:
    linridge = Ridge(alpha = this_alpha).fit(X_train_scaled, y_train)
    r2_train = linridge.score(X_train_scaled, y_train)
    r2_test = linridge.score(X_test_scaled, y_test)
    num_coeff_bigger = np.sum(abs(linridge.coef_) > 1.0)
    print('Alpha = {:.2f}\nnum abs(coeff) > 1.0: {}, r-squared training: {:.2f}, r-squared test: {:.2f}\n'
         .format(this_alpha, num_coeff_bigger, r2_train, r2_test))


# In[1363]:


coeff_df = pd.DataFrame(linridge.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1366]:


linlasso = Lasso(alpha=0.1, max_iter = 10000).fit(X_train_scaled, y_train)
print('lasso regression linear model intercept: {}'
     .format(linlasso.intercept_))
print('lasso regression linear model coeff:\n{}'
     .format(linlasso.coef_))
print('Non-zero features: {}'
     .format(np.sum(linlasso.coef_ != 0)))
print('R-squared score (training): {:.3f}'
     .format(linlasso.score(X_train_scaled, y_train)))
print('R-squared score (test): {:.3f}\n'
     .format(linlasso.score(X_test_scaled, y_test)))
print('Features with non-zero weight (sorted by absolute magnitude):')

for e in sorted (list(zip(list(X), linlasso.coef_)),
                key = lambda e: -abs(e[1])):
    if e[1] != 0:
        print('\t{}, {:.3f}'.format(e[0], e[1]))


# In[1365]:


print('Lasso regression: effect of alpha regularization\nparameter on number of features kept in final model\n')

for alpha in [0.1, 0.5, 1, 2, 3, 5, 10, 20, 50]:
    linlasso = Lasso(alpha, max_iter = 10000).fit(X_train_scaled, y_train)
    r2_train = linlasso.score(X_train_scaled, y_train)
    r2_test = linlasso.score(X_test_scaled, y_test)
    
    print('Alpha = {:.2f}\nFeatures kept: {}, r-squared training: {:.2f}, r-squared test: {:.2f}\n'
         .format(alpha, np.sum(linlasso.coef_ != 0), r2_train, r2_test))


# In[1367]:


coeff_df = pd.DataFrame(linlasso.coef_,X.columns,columns=['Coefficient'])
coeff_df.sort_values(by=['Coefficient'],ascending=False)


# In[1376]:


clf = RandomForestRegressor(max_features=100,random_state=0).fit(X_train, y_train)
print('Accuracy of RF classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of RF classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[1377]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False)


# In[1382]:


clf = GradientBoostingRegressor(learning_rate=0.1, random_state=0).fit(X_train, y_train)
print('Accuracy of GBDT classifier on training set: {:.2f}'
     .format(clf.score(X_train, y_train)))
print('Accuracy of GBDT classifier on test set: {:.2f}'
     .format(clf.score(X_test, y_test)))


# In[1383]:


imp_df = pd.DataFrame(clf.feature_importances_,X.columns,columns=['Importance'])
imp_df.sort_values(by=['Importance'],ascending=False)


# In[ ]:




