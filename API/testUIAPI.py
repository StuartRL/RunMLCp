""" Basic web page API UI for RunMLC testing
CLI "streamlit run ./API/testUIAPI.py"
ToDo:
1) 
2) 
3) 
"""

import streamlit as st
import numpy as np
from datetime import datetime
import sys
import os

header = st.container()
results = st.container()

model_file = "./model/Data.npy"
Data = np.load(model_file)

with header:
    st.title("RUNNING CLOTHES SELECTOR")
    st.text(f"RunMLC - {datetime.now().strftime('%d/%m/%y %H:%M')}")
    st.markdown(
        "Obj. Predict the appropriate outdoor running clothing.\\\nModel: " +
        str(datetime.fromtimestamp(os.path.getmtime(model_file)).strftime("%d/%m/%y %H:%M"))
    )

st.sidebar.markdown(
    """
    **Rev:** 1.0 \n
    **Model:**
    Array 18 x 41 x 3 x 13 x 6 = 172,692
    """
)

with st.sidebar:
    st.header("Inputs")
    usr_Temperature = st.slider(
        "1\) Temperature", min_value=-10, max_value=30, value=10, step=1
    )
    usr_Conditions = st.radio(
        "2\) Condition",
        ["Wind/Cold", "Rain/Snow", "Sun/Hot"]
    )
    match usr_Conditions:
        case "Wind/Cold":
            Cond = 0
        case "Rain/Snow":
            Cond = 1
        case "Sun/Hot":
            Cond = 2

count = 0
Clothing = [
    "Light Hat",
    "Thick Hat",
    "Light Gloves",
    "Gloves",
    "Running Vest",
    "Tshirt",
    "Long Sleeve",
    "Helly Long Sleeve",
    "Track Top",
    "Windstop Top",
    "Kag",
    "Shorts",
    "Light Leggings",
    "Leggings",
    "Helly Leggings",
    "Short Socks",
    "Long Socks",
    "Sun Cream",
]
Temperature = {
    -10: 0,
    -9: 1,
    -8: 2,
    -7: 3,
    -6: 4,
    -5: 5,
    -4: 6,
    -3: 7,
    -2: 8,
    -1: 9,
    0: 10,
    1: 11,
    2: 12,
    3: 13,
    4: 14,
    5: 15,
    6: 16,
    7: 17,
    8: 18,
    9: 19,
    10: 20,
    11: 21,
    12: 22,
    13: 23,
    14: 24,
    15: 25,
    16: 26,
    17: 27,
    18: 28,
    19: 29,
    20: 30,
    21: 31,
    22: 32,
    23: 33,
    24: 34,
    25: 35,
    26: 36,
    27: 37,
    28: 38,
    29: 39,
    30: 40,
}
Conditions = {
    0: "Wind/Cold",
    1: "Rain/Snow",
    2: "Sun/Hot",
}

with results:
    st.write(f"For {usr_Temperature} DEGREES in {Conditions[Cond].upper()} conditions:")
    for i in range(18):
        if Data[i, Temperature[usr_Temperature], Cond, 0, 0]:
            count += 1
            st.text(f"{count}) {Clothing[i]}")

st.markdown(
    """Notes
* windchill, watch, water, tracker, glasses... shoes! :smile:
"""
)
