#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import dependencies
import pandas as pd
import numpy as np
pd.set_option('max_colwidth', 400)
file1="City_zhvi_uc_sfrcondo_tier_0.33_0.67_sm_sa_month.csv"
file2="../Project-3-Group-4/uscities_main.csv"
file3="../Project-3-Group-4/600K US Housing Properties.csv"


# ### Extract the crowdfunding.xlsx Data

# In[2]:


uscities_prices = pd.read_csv(file1)
uscities_prices


# In[3]:


uscities_prices.columns


# In[4]:


uscities_lat_long = pd.read_csv(file2)
uscities_lat_long.head(5)


# In[5]:


uscities_lat_long.columns


# In[6]:


US_Housing_Properties = pd.read_csv(file3)
US_Housing_Properties.head()


# In[7]:


US_Housing_Properties.columns


# In[10]:


# Drop unwanted columns
uscities_newcolumns_df = uscities_prices_df.drop(columns=["SizeRank","RegionType","State","Metro","CountyName"])
uscities_newcolumns_df


# In[ ]:


uscities_renamecolumns_df = uscities_newcolumns_df.rename(columns={"RegionID": "ID","RegionName":"city","StateName":"state"})
uscities_renamecolumns_df


# In[9]:


#Drop non values
uscities_dropnanvalue_df = uscities_renamecolumns_df.dropna()
uscities_dropnanvalue_df


# In[ ]:


uscities_dropnanvalue_df.dtypes


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2000"] = uscities_dropnanvalue_df.loc[:, ["2000-01-31","2000-02-29","2000-03-31",
                                                     "2000-04-30","2000-05-31","2000-06-30","2000-07-31","2000-08-31",
                                                     "2000-09-30","2000-10-31","2000-11-30","2000-12-31"]].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2001"] = uscities_dropnanvalue_df.loc[:, ("2001-01-31","2001-02-28","2001-03-31",
                                                     "2001-04-30","2001-05-31","2001-06-30","2001-07-31","2001-08-31",
                                                     "2001-09-30","2001-10-31","2001-11-30","2001-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2002"] = uscities_dropnanvalue_df.loc[:, ("2002-01-31","2002-02-28","2002-03-31",
                                                     "2002-04-30","2002-05-31","2002-06-30","2002-07-31","2002-08-31",
                                                     "2002-09-30","2002-10-31","2002-11-30","2002-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2003"] = uscities_dropnanvalue_df.loc[:, ("2003-01-31","2003-02-28","2003-03-31",
                                                     "2003-04-30","2003-05-31","2003-06-30","2003-07-31","2003-08-31",
                                                     "2003-09-30","2003-10-31","2003-11-30","2003-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2004"] = uscities_dropnanvalue_df.loc[:, ("2004-01-31","2004-02-29","2004-03-31",
                                                     "2004-04-30","2004-05-31","2004-06-30","2004-07-31","2004-08-31",
                                                     "2004-09-30","2004-10-31","2004-11-30","2004-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2005"] = uscities_dropnanvalue_df.loc[:, ("2005-01-31","2005-02-28","2005-03-31",
                                                     "2005-04-30","2005-05-31","2005-06-30","2005-07-31","2004-08-31",
                                                     "2005-09-30","2005-10-31","2005-11-30","2005-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2006"] = uscities_dropnanvalue_df.loc[:, ("2006-01-31","2006-02-28","2006-03-31",
                                                     "2006-04-30","2006-05-31","2006-06-30","2006-07-31","2006-08-31",
                                                     "2006-09-30","2006-10-31","2006-11-30","2006-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2007"] = uscities_dropnanvalue_df.loc[:, ("2007-01-31","2007-02-28","2007-03-31",
                                                     "2007-04-30","2007-05-31","2007-06-30","2007-07-31","2007-08-31",
                                                     "2007-09-30","2007-10-31","2007-11-30","2007-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2008"] = uscities_dropnanvalue_df.loc[:, ("2008-01-31","2008-02-29","2008-03-31",
                                                     "2008-04-30","2008-05-31","2008-06-30","2008-07-31","2008-08-31",
                                                     "2008-09-30","2008-10-31","2008-11-30","2008-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2009"] = uscities_dropnanvalue_df.loc[:, ("2009-01-31","2009-02-28","2009-03-31",
                                                     "2009-04-30","2009-05-31","2009-06-30","2009-07-31","2009-08-31",
                                                     "2009-09-30","2009-10-31","2009-11-30","2009-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2010"] = uscities_dropnanvalue_df.loc[:, ("2010-01-31","2010-02-28","2010-03-31",
                                                     "2010-04-30","2010-05-31","2010-06-30","2010-07-31","2010-08-31",
                                                     "2010-09-30","2010-10-31","2010-11-30","2010-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2011"] = uscities_dropnanvalue_df.loc[:, ("2011-01-31","2011-02-28","2011-03-31",
                                                     "2011-04-30","2011-05-31","2011-06-30","2011-07-31","2011-08-31",
                                                     "2011-09-30","2011-10-31","2011-11-30","2011-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2012"] = uscities_dropnanvalue_df.loc[:, ("2012-01-31","2012-02-29","2012-03-31",
                                                     "2012-04-30","2012-05-31","2012-06-30","2012-07-31","2012-08-31",
                                                     "2012-09-30","2012-10-31","2012-11-30","2012-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2013"] = uscities_dropnanvalue_df.loc[:, ("2013-01-31","2013-02-28","2013-03-31",
                                                     "2013-04-30","2013-05-31","2013-06-30","2013-07-31","2013-08-31",
                                                     "2013-09-30","2013-10-31","2013-11-30","2013-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2014"] = uscities_dropnanvalue_df.loc[:, ("2014-01-31","2014-02-28","2014-03-31",
                                                     "2014-04-30","2014-05-31","2014-06-30","2014-07-31","2014-08-31",
                                                     "2014-09-30","2014-10-31","2014-11-30","2014-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2015"] = uscities_dropnanvalue_df.loc[:, ("2015-01-31","2015-02-28","2015-03-31",
                                                     "2015-04-30","2015-05-31","2015-06-30","2015-07-31","2015-08-31",
                                                     "2015-09-30","2015-10-31","2015-11-30","2015-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2016"] = uscities_dropnanvalue_df.loc[:, ("2016-01-31","2016-02-29","2016-03-31",
                                                     "2016-04-30","2016-05-31","2016-06-30","2016-07-31","2016-08-31",
                                                     "2016-09-30","2016-10-31","2016-11-30","2016-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2017"] = uscities_dropnanvalue_df.loc[:, ("2017-01-31","2017-02-28","2017-03-31",
                                                     "2017-04-30","2017-05-31","2017-06-30","2017-07-31","2017-08-31",
                                                     "2017-09-30","2017-10-31","2017-11-30","2017-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2018"] = uscities_dropnanvalue_df.loc[:, ("2018-01-31","2018-02-28","2018-03-31",
                                                     "2018-04-30","2018-05-31","2018-06-30","2018-07-31","2018-08-31",
                                                     "2018-09-30","2018-10-31","2018-11-30","2018-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2019"] = uscities_dropnanvalue_df.loc[:, ("2019-01-31","2019-02-28","2019-03-31",
                                                     "2019-04-30","2019-05-31","2019-06-30","2019-07-31","2019-08-31",
                                                     "2019-09-30","2019-10-31","2019-11-30","2019-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2020"] = uscities_dropnanvalue_df.loc[:, ("2020-01-31","2020-02-29","2020-03-31",
                                                     "2020-04-30","2020-05-31","2020-06-30","2020-07-31","2020-08-31",
                                                     "2020-09-30","2020-10-31","2020-11-30","2020-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2021"] = uscities_dropnanvalue_df.loc[:, ("2021-01-31","2021-02-28","2021-03-31",
                                                     "2021-04-30","2021-05-31","2021-06-30","2021-07-31","2021-08-31",
                                                     "2021-09-30","2021-10-31","2021-11-30","2021-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2022"] = uscities_dropnanvalue_df.loc[:, ("2022-01-31","2022-02-28","2022-03-31",
                                                     "2022-04-30","2022-05-31","2022-06-30","2022-07-31","2022-08-31",
                                                     "2022-09-30","2022-10-31","2022-11-30","2022-12-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df["Ave_Price_2023"] = uscities_dropnanvalue_df.loc[:, ("2023-01-31","2023-02-28","2023-03-31",
                                                     "2023-04-30","2023-05-31","2023-06-30","2023-07-31","2023-08-31")].mean(axis = 1)


# In[ ]:


uscities_dropnanvalue_df


# In[ ]:


uscities_means_df = uscities_dropnanvalue_df[["ID","city","state","Ave_Price_2000","Ave_Price_2001","Ave_Price_2002","Ave_Price_2003",
                                             "Ave_Price_2004","Ave_Price_2005","Ave_Price_2006","Ave_Price_2007",
                                              "Ave_Price_2008","Ave_Price_2009","Ave_Price_2010","Ave_Price_2011",
                                             "Ave_Price_2012","Ave_Price_2013","Ave_Price_2014","Ave_Price_2015",
                                              "Ave_Price_2016","Ave_Price_2017","Ave_Price_2018","Ave_Price_2019",
                                              "Ave_Price_2020","Ave_Price_2021","Ave_Price_2022","Ave_Price_2023"
                                             ]]


# In[ ]:


uscities_means_df["Total_Ave_Price"] = uscities_means_df.loc[:, ("Ave_Price_2000","Ave_Price_2001","Ave_Price_2002","Ave_Price_2003",
                                             "Ave_Price_2004","Ave_Price_2005","Ave_Price_2006","Ave_Price_2007",
                                              "Ave_Price_2008","Ave_Price_2009","Ave_Price_2010","Ave_Price_2011",
                                             "Ave_Price_2012","Ave_Price_2013","Ave_Price_2014","Ave_Price_2015",
                                              "Ave_Price_2016","Ave_Price_2017","Ave_Price_2018","Ave_Price_2019",
                                              "Ave_Price_2020","Ave_Price_2021","Ave_Price_2022","Ave_Price_2023")].mean(axis = 1)


# In[ ]:


USCities_AvePrices = uscities_means_df


# In[ ]:


USCities_AvePrices.to_csv("output/USCities_AvePrices.csv", index=False)


# In[ ]:


USCities_AvePrices


# In[ ]:


#greate a data frame 
usc_lat_long_df = pd.DataFrame(data=uscities_lat_long)


# In[ ]:


#drop nan values,
usc_lat_long_drop = usc_lat_long_df.dropna()


# In[ ]:


usc_lat_long_drop.columns


# In[ ]:


usc_lat_long_columns = usc_lat_long_drop.drop(columns=['city_ascii', 'state_id', 'state_name', 'county_fips',
       'county_name', 'source',
       'military', 'incorporated', 'timezone', 'ranking', 'zips', 'id'])
usc_lat_long = usc_lat_long_columns
usc_lat_long


# In[ ]:


usc_lat_long.to_csv("output/USCities_lat_long.csv", index=False)


# In[ ]:


#merge both data on city column:
USCities_data = USCities_AvePrices.merge(usc_lat_long, how='outer', on='city')
USCities_data


# In[ ]:


USCities = USCities_data.drop_duplicates(subset=['ID'])


# In[ ]:


USCities


# In[ ]:


USCities.to_csv("output/USCities.csv", index=False)


# In[ ]:


US_Housing_Properties.columns


# In[ ]:


US_Housing_Properties_columns = US_Housing_Properties.drop(columns=['property_url','street_name', 'apartment', 'price_per_unit', 'broker_id', 'year_build', 'total_num_units', 'listing_age',
       'RunDate', 'agency_name', 'agent_name', 'agent_phone',
       'is_owned_by_zillow'])



# In[ ]:


US_Housing_Properties_columns


# In[ ]:


US_Properties = US_Housing_Properties_columns.dropna()


# In[ ]:


US_Properties.dtypes


# In[ ]:


US_Properties_type = US_Properties.astype({'bedroom_number': 'int64', 'bathroom_number': 'int64' })


# In[ ]:


USProperties_Data = US_Properties_type
USProperties_Data


# In[11]:


from pymongo import MongoClient


# In[12]:


mongo=MongoClient(port=27017)


# In[13]:


from pprint import pprint


# In[14]:


db1=mongo.AvePrice


# In[15]:


db1.list_collection_names()


# In[16]:


houseprice=db1.houseprices


# In[17]:


houseprice.count_documents({})          


# In[ ]:





# In[18]:


query1={}
field1={'id':1,'city':1,'state':1,'Ave_Price_2000':1}


# In[19]:


result1=houseprice.find(query1,field1)


# In[20]:





# In[ ]:





# In[21]:


query2={}
field2={'id':1,'city':1,'state':1,'Ave_Price_2001':1}


# In[22]:


result2=houseprice.find(query2,field2)


# In[23]:


query3={}
field3={'id':1,'city':1,'state':1,'Ave_Price_2002':1}


# In[24]:


result3=houseprice.find(query3,field3)


# In[25]:


query4={}
field4={'id':1,'city':1,'state':1,'Ave_Price_2003':1}


# In[26]:


result4=houseprice.find(query4,field4)


# In[27]:


query5={}
field5={'id':1,'city':1,'state':1,'Ave_Price_2004':1}


# In[28]:


result5=houseprice.find(query5,field5)


# In[29]:


query6={}
field6={'id':1,'city':1,'state':1,'Ave_Price_2005':1}


# In[30]:


result6=houseprice.find(query6,field6)


# In[31]:


query7={}
field7={'id':1,'city':1,'state':1,'Ave_Price_2006':1}


# In[32]:


result7=houseprice.find(query7,field7)


# In[33]:


query8={}
field8={'id':1,'city':1,'state':1,'Ave_Price_2007':1}


# In[34]:


result8=houseprice.find(query8,field8)


# In[35]:


query9={}
field9={'id':1,'city':1,'state':1,'Ave_Price_2008':1}


# In[36]:


result9=houseprice.find(query9,field9)


# In[37]:


query10={}
field10={'id':1,'city':1,'state':1,'Ave_Price_2009':1}


# In[38]:


result10=houseprice.find(query10,field10)


# In[39]:


query11={}
field11={'id':1,'city':1,'state':1,'Ave_Price_2010':1}


# In[40]:


result11=houseprice.find(query11,field11)


# In[41]:


query12={}
field12={'id':1,'city':1,'state':1,'Ave_Price_2011':1}


# In[42]:


result12=houseprice.find(query12,field12)


# In[43]:


query13={}
field13={'id':1,'city':1,'state':1,'Ave_Price_2012':1}


# In[44]:


result13=houseprice.find(query13,field13)


# In[45]:


query14={}
field14={'id':1,'city':1,'state':1,'Ave_Price_2013':1}


# In[46]:


result14=houseprice.find(query14,field14)


# In[47]:


query15={}
field15={'id':1,'city':1,'state':1,'Ave_Price_2014':1}


# In[48]:


result15=houseprice.find(query15,field15)


# In[49]:


query16={}
field16={'id':1,'city':1,'state':1,'Ave_Price_2015':1}


# In[50]:


result16=houseprice.find(query16,field16)


# In[51]:


query17={}
field17={'id':1,'city':1,'state':1,'Ave_Price_2016':1}


# In[52]:


result17=houseprice.find(query17,field17)


# In[53]:


query18={}
field18={'id':1,'city':1,'state':1,'Ave_Price_2017':1}


# In[54]:


result18=houseprice.find(query18,field18)


# In[55]:


query19={}
field19={'id':1,'city':1,'state':1,'Ave_Price_2018':1}


# In[56]:


result19=houseprice.find(query19,field19)


# In[57]:


query20={}
field20={'id':1,'city':1,'state':1,'Ave_Price_2019':1}


# In[58]:


result20=houseprice.find(query20,field20)


# In[59]:


query21={}
field21={'id':1,'city':1,'state':1,'Ave_Price_2020':1}


# In[60]:


result21=houseprice.find(query21,field21)


# In[61]:


query22={}
field22={'id':1,'city':1,'state':1,'Ave_Price_2021':1}


# In[62]:


result22=houseprice.find(query22,field22)


# In[63]:


query23={}
field23={'id':1,'city':1,'state':1,'Ave_Price_2022':1}


# In[64]:


result23=houseprice.find(query23,field23)


# In[65]:


query24={}
field24={'id':1,'city':1,'state':1,'Ave_Price_2023':1}


# In[66]:


result24=houseprice.find(query24,field24)


# In[67]:


query25={}
field25={'id':1,'city':1,'state':1,'Total_Ave_Price':1}


# In[68]:


result25=houseprice.find(query25,field25)


# In[2]:


 result=[]


for i in result1:
   result.append(i)



pprint(result[0:5])









