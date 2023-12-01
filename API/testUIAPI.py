""" Basic web page API UI for RunMLC testing
Development CLI "streamlit run ./API/testUIAPI.py"
# TODO Consider item 2) 'Condition Wind' against item 3) 'Wind mph' option
"""

import streamlit as st
import numpy as np
from datetime import datetime
import os

header = st.container()
results = st.container()

# model_file = "/home/stuart/Documents/RunMLC/Data_int.npy"
model_file = "./model/Data.npy"  # Streamlit to Github path
Data = np.load(model_file)

with header:
    st.title("RUNNING CLOTHES SELECTOR")
    st.text(f"RunMLC - {datetime.now().strftime('%d/%m/%y %H:%M')}")
    st.markdown(
        "Obj. Predict the appropriate outdoor running clothing.\\\nModel: "
        + str(
            datetime.fromtimestamp(os.path.getmtime(model_file)).strftime(
                "%d/%m/%y %H:%M"
            )
        )
    )

st.sidebar.markdown(
    """
    **Rev:** 1.1 \n
    **Model:**
    Array 18 x 41 x 3 x 13 x 2 = 57,564
    """
)

with st.sidebar:
    st.header("Inputs")

    usr_Temperature = st.slider(
        "1\) Temperature (C)", min_value=-10, max_value=30, value=10, step=1
    )

    usr_Conditions = st.radio("2\) Condition", ["Wind", "Rain/Fog/Snow", "Sun"])
    if usr_Conditions == "Wind":
        Cond = 0
    elif usr_Conditions == "Rain/Fog/Snow":
        Cond = 1
    else:
        Cond = 2

    usr_Windy = st.slider("3\) Wind (mph)", min_value=0, max_value=10, value=8, step=1)
    if usr_Windy < 1:
        WindBF = 0
    elif 1 <= usr_Windy <=3:
        WindBF = 1
    elif 4<= usr_Windy <=7 :
        WindBF = 2
    elif 8<= usr_Windy <=12 :
        WindBF = 3
    else:
        WindBF = 12  # error
    # st.write("DEBUG> WindBF=", WindBF, "Feels=", round(usr_Temperature-(usr_Windy*0.7)))  # debug
    # st.write("Beaufort Scale:\\\n0=Calm\\\n1=Light Air (1 to 3mph)\\\n2=Light Breeze (4 to 7mph)\\\n3=Gentle Breeze (8 to 12mph)\\\n4=Moderate Breeze (13 to 18mph)...")

    usr_DayTime = st.radio("4\) Day light", ["Yes", "No"])
    if usr_DayTime == "Yes":
        DayNight = 1
    else:
        DayNight = 0
    # st.write("DEBUG> DayNight=", DayNight)  # debug

count = 0

Clothing = [
    "Peaked Hat",
    "Light Hat",
    "Thick Hat",
    "Thin Gloves",
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
    "Sun Glasses",
    "Florescent",
    "Light",
    "Water",
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
    0: "Wind",
    1: "Rain/Fog/Snow",
    2: "Sun",
}

WindBF_index = {
    0: "Calm",
    1: "Light Air (1 to 3mph)",
    2: "Light Breeze (4 to 7mph)",
    3: "Gentle Breeze (8 to 12mph)",
    4: "Moderate Breeze (13 to 18mph)",
    5: "Fresh Breeze (19 to 24mph)",
    6: "Strong Breeze (25 to 31mph)",
    7: "Near Gale (32 to 38mph)",
    8: "Gale (39 to 46mph)",
    9: "Strong Gale (47 to 54mph)",
    10: "Whole Gale (55 to 63mph)",
    11: "Storm Force (64 to 75mph)",
    12: "Hurricane Force (over 75mph)",
}  # BF# to description

Day = {
    0: "Night time",
    1: "Day time",
}

# --------------
with results:
    st.write(
        f"{Day[DayNight].upper()} in {usr_Temperature}C DEGREES, {Conditions[Cond].upper()}, {WindBF_index[WindBF].upper()} conditions, requires:"
    )
    for i in range(24):
        if Data[i, Temperature[usr_Temperature], Cond, WindBF, DayNight] == 1.0:
            count += 1
            st.write(f"{count}. {Clothing[i].upper()}")
        elif Data[i, Temperature[usr_Temperature], Cond, WindBF, DayNight] > 0:
            count += 1
            st.write(f"{count}. {Clothing[i].lower()} - _option or replacement item_")            

st.markdown(
    """_Notes:_
* _Windchill; ID, Watch, Water/Food, Tracker, Glasses... Shoes._ :smile:
* _This information does not constitute legal advice. Lookout the window!_
"""
)
