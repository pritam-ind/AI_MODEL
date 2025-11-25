import streamlit as st

st.title("PUBLIC AI INTERFACE")
# st.header("This is my header section")

#add tabs section
st_home, st_select, st_about = st.tabs(["Home", "Select Model", "About"])

#add functions to each section
with st_home:
    st.write("Welcome Friends, This is Our Home Dashboard!")
    
with st_select:
    st.header("Please select")
    
    selection_model = ["Gemini", "ChatGPT", "Grok", "Deepseek"]
    
    user_selection = st.selectbox(
        "Choose your prefered AI Model",
        selection_model)

    if user_selection.lower() == "gemini":
        st.warning("By Default, You are on Gemini")
    elif user_selection.lower() == "chatgpt":
        st.warning("Sorry for the Inconvenience, ChatGPT model is not available now!\nWe well come in touch with you very soon")
    elif user_selection.lower() == "grok":
        st.warning("Sorry for the Inconvenience, Grok model is not available now!\nWe well come in touch with you very soon")
    elif user_selection.lower() == "deepseek":
        st.warning("Sorry for the Inconvenience, Deepseek model is not available now!\nWe well come in touch with you very soon")
    else:
        pass
        