import streamlit as st
import numpy as np
import pickle
import pandas as pd
import base64
import math

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Laptop Valuation System",
    layout="wide"
)

# ---------------- BACKGROUND ----------------
def set_bg(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()
    st.markdown(
    f"""
    <style>
    /* APP BACKGROUND */
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* MAIN CARD */
    .card {{
        background: rgba(15,15,25,0.9);
        padding: 25px;
        border-radius: 18px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.7);
        color: white;
    }}

    h1, h2, h3, label {{
        color: white !important;
    }}

    /* 🔥 SELECTBOX CURSOR FIX 🔥 */
    section[data-testid="stSidebar"] div[data-baseweb="select"],
    section[data-testid="stSidebar"] div[data-baseweb="select"] * {{
        cursor: pointer !important;
    }}

    /* SLIDER CURSOR */
    section[data-testid="stSidebar"] input[type="range"] {{
        cursor: pointer !important;
    }}

    /* TEXT INPUT CURSOR */
    section[data-testid="stSidebar"] input[type="text"],
    section[data-testid="stSidebar"] input[type="number"] {{
        caret-color: white !important;
        cursor: text !important;
        color: white !important;
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# comment this line if you don't want background
set_bg("laptop2.jpg")

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("laptop_price_model.pkl", "rb"))

# ---------------- SIDEBAR ----------------
st.sidebar.title("⚙️ Configuration")

company = st.sidebar.selectbox(
    "Company",
    ["Apple","HP","Dell","Lenovo","Asus","Acer","MSI","Toshiba","Samsung"]
)

typename = st.sidebar.selectbox(
    "Type",
    ["Notebook","Ultrabook","Gaming","2 in 1 Convertible","Workstation"]
)
if company == "Apple":
    ram = st.sidebar.selectbox("RAM (GB)", [8,16,32,64])
else:
    ram = st.sidebar.selectbox("RAM (GB)", [4,8,16,32,64])
 
if typename == "Ultrabook":
    weight = st.sidebar.selectbox("Weight (kg)", [1.2,1.3,1.5])
elif typename == "Gaming":
    weight = st.sidebar.selectbox("Weight (kg)", [2.3, 2.5,2.8])                              
else:
    weight = st.sidebar.selectbox("Weight (kg)", [1.5,1.8,2.0,2.3])
                                 

touchscreen = st.sidebar.selectbox("Touchscreen", ["No", "Yes"])
ips = st.sidebar.selectbox("IPS Display", ["No", "Yes"])

cpu_brand = st.sidebar.selectbox(
    "CPU Brand",
    ["Intel Core i3","Intel Core i5","Intel Core i7",
     "AMD Ryzen 3","AMD Ryzen 5","AMD Ryzen 7"]
)

gpu_brand = st.sidebar.selectbox("GPU Brand", ["Intel","Nvidia","AMD"])

os = st.sidebar.selectbox("Operating System", ["Windows","Linux","Mac"])

hdd = st.sidebar.selectbox("HDD (GB)", [0, 500, 1000, 2000])
ssd = st.sidebar.selectbox("SSD (GB)", [0, 128, 256, 512, 1024])

screen_size = st.sidebar.selectbox("Screen Size (inches)", [13.3,14,15.6,16,17.3])
resolution = st.sidebar.selectbox(
    "Screen Resolution",
    ["1920x1080","1366x768","2560x1440","3840x2160"]
)

# ---------------- FEATURE ENGINEERING ----------------
touchscreen = 1 if touchscreen == "Yes" else 0
ips = 1 if ips == "Yes" else 0

X_res, Y_res = map(int, resolution.split('x'))
ppi = math.sqrt(X_res**2 + Y_res**2) / screen_size

# ---------------- INPUT DATAFRAME (EXACT MATCH) ----------------
input_df = pd.DataFrame({
    "Company": [company],
    "TypeName": [typename],
    "Ram": [ram],
    "Weight": [weight],
    "Touchscreen": [touchscreen],
    "Ips": [ips],
    "ppi": [ppi],
    "Cpu brand": [cpu_brand],
    "HDD": [hdd],
    "SSD": [ssd],
    "Gpu brand": [gpu_brand],
    "os": [os]
})

# ---------------- MAIN UI ----------------
st.markdown("<h1>💻Laptop Valuation System</h1>", unsafe_allow_html=True)




c1, c2, c3, c4 = st.columns(4)
c1.metric("Company", company)
c2.metric("CPU", cpu_brand)
c3.metric("RAM", f"{ram} GB")
c4.metric("Type", typename)

st.divider()

c5, c6, c7 = st.columns(3)
c5.metric("Storage", f"SSD: {ssd} GB")
c6.metric("GPU", gpu_brand)
c7.metric("OS", os)

st.write("### Ready to Calculate")


if st.button("💰 Calculate Laptop Price"):
    log_price = model.predict(input_df)[0]
    real_price = np.expm1(log_price)

    st.markdown(
        f"""
        <div style="
            margin-top: 20px;
            font-size: 22px;
            color: #b0b0b0;
        ">
            <span style="font-weight: 500;">
                Estimated Laptop Price :
            </span>
            <span style="
                font-size: 32px;
                color: white;
                font-weight: bold;
                margin-left: 10px;
            ">
                ₹ {int(real_price):,}
            </span>
        </div>
        """,
        unsafe_allow_html=True
    )
