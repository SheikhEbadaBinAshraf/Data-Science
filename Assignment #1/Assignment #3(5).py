#!/usr/bin/env python
# coding: utf-8

# In[17]:


"""# Q5
#Write a Python program which accepts the user's first and last name and print them in
#reverse order with a space between them."""

first_name = input("Enter First Name: ");
last_name = input("\nEnter Last Name: ");
last_name_reversed = last_name[::-1];
first_name_reversed = first_name[::-1];
print("\nName is in Simple Order: ",first_name +" "+ last_name);
print("Name is in Reverse Order: ",last_name_reversed +" "+  first_name_reversed);


# In[ ]:




