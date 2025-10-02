# Import pickle and streamlit
import pickle
import streamlit as st

# read pickle file
model1 = pickle.load(open("model3.pkl", "rb"))

# deploy model
def model_deploy():
    # title
    st.title("Insurance Prediction")
    # Take input from user
    age = st.number_input("Enter your age :")
    # predict button
    predict = st.button("Predict")

    if predict:
        # predict the result and print output
        
        if model1.predict([[age]])[0] == 0:
            st.write("Person will not buy the insurance")
        else:
            st.write("Person will buy the insurance")

# call function
model_deploy()