import streamlit as st
from preprocessingfile import preprocessing_text,sentiment
import time

st.set_page_config(layout="wide")
st.title("Movie Sentiment Analysis :smile::disappointed: ")

text = st.text_area(
    label="Enter a movie review :lower_left_fountain_pen: ",
    height=150,
    placeholder="write/paste review here"
    )

btn=st.button("Analysis the review :mag:")
start_time=time.time()


if btn and text!="":
    cleaned_text=preprocessing_text(text)
    senti=sentiment(cleaned_text)
    senti=senti.title()


    if senti=="Positive":
        col1, col2, col3 = st.columns(3)
        with col1:
            pass
        with col2:
            st.subheader("The sentiment is {}.".format(senti.lower()))
            end_time = round(time.time() - start_time)
            if end_time > 1:
                st.text("Time taken : {} secs".format(end_time))
        with col3:
            pass

        col1, col2, col3 = st.columns(3)
        with col1:
            pass
        with col2:
            st.image("thumb.png", width=300)

        with col3:
            pass

    else:
        col1, col2,col3 = st.columns(3)
        with col1:
            pass
        with col2:
            st.subheader("The sentiment is {}.".format(senti.lower()))
            end_time = round(time.time() - start_time)
            if end_time > 1:
                st.text("Time taken : {} secs".format(end_time))
        with col3:
            pass
        col1,col2,col3=st.columns(3)
        with col1:
            pass
        with col2:
            st.image("sad.png", width=300)
        with col3:
            pass

elif btn and text=="":
    st.error("Enter the review please!")


