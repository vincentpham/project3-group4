DROP TABLE IF EXISTS USCities;
DROP TABLE IF EXISTS USProperties_Data;
DROP TABLE IF EXISTS USCities_lat_long;
DROP TABLE IF EXISTS USCities_Ave_Prices;
CREATE TABLE USCities(
ID DECIMAL,
city VARCHAR,
state VARCHAR,
Ave_Price_2000 DECIMAL,
Ave_Price_2001 DECIMAL,
Ave_Price_2002 DECIMAL,
Ave_Price_2003 DECIMAL,
Ave_Price_2004 DECIMAL,
Ave_Price_2005 DECIMAL,
Ave_Price_2006 DECIMAL,
Ave_Price_2007 DECIMAL,
Ave_Price_2008 DECIMAL,
Ave_Price_2009 DECIMAL,
Ave_Price_2010 DECIMAL,
Ave_Price_2011 DECIMAL,
Ave_Price_2012 DECIMAL,
Ave_Price_2013 DECIMAL,
Ave_Price_2014 DECIMAL,
Ave_Price_2015 DECIMAL,
Ave_Price_2016 DECIMAL,
Ave_Price_2017 DECIMAL,
Ave_Price_2018 DECIMAL,
Ave_Price_2019 DECIMAL,
Ave_Price_2020 DECIMAL,
Ave_Price_2021 DECIMAL,
Ave_Price_2022 DECIMAL,
Ave_Price_2023 DECIMAL,
Total_Ave_Price DECIMAL,
lat DECIMAL,
lng DECIMAL,
population DECIMAL,
density DECIMAL
);

SELECT * from USCities;

CREATE TABLE USProperties_Data(
property_id DECIMAL,
address VARCHAR,
city VARCHAR,
state VARCHAR,
latitude DECIMAL,
longitude DECIMAL,
postcode VARCHAR,
price DECIMAL,
bedroom_number INT,
bathroom_number INT,
living_space DECIMAL,
land_space DECIMAL,
land_space_unit VARCHAR,
property_type VARCHAR,
property_status VARCHAR
);

SELECT * from USProperties_Data;

CREATE TABLE USCities_lat_long(
city VARCHAR,
lat DECIMAL,
lng DECIMAL,
population INT,
density DECIMAL
);

SELECT * from USCities_lat_long;

CREATE TABLE USCities_Ave_Prices(
ID DECIMAL,
city VARCHAR,
state VARCHAR,
Ave_Price_2000 DECIMAL,
Ave_Price_2001 DECIMAL,
Ave_Price_2002 DECIMAL,
Ave_Price_2003 DECIMAL,
Ave_Price_2004 DECIMAL,
Ave_Price_2005 DECIMAL,
Ave_Price_2006 DECIMAL,
Ave_Price_2007 DECIMAL,
Ave_Price_2008 DECIMAL,
Ave_Price_2009 DECIMAL,
Ave_Price_2010 DECIMAL,
Ave_Price_2011 DECIMAL,
Ave_Price_2012 DECIMAL,
Ave_Price_2013 DECIMAL,
Ave_Price_2014 DECIMAL,
Ave_Price_2015 DECIMAL,
Ave_Price_2016 DECIMAL,
Ave_Price_2017 DECIMAL,
Ave_Price_2018 DECIMAL,
Ave_Price_2019 DECIMAL,
Ave_Price_2020 DECIMAL,
Ave_Price_2021 DECIMAL,
Ave_Price_2022 DECIMAL,
Ave_Price_2023 DECIMAL,
Total_Ave_Price DECIMAL
);

SELECT * from USCities_Ave_Prices;