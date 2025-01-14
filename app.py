from flask import Flask, render_template, request
from src.helper import download_hugging_face_embeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.llms import CTransformers
import os
from src.prompt import *
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Load Hugging Face embeddings
embeddings = download_hugging_face_embeddings()

# Initialize Pinecone
PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
index_name = "medibot"

if not PINECONE_API_KEY:
    raise ValueError("Pinecone API Key is missing!")

# Load Pinecone index
docsearch = PineconeVectorStore.from_existing_index(index_name, embeddings)
print("Pinecone index loaded successfully.")

# Define prompt template
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

# Load the language model
llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={
        'max_new_tokens': 256,
        'temperature': 0.5,
        'repetition_penalty': 1.3,
        'top_p': 0.9,
        'stop': ["\n", ".", "?", "!"]
    }
)

# Initialize QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_type="mmr", search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Flask routes
@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User Input:", msg)
    try:
        result = qa.invoke({"query": msg})
        print("Response:", result["result"])
        return str(result["result"])
    except Exception as e:
        print("Error:", str(e))
        return "Sorry, something went wrong."

# Run the app
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
