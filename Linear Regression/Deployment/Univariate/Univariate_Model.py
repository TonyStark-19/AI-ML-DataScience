# Import pickle and streamlit
import pickle
import streamlit as st

# read pickle file
model1 = pickle.load(open("model1.pkl", "rb"))

# deploy model
def model_deploy():
    # title
    st.title("Area Price Prediction")
    # Take input from user
    area = st.number_input("Enter your area value :")
    # predict button
    predict = st.button("Predict")

    if predict:
        # predict the result and print output
        
        if area <= 0:
            st.write("Price of area", area, "sq feet is : 0")
        else:
            x = model1.predict([[area]])
            st.write("Price of area", area, "sq feet is :", x[0].round(), "rupees")

# call function
model_deploy()