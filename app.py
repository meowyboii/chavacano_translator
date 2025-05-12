import streamlit as st
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast
import torch

@st.cache_resource
def load_model():
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = MBartForConditionalGeneration.from_pretrained("meowyboi/mbart-large-50-en-cbk-finetuned").to(device)
    tokenizer = MBart50TokenizerFast.from_pretrained("meowyboi/mbart-large-50-en-cbk-finetuned")
    return model, tokenizer, device

model, tokenizer, device = load_model()

# Streamlit UI
st.title("English to Chavacano Translator")
st.subheader("Enter an English sentence, and the model will translate it into Chavacano.")

# Input text box
input_text = st.text_area("Enter your English text here:", value="", height=100)

if st.button("Translate"):
    if input_text.strip():
        with st.spinner("Translating..."):
            inputs = tokenizer(input_text, return_tensors="pt").to(device)
            outputs = model.generate(**inputs, forced_bos_token_id=tokenizer.convert_tokens_to_ids("<cbk_XX>"))
            translated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
            st.success("Translation complete!")
            st.write(translated_text)
    else:
        st.warning("Please enter text to translate!")
