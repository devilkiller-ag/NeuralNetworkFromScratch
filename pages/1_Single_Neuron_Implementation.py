import os
import sys
import pandas as pd
import streamlit as st

# Get the parent folder path
parent_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Add the parent folder to sys.path
if parent_folder not in sys.path:
    sys.path.append(parent_folder)

from scripts.display_pdf import displayPDF

st.title("Single Neuron Implementation")

sample_inputs = [1, 2, 3]
sample_weights = [0.2, 0.8, -0.5]
sample_bias = 2

st.write("Enter Neuron Bias: ")
bias = st.number_input(
    "Neuron Bias", value=sample_bias, key="bias", label_visibility="collapsed"
)

st.write("Enter Inputs and respective weights for the Neuron: ")
input_df = pd.DataFrame({"Inputs": sample_inputs, "Weights": sample_weights})
input_edited_df = st.data_editor(
    input_df,
    use_container_width=True,
    num_rows="dynamic",
    hide_index=True,
)

inputs = input_edited_df["Inputs"].tolist()
weights = input_edited_df["Weights"].tolist()

output = 0
calculation_string = ""
for i in range(len(inputs)):
    inputs[i] = float(inputs[i])
    weights[i] = float(weights[i])
    output += inputs[i] * weights[i]
    calculation_string += f"({inputs[i]} * {weights[i]}) + "
output += bias
calculation_string += f"{bias}"

st.write("Neuron Value: ", calculation_string, " = ", output)


st.subheader("Theory")
st.image("resources/single_neuron.png")

st.subheader("Example Implementation Using Python")
code = """
inputs = [1, 2, 3]
weights = [0.2, 0.8, -0.5]
bias = 2

output = 0
for i in range(len(inputs)):
    output += inputs[i] * weights[i]
output += bias

print(outputs)
"""
st.code(code)

st.subheader("Example Implementation Using NumPy")
code = """
import numpy as np

inputs = np.array([1, 2, 3])
weights = np.array([0.2, 0.8, -0.5])
bias = 2

output = np.dot(inputs, weights) + bias

print(output)
"""
st.code(code)

st.subheader("References")
st.write("**[Neural Networks from Scratch: Chapter 2](https://nnfs.io/)**")
st.write(
    "**[YouTube: Vizuara: Neural Network from Scratch: Coding Neurons and Layers](https://youtu.be/zrKpz9-AZ_E?si=CL2Y_qyIKeWPiRxU)**"
)
