import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="File Dashboard", layout="wide")

# Load metadata from CSV
df = pd.read_csv("metadata.csv")

st.title("📁 Screenshot File Dashboard")

# Sidebar filters
category = st.sidebar.selectbox("Filter by Category", ["All"] + sorted(df['category'].unique()))
file_type = st.sidebar.selectbox("Filter by Type", ["All"] + sorted(df['type'].unique()))

# Apply filters
filtered_df = df.copy()
if category != "All":
    filtered_df = filtered_df[filtered_df['category'] == category]
if file_type != "All":
    filtered_df = filtered_df[filtered_df['type'] == file_type]

# Show files
st.subheader("Files")
for _, row in filtered_df.iterrows():
    file_path = os.path.join("screenshots", row["filename"])
    st.markdown(f"**{row['filename']}**")
    st.image(file_path, caption=f"{row['type']} | {row['date']} | Tags: {row['tags']}", width=600)
    st.download_button("Download", open(file_path, "rb"), file_name=row['filename'])
    st.markdown("---")
