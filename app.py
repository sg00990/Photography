import streamlit as st
from streamlit_gsheets import GSheetsConnection
import requests
from io import BytesIO
import pandas as pd

# connect to google sheets
conn = st.connection("gsheets", type=GSheetsConnection)
app_data = conn.read()
df = pd.DataFrame(app_data)

st.set_page_config(title='Photography Portfolio', page_icon='📷', layout='wide')

def get_image(url):
    response = requests.get(url)
    return BytesIO(response.content)


def photos():
 suki_photos = df[df['Collection'] == 'Suki']

 col1, col2, col3 = st.columns(3)
 
 if not suki_photos.empty:
    col1.header('Suki')
    col2.header('')
    col3.header('')

    images_per_col = [suki_photos.iloc[i::3] for i in range(3)]

    for idx, img_df in enumerate(images_per_col):
        for _, row in img_df.iterrows():
            image_id = row["Image ID"]
            url = f"https://drive.google.com/uc?export=view&id={image_id}"
            img = get_image(url)  
            
            if idx == 0:
                col1.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            elif idx == 1:
                col2.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            else:
                col3.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")

 col4, col5, col6 = st.columns(3)

 nature_photos = df[df['Collection'] == 'Nature']

 if not nature_photos.empty:
    col4.header('Nature & Scenery')
    col5.header('')
    col6.header('')

    images_per_col2 = [nature_photos.iloc[i::3] for i in range(3)]

    for idx, img_df in enumerate(images_per_col2):
        for _, row in img_df.iterrows():
            image_id = row["Image ID"]
            url = f"https://drive.google.com/uc?export=view&id={image_id}"
            img = get_image(url) 
            
            if idx == 0:
                col4.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            elif idx == 1:
                col5.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            else:
                col6.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")

 col7, col8, col9 = st.columns(3)

 event_photos = df[df['Collection'] == 'Event']

 if not event_photos.empty:
    col7.header('Events')
    col8.header('')
    col9.header('')

    images_per_col3 = [event_photos.iloc[i::3] for i in range(3)]

    for idx, img_df in enumerate(images_per_col3):
        for _, row in img_df.iterrows():
            image_id = row["Image ID"]
            url = f"https://drive.google.com/uc?export=view&id={image_id}"
            img = get_image(url)
            
            if idx == 0:
                col7.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            elif idx == 1:
                col8.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")
            else:
                col9.image(img, use_container_width=True, caption=f"{row['Description']} ({row['Year']}) | {row['Lens']} | {row['Aperture']} | {row['Shutter Speed']} | {row['ISO']}")


def main():

    tab1, tab2, tab3 = st.tabs(["Home", "Photos", "Feedback"])


    with tab2:
        photos()

    with tab3:
        pass
    
    with tab1:
        col2, col2, col3 = st.columns([.25, 2, 1.5])

        with col2:
            st.title("Hi, I'm Sarah")
            st.subheader('*Data Engineer & Amateur Photographer*')  
            st.write(
                    "I'm an **amateur photographer** who started my photography journey in **June 2024** "
                    "with a **Canon EOS 50**. I love capturing the beauty of **nature, people, scenery, and my cat, Suki 🐱**. "
                    "I also have a lot of fun taking photos of my family, but I’ve chosen not to include them here for privacy reasons. This gallery showcases some of my favorite shots. "
                    "I hope you enjoy!\n\n"
                    "If you have any thoughts or suggestions, "
                    "I'd love to hear from you in the **Feedback** tab! I am still learning after all."
                )

            st.write('#')

            col4, col5, col6 = st.columns(3)
            col4.link_button('LinkedIn', "https://www.linkedin.com/in/sarah-graddy/", use_container_width=True)
            col5.link_button('GitHub', "https://github.com/sg00990", use_container_width=True)

        col3.image('img/bkg1.png', use_container_width=True)

if __name__ == "__main__":
    main()
