# Import pickle and streamlit
import pickle
import streamlit as st

# read pickle file
model1 = pickle.load(open("model2.pkl", "rb"))

# deploy model
def model_deploy():
    # title
    st.title("Area Price Prediction")
    
    # Take input from user
    area = st.number_input("Enter the value of area :")
    berdroom = st.number_input("Enter the number of bedrooms :")
    age = st.number_input("Enter the value of age :")

    # predict button
    predict = st.button("Predict")
    
    if predict:
        # predict the result and print output
        
        x = model1.predict([[area,berdroom,age]])
        st.write("Price of area", area, "sq feet is :", x[0].round(), "rupees")

# call function
model_deploy()