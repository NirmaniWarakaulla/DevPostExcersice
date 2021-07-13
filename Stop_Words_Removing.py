#!/usr/bin/env python
# coding: utf-8

# # Stop_Words_Removing Excercise
# 
# ## By Nirmani Warakaulla

# ### Using NLTK Library

# #### import all the modules and libraries you want

# In[11]:


from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize


# #### input your sentence or paragraph

# In[13]:


example_sent = "This is a sample sentence created by Nirmani Warakaulla, showing off the stop words filtration."
print(example_sent)


# #### stop words removing

# In[14]:


stop_words = set(stopwords.words('english'))
word_tokens = word_tokenize(example_sent)
filtered_sentence = [w for w in word_tokens if not w in stop_words]
filtered_sentence = []
for w in word_tokens:
    if w not in stop_words:
        filtered_sentence.append(w)


# #### print the tokenized words.Because we have to tokenize the sentences before applying the stop words remove.

# In[15]:


print(word_tokens)


# #### print the filtered sentence after removing the stop words.

# In[16]:


print(filtered_sentence)


# #### print the orginal stop words corpus 

# In[17]:


print(stop_words)


# #### Add new stopword into corpus as you wish.

# In[19]:


stop_words.add("Nirmani")


# #### print the stop words corpus after adding new stop word.

# In[20]:


print(stop_words)


# #### Remove unnecessary stopword from the corpus as you wish.

# In[21]:


stop_words.remove("Nirmani")


# #### print the stop words corpus after removing unnecessary stop word.

# In[22]:


print(stop_words)


# In[ ]:




