#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def Function_CI(P,i,n):
  if n == 0:
    return P
  else:
    return (1+(i/100))* Function_CI(P,i,n-1)

