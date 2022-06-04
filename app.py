#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from textblob import TextBlob


# In[ ]:


#pip install Flask 


# In[ ]:


from flask import Flask


# In[ ]:


from flask import render_template, request


# In[ ]:


app = Flask (__name__) 


# In[ ]:


@app.route("/", methods =["GET","POST"]) # the @ sign means put the function of this object route, embed inside a function
def index():
    if request.method =="POST":
        text = request.form.get("text")
        print(text)
        r = Textblob(text).sentiment
        return(render_template("index.html", result="r"))
    else:
        return(render_template("index.html", result ="waiting...."))


# In[ ]:


if __name__=="__main__":
    app.run()


# In[ ]:




