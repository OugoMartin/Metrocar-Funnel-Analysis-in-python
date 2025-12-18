#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib as plt


# # Load and Inspect the Data

# In[2]:


df = pd.read_csv("metrocar_funnel_analysis_query.csv")
df.head()


# In[3]:


df.info()


# In[5]:


df.isna().sum()


# # Define Funnel Stages 

# In[8]:


funnel_stages = [
    "app_opened",
    "ride_requested",
    "driver_assigned",
    "ride_completed"
]
for stage in funnel_stages:
    print(stage)


# # Calculate Funnel Counts

# In[9]:


funnel_counts = df.notnull().sum()

funnel_counts_df = pd.DataFrame({
    "Stage": funnel_counts.index,
    "Users": funnel_counts.values
})

funnel_counts_df


# # Calculate Conversion Rates Between Stages

# In[10]:


funnel_counts_df["Conversion_Rate"] = (
    funnel_counts_df["Users"] /
    funnel_counts_df["Users"].shift(1)
)

funnel_counts_df.loc[0, "Conversion_Rate"] = 1.0

funnel_counts_df


# # Calculate Drop-Off Rates

# In[11]:


funnel_counts_df["Drop_Off_Rate"] = 1 - funnel_counts_df["Conversion_Rate"]

funnel_counts_df


# # Overall Funnel Completion Rate

# In[12]:


overall_conversion = (
    funnel_counts_df.iloc[-1]["Users"] /
    funnel_counts_df.iloc[0]["Users"]
)

overall_conversion


# # Funnel Visualization (Bar Chart)

# In[19]:


plt.figure()
plt.bar(
    funnel_counts_df["Stage"],
    funnel_counts_df["Users"]
)

plt.title("Metrocar User Funnel")
plt.xlabel("Funnel Stage")
plt.ylabel("Number of Users")
plt.show()


# # Conversion Rate Visualization

# In[14]:


plt.figure()
plt.plot(
    funnel_counts_df["Stage"],
    funnel_counts_df["Conversion_Rate"],
    marker="o"
)

plt.title("Stage-to-Stage Conversion Rates")
plt.xlabel("Funnel Stage")
plt.ylabel("Conversion Rate")
plt.ylim(0, 1)
plt.show()


# # Key Business Insights (Template Logic)

# In[15]:


largest_drop = funnel_counts_df.loc[
    funnel_counts_df["Drop_Off_Rate"].idxmax()
]

largest_drop


# # Export Results for Reporting

# In[16]:


funnel_counts_df.to_csv("metrocar_funnel_metrics_summary.csv", index=False)


# # Funnel Chart (Horizontal Funnel)

# In[17]:


import matplotlib.pyplot as plt

# Ensure correct order (top of funnel first)
funnel_counts_df = funnel_counts_df.sort_values(
    by="Users", ascending=False
)

plt.figure()

plt.barh(
    funnel_counts_df["Stage"],
    funnel_counts_df["Users"]
)

plt.gca().invert_yaxis()  # Top stage at the top

plt.title("Metrocar User Funnel")
plt.xlabel("Number of Users")
plt.ylabel("Funnel Stage")

plt.show()


# # Funnel Chart with Percentage Labels (Optional but Recommended)

# In[18]:


total_users = funnel_counts_df["Users"].iloc[0]

plt.figure()

plt.barh(
    funnel_counts_df["Stage"],
    funnel_counts_df["Users"]
)

plt.gca().invert_yaxis()

for index, value in enumerate(funnel_counts_df["Users"]):
    percentage = value / total_users
    plt.text(
        value,
        index,
        f" {percentage:.1%}",
        va="center"
    )

plt.title("Metrocar User Funnel with Conversion Percentages")
plt.xlabel("Number of Users")
plt.ylabel("Funnel Stage")

plt.show()

