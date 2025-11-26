import streamlit as st

st.title("PUBLIC AI INTERFACE")
# st.header("This is my header section")

#add tabs section
st_home, st_select, st_about = st.tabs(["Home", "Select Model", "About"])

#add functions to each section
with st_home:
    st.write("Welcome Friends, This is Our Own Home Dashboard!")
    
    
with st_select:
    st.header("Please select")
    
    selection_model = ["Gemini", "ChatGPT", "Grok", "Deepseek"]
    
    user_selection = st.selectbox(
        "Choose your prefered AI Model",
        selection_model)

    if user_selection.lower() == "gemini":
        st.success("By Default, You are on Gemini")
    elif user_selection.lower() == "chatgpt":
        st.warning("Sorry for the Inconvenience, ChatGPT model is not available now!\nWe well come in touch with you very soon")
    elif user_selection.lower() == "grok":
        st.warning("Sorry for the Inconvenience, Grok model is not available now!\nWe well come in touch with you very soon")
    elif user_selection.lower() == "deepseek":
        st.warning("Sorry for the Inconvenience, Deepseek model is not available now!\nWe well come in touch with you very soon")
    else:
        pass

with st_about:
        st.header("This is Pritam's About Section!")
        st.write("""Hi, I am a student at Vivekananda Global University (VGU). This application was developed as part of my AI Internship Project. My goal was to create a user-friendly interface that integrates powerful LLMs like Gemini to help students and users interact with AI easily.

Tech Stack: Python, Streamlit, Google Gemini API.""")

        #add button of github and linkedin
        col1, col2, *_ = st.columns(6)    #col1, col2 = st.column(6)...........gives error, why?.....task everytime when i come here
        with col1:
            st.link_button("GitHub", "https://github.com/pritam-ind")
        with col2:
            st.link_button("LinkedIn", "https://github.com/pritam-ind")


        #linux-world section
        st.header("LinuxWorld & the Team")
        st.subheader("Internship Program!")
        st.image("LinuxWorldILinkedIn.png")
        
        st.write("""Created with ❤️ during the LinuxWorld Informatics Internship. This tool showcases the power of Python in building rapid AI prototypes. It demonstrates how modern AI can be made accessible to everyone through simple, effective web interfaces.""")

        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.write("Our Internship")
            st.link_button("LinuxWorld", "https://www.linkedin.com/company/linuxworld-informatics-pvt-ltd")
        st.caption("© VGU Internship Project, All Rights Reserved.")

        with col2:
            st.write("Our Mentor")
            st.link_button("Mr. Vimal Daga", "https://www.linkedin.com/in/vimaldaga")

        with col3:
            st.write("Our Tech Head")
            st.link_button("Mr. Jibbran Ali", "https://www.linkedin.com/in/jibbran-ali")

                
#first i pulled this program from my github
# warning to success at gemini 
# in about section, added my details & links of LinkedIn and Github,  with this i added LinuxWorld information as well