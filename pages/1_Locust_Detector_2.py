import pandas as pd
import streamlit as st
from joblib import load
import pywhatkit
st.set_page_config(
    page_title="Locust Detector",
    page_icon=" "
)

def main():
    xgb_model = load('bph_prediction2.json')
    html_temp="""
        <div style="background-color:lightblue;padding:16px">
            <h2 style="color:black;text-align:center;">Locust Detection using eXtreme Gradient Boosting</h2>
        </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("##### Enter the values by PIR and TCS3200 sensor. \n ")

    p1 = st.selectbox("Select IR Value",(7,8,9,10,11,12,13,14))
    p2 = st.selectbox("Select color in hexadecimal",('#00FF00','#FFFF00','#FFAE42','#964B00','#9ACD32','#023020'))
    if p2=="#FFFF00":
        p2=0
    elif p2=="#00FF00":
        p2=1
    elif p2=='#FFAE42':
        p2=2
    elif p2=='#964B00':
        p2=3
    elif p2=='#9ACD32':
        p2=4
    elif p2=='#023020':
        p2=5

    user_input = pd.DataFrame({
        'wavelength':p1,
        'color':p2,
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