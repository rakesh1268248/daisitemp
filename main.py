import streamlit as st
import spacy
from spacy_streamlit import visualize_ner


def st_ui():
  st.set_page_config(layout = "wide")
  st.title("Auto Review Legal contracts - DocumentAI")  
  fileupload = st.sidebar.file_uploader("Upload a Contract here")
  select_category = st.sidebar.selectbox("select_category", ["Summarization", "Sentiment Analytics", "Risk Analytics","Price Analytics","People/Stakeholders Analytics","Spatial Analytics",
                                                             "Text To Search","Grid Analytics","Social Analytics","Conversation-Transcripts Analytics","Non English Text","Filter Non English",
                                                            "List Of Languages","Display Full English Version","Full Document Translation"])
  Button=st.sidebar.button('content Analytics')
  #button=st.sidebar.button('Risk Analytics')
  Enter_text = st.sidebar.text_input("Text to search")
  
  nlp = spacy.load("en_core_web_sm")
  doc = nlp("Sundar Pichai is the CEO of Google.")
  visualize_ner(doc, labels=nlp.get_pipe("ner").labels)
  
   
if __name__ == "__main__":
  st_ui()
