import os
import streamlit as st
from PIL import Image
import PIL


mywidth = 3000

def resize_pic(uploaded_image, downloaded_image) :
    img=Image.open (uploaded_image)
    wpercent = (mywidth/float(img.size[0]))
    hsize=int((float(img.size[1])*float(wpercent)))
    img=img.resize( (mywidth, hsize), PIL.Image.ANTIALIAS)
    img.save (downloaded_image)



@st.cache(persist=True,allow_output_mutation=True,show_spinner=False,suppress_st_warning=True)
def download_success():
    st.balloons()
    st.success('✅ Download Successful !!')

st.set_page_config(
    page_title="IMAGE TO SKETCH WEBAPP",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="auto",
)
main_image = Image.open('main_banner.png')


upload_path = "uploads/"
download_path = "downloads/"

st.image(main_image,use_column_width='auto')
st.title("✨ IMAGE TO SKETCH WEBAPP 🖼 ")
st.info('✨ Supports all popular image formats 📷 - PNG, JPG, BMP 😉')

uploaded_file = st.file_uploader("Upload Image 🖼", type=["png","jpg","bmp","jpeg"])

if uploaded_file is not None:
    with open(os.path.join(upload_path,uploaded_file.name),"wb") as f:
        f.write((uploaded_file).getbuffer())

    with st.spinner(f"Sketching... 💫"):
        uploaded_image = os.path.abspath(os.path.join(upload_path,uploaded_file.name))
        downloaded_image = os.path.abspath(os.path.join(download_path,str("enhanced_"+uploaded_file.name)))
        resize_pic(uploaded_image, downloaded_image)

        final_image = Image.open(downloaded_image)
        print("Opening ",final_image)
        st.markdown("---")
        st.image(final_image, caption='This is how your sketch image looks like 😉')
        with open(downloaded_image, "rb") as file:
            if uploaded_file.name.endswith('.jpg') or uploaded_file.name.endswith('.JPG'):
                if st.download_button(
                                        label="Download Sketch Image 📷",
                                        data=file,
                                        file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                        mime='image/jpg'
                                     ):
                    download_success()

            if uploaded_file.name.endswith('.jpeg') or uploaded_file.name.endswith('.JPEG'):
                if st.download_button(
                                        label="Download Sketch Image 📷",
                                        data=file,
                                        file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                        mime='image/jpeg'
                                     ):
                    download_success()

            if uploaded_file.name.endswith('.png') or uploaded_file.name.endswith('.PNG'):
                if st.download_button(
                                        label="Download Sketch Image 📷",
                                        data=file,
                                        file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                        mime='image/png'
                                     ):
                    download_success()

            if uploaded_file.name.endswith('.bmp') or uploaded_file.name.endswith('.BMP'):
                if st.download_button(
                                        label="Download Sketch Image 📷",
                                        data=file,
                                        file_name=str("Sketch_AFFI_"+uploaded_file.name),
                                        mime='image/bmp'
                                     ):
                    download_success()
else:
    st.warning('⚠ Please upload your Image file 😯')


#Add 'before' and 'after' columns
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    col1, col2 = st.columns( [0.5, 0.5])
    with col1:
        st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
        st.image(image,width=300)  

    with col2:
        st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)
        st.image(final_image,width=300)


st.markdown("<br><hr><center>Made with ❤️ by <a href='a03003132335@gmail.com?subject=IMAGE to SKETCH WebApp!&body=Please specify the issue you are facing with the app.'><strong>AFTAB HUSSAIN SHAR</strong></a></center><hr>", unsafe_allow_html=True)