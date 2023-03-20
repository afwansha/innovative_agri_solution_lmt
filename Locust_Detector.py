import pandas as pd
import streamlit as st
import pywhatkit
import numpy as np

from joblib import load
st.set_page_config(
    page_title="Locust Detector",
    page_icon=" "
)

def main():
    xgb_model = load('bph_predictor.json')
    html_temp="""
        <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black;text-align:center;">Locust Detection using eXtreme Gradient Boosting</h2>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("##### Enter the atmospheric conditions \n ")

    p1 = st.number_input("temperature in degree celsius",20,40,step=1)
    p2 = st.number_input("moisture in percentage",60,110,step=1)
    p3 = st.number_input("humidity in percentage",60,90,step=1)
    p4 = st.number_input("Nitrogen in Kilogram per hectare",110.00,160.00,step=1.00)
    p5 = st.number_input("Phosphorus in Kilogram per hectare",50.00,100.00,step=1.00)
    p6 = st.number_input("Potassium in Kilogram per hectare",50.00,100.00,step=1.00)

    user_input = pd.DataFrame({
        'temperature':p1,
        'moisture':p2,
        'humidity':p3,
        'nitrogen':p4,
        'phosphorous':p5,
        'potassium':p6,
    },index=[0])

    xgb_model.predict(user_input)

    try:
        if st.button('Predict'):
            pred = xgb_model.predict(user_input)
            #st.balloons()
            st.success("Probability of locust = {:.3f}".format(pred[0]))

    except:
        st.warning("Prediction error")

    if st.button('send whatsapp message'):
        pywhatkit.sendwhatmsg_instantly('+918714267479','नमस्ते आपके खेत में टिड्डियों का प्रकोप है। कृपया आवश्यक उपाय करें और कृषि अधिकारियों को जल्द से जल्द सूचित करें',7,tab_close=True)
    
    
if __name__ == "__main__":
    main()