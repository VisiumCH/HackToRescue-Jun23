import base64
import logging
import logging.handlers
from os import mkdir
from os.path import exists
import os

import streamlit as st
from model import ChatGPTModel


#############################
# GLOBAL PAGE STYLE
#############################

st.set_page_config(page_title="Peptide Translator", page_icon=None, layout="centered", menu_items=None)
st.markdown("<style>#MainMenu {visibility: hidden;} footer {visibility: hidden;}</style>", unsafe_allow_html=True)


#############################
# LOGGER
#############################

LOGS_PATH = "logs"

@st.cache_resource
def get_logger():
    if not exists(LOGS_PATH):
        mkdir(LOGS_PATH)
    log_file_name = os.path.join(LOGS_PATH, "translator.log")  # 'logs/translator.log'
    logging_level = logging.DEBUG if os.getenv("DEBUG", default=False) else logging.INFO
    formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s | %(message)s")
    handler = logging.handlers.TimedRotatingFileHandler(log_file_name, when="D", interval=1, backupCount=0)
    handler.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(handler)
    logger.setLevel(logging_level)
    return logger


logger = get_logger()

#############################
# LOAD MODEL
#############################


@st.cache_resource
def load_model():
    return ChatGPTModel()


model = load_model()


#############################
# UTIL FUNCTIONS
#############################


def change_input() -> None:
    st.session_state.model_outputs = []
    st.session_state.success_message = None


def submit_input() -> None:
    """Submit input form."""
    st.session_state.model_outputs = model.predict(st.session_state.input_key)
    st.session_state.success_message = None


def save_output() -> None:
    """Notify translation saved."""
    st.session_state.success_message = (
        f"Translation saved: {st.session_state.input_key} -> {st.session_state.output_key}"
    )
    request_dict = {
        "request": st.session_state.input_key,
        "outputs": st.session_state.model_outputs,
    }
    logger.info(f"REQUEST {request_dict}")


#############################
# SESSION VARIABLES
#############################

if "model_outputs" not in st.session_state:
    st.session_state.model_outputs = []
if "success_message" not in st.session_state:
    st.session_state.success_message = None
if "input_note_key" not in st.session_state:
    st.session_state.input_note_key = ""

#############################
# TRANSLATOR
#############################


def display_translator():
    col1, col2 = st.columns(2)

    with col1:
        st.text_input(r"Please enter the query:", key="input_key", on_change=change_input)
        st.button("Retrieve relevant results", on_click=submit_input)

    with col2:
        st.radio(
            label=r"2\. Top 5 AI generated translations, select the best one:",
            options=st.session_state.model_outputs,
            index=0,
            key="output_key_select",
        )

    with st.container():
        if st.session_state.success_message is not None:
            st.success(st.session_state.success_message)


display_translator()