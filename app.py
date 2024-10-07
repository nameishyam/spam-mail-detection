
import streamlit as st
import pickle
import numpy as np
 # Load the model
with open('C:\\Users\\gedda\\OneDrive\\Desktop\\ML PROJECT\\MailPrediction.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
# Streamlit app
st.title("Mail Prediction App")
st.write("""Enter the features to get the prediction""")

# Input fields
input_data = []
for i in range(1, 6):  # Assuming there are 5 features
    input_data.append(st.number_input(f'Feature {i}', value=0.0))
    if st.button('Predict'):
        final_features = [np.array(input_data)]
        prediction = model.predict(final_features)
        output = prediction[0]
        st.success(f'Prediction: {output}')