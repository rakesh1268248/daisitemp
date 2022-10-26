import streamlit as st
import spacy
from spacy import displacy


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
  
  text = "When Sebastian Thrun started working on self-driving cars at Google in 2007, few people outside of the company took him seriously."

  nlp = spacy.load("en_core_web_sm")
  doc = nlp(text)
  displacy.render(doc, style="ent")
   
if __name__ == "__main__":
  st_ui()
