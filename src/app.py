import streamlit as st
from constants import *
from stqdm import stqdm
from prompts import *
from generator import *
from utils import *


st.set_page_config(
    layout="wide",
    page_title="AI Book Generator",
    page_icon=":book:",
)
st.title("AI Book Generator")
st.markdown("<h3>Select options </h3>", unsafe_allow_html=True)
with st.expander("Educational value *"):
    age_range = st.select_slider("Age range of the reader", options=AGE_RANGE)
    skill_development = st.selectbox("Skill development", options=SKILL_DEVELOPMENT)
    learning_obectives = st.selectbox(
        "Learning objectives", options=LEARNING_OBJECTIVES
    )
with st.expander("Emotional value *"):
    theme = st.selectbox("Theme", options=THEME)
    mood = st.selectbox("Moood of story", options=MODD_OF_STORY)
    positive_messaging = st.selectbox("Skill development", options=POSITIVE_MESSAGNG)
with st.expander("Personal *"):
    theme = st.selectbox("Gender", options=GENDER)
    fvrt_book = st.text_input("Favorite book")
with st.expander("Book Details * "):
    chapters = st.number_input(
        "How many chapters should the book have?", min_value=3, max_value=100, value=5
    )

    title = st.text_input("Title of the book")
    genre = st.selectbox("Genre", options=GENRE)
    topic = st.selectbox("Topic ", options=TOPIC)
    main_name = st.text_input("Name of main character")
    type_of_main_character = st.selectbox(
        "Type of main character", TYPE_OF_MAIN_CHARACTER
    )
    antagonist_name = st.text_input("Antagonist name")
    antagonsit_type = st.selectbox("Antagonist type", options=ANTAGONIST_TYPE)
    suuporting_character_name = st.text_input("Supporting character name (if any)")
    suporting_character_type = st.selectbox(
        "Supporting character type", options=SUPPORTING_CHARACTER_TYPE
    )
    settings = st.selectbox("Setting ", options=SETTINGS)
    resolution = st.selectbox("Resolution", options=RESOLUTION)

btn = st.button("Generate Book")
if btn:
    content = []
    for x in stqdm(range(chapters), desc="Generating book"):
        if x == 0:
            prmpt = get_initial_prompts(
                genre,
                type_of_main_character,
                main_name,
                skill_development,
                learning_obectives,
                theme,
                topic,
            )
            content.append(complete_with_gpt(prmpt, 200, "meta-llama/Llama-3.2-3B", 1500, 0.7, 1.5))
        if x == 1:
            prmpt = story_setting_prompt(
                genre,
                type_of_main_character,
                main_name,
                skill_development,
                learning_obectives,
                theme,
                mood,
                antagonist_name,
                antagonsit_type,
            )
            previous = " ".join(x for x in content)
            prmpt = previous + " " + prmpt
            content.append(complete_with_gpt(prmpt, 200, "meta-llama/Llama-3.2-3B", 1500, 0.7, 1.5))

        if x % 3 == 0:
            prmpt = supporting_character_inclusion(
                genre,
                suuporting_character_name,
                suporting_character_type,
                positive_messaging,
            )
            previous = " ".join(x for x in content)
            prmpt = previous + " " + prmpt
            content.append(complete_with_gpt(prmpt, 200, "meta-llama/Llama-3.2-3B", 1500, 0.7, 1.5))
        if x == chapters - 1:
            prmpt = ending_scene(genre, resolution, main_name, positive_messaging)
            previous = " ".join(x for x in content)
            prmpt = previous + " " + prmpt
            content.append(complete_with_gpt(prmpt, 200, "meta-llama/Llama-3.2-3B", 1500, 0.7, 1.5))
        else:
            previous = " ".join(x for x in content)
            prmpt = previous
            content.append(complete_with_gpt(prmpt, 200, "meta-llama/Llama-3.2-3B", 1500, 0.7, 1.5))

    st.write(content)
    filenamee = to_pdf(convert(create_md(text=content, title=title)))
    with open(filenamee, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(
        label="Download Book",
        data=PDFbyte,
        file_name=filenamee,
        mime="application/octet-stream",
    )
