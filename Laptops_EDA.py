#Importing Required Libraries
import streamlit as slt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

#Setting Page Configuration
slt.set_page_config(page_title = "Laptops - EDA",page_icon="icon.png",layout="wide")
slt.title("@PraneethVasa")
slt.sidebar.title("Project Description")
slt.sidebar.write("The Laptop Finder is a Python-based web app built with Streamlit that helps users discover the best laptops based on their specific requirements and preferences. Whether you're a student, a gamer, or a professional seeking a reliable workhorse, the Laptop Finder simplifies the process of finding the ideal laptop that meets your needs and budget.")
# Creator Information
slt.sidebar.title("About the Creator")
slt.sidebar.write("**Created by**: Praneeth Vasa")
slt.sidebar.write("**Email**     : praneethbalu178@gmail.com")

# Social Media Profiles
slt.sidebar.title("Connect with Me")
slt.sidebar.markdown(
    """
    [LinkedIn](https://www.linkedin.com/in/praneeth-vasa-a42922262/)\n
    [GitHub](https://github.com/PraneethVasa/)\n
    [Instagram](https://www.instagram.com/praneeth_vasa_/)
    """
)
mt = True
mt = False
if mt:
    l = Image.open("mn.png")
    slt.image(l,use_column_width = True)
    slt.title("Sorry, the app (Laptops_EDA) is currently under maintenance. Please try again Later😶‍🌫️")
else:
    #Designing Main Page
        slt.title("LAPTOP FINDER")
        if slt.checkbox("Confused about which laptop to buy? Just feed in your requirements to our Laptop Finder and you will get best recommendations according to your specifications"):
             brand = slt.selectbox("Select Preferred Brand",['Lenovo','HP','DELL','APPLE','RedmiBook','SAMSUNG','MSI','realme Book','ASUS','acer','Infinix'])
             x1 = data[data['name'].str.contains(brand)]
             p = x1.processor.unique()
             processor = slt.selectbox("Select Preferred Processor",p)
             x1 = x1[x1['processor'] == processor]
             r = x1.ram.unique()
             ram = slt.selectbox("Select Preferred RAM",r)
             x1 = x1[x1['ram'] == ram]
             s = x1.storage.unique()
             storage = slt.selectbox("Select Preferred Storage",s)
             x1 = x1[x1['storage'] == storage]
             d = x1.display_size.unique()
             display = slt.selectbox("select Preferred Display Size",d)
             x1 = x1[x1['display_size'] == display]
             price = slt.number_input("Enter Your Budget : ",value=45000,step=5000)
             x1 = x1[x1['price'] <= price]
             x1 = x1.sort_values(by='rating', ascending=False)
             x1 = x1[['name','os','ram','storage','display_size','price','rating']]
             if slt.button("Find Laptops",key='1'):
                if len(x1) == 0:
                    slt.warning(f"The {brand} Laptops having {processor} are bit Much Expensive.  -- TRY TO INCREASE YOUR BUDGET(₹ price) for the Above Requirments")
                else:
                    slt.write("Here are the Best Matches for the Above Specifications")
                    slt.write(x1)
