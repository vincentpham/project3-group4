from pymongo import MongoClient
from flask_cors import CORS

# In[2]:


mongo=MongoClient(port=27017)


# In[8]:


print(mongo.list_database_names())


# In[3]:





# In[9]:


db1=mongo.us


# In[10]:





# In[11]:


city=db1.cities


# In[12]:


city.count_documents({})


# In[ ]:





# In[17]:


query={}
field={'_id':0}


# In[18]:


result=list(city.find(query,field))


db2=mongo.usproperties


# In[23]:


db2.list_collection_names()


# In[24]:


usproperty=db2.properties


# In[25]:


usproperty.count_documents({})


# In[26]:


query_1={}


# In[27]:


field_1={'_id':0}


# In[28]:


result_1=list(usproperty.find(query_1,field_1))


# In[29]:

db3=mongo.us1

geo_loc=db3.geo

query_3={}

field_3={'_id':0,'longitude':1,'latitude':1,'change':1}

result_3=list(geo_loc.find(query_3,field_3))







# In[19]:




from flask import Flask,jsonify


# In[ ]:


app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    return jsonify(result)

@app.route("/uscities")
def city():
    return jsonify(result)

@app.route("/uslocation")
def location():
    return jsonify(result_3)

@app.route("/usproperties")
def usproperties():
    return jsonify(result_1)

if __name__=="__main__":
    app.run(debug=True)