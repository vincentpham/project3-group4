
from part_1.py import result





from flask import Flask,jsonify


# In[ ]:


app=Flask(__name__)

@app.route("/")
def home():
    return jsonify(result)


if __name__=="__main__":
    app.run('localhost', 5000)



# In[ ]: