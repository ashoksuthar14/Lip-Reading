import streamlit as st
import tempfile

# Title of the app
st.title("Lip Reading Device")

# File uploader for selecting a video
video_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if video_file is not None:
    # Save the uploaded file temporarily
    temp_file = tempfile.NamedTemporaryFile(delete=False)
    temp_file.write(video_file.read())

    # Display the video in the Streamlit app
    st.video(temp_file.name)

# Button to submit the video
if st.button("Submit"):
    if video_file is not None:
        # Show a text box with the message
        st.text_area("Predicted value:", "read my lips")
    else:
        st.warning("Please upload a video file before clicking submit.")
