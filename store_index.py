
from src.helper import load_pdf, text_split, download_hugging_face_embeddings
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore

import os
from dotenv import load_dotenv

load_dotenv()


PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
# print(PINECONE_API_ENV)

extracted_data = load_pdf(data='c:/Users/Deepak/Project/Medical-Chatbot-GenAI/Data')
text_chunks=text_split(extracted_data)
embeddings = download_hugging_face_embeddings()


pc = Pinecone(api_key=PINECONE_API_KEY)

index_name = "medical-bot"


pc.create_index(
    name=index_name,
    dimension=384, 
    metric="cosine", 
    spec=ServerlessSpec(
        cloud="aws", 
        region="us-east-1"
    ) 
) 


#Creating Embeddings for Each of The Text Chunks & storing
docsearch=PineconeVectorStore.from_texts([t.page_content for t in text_chunks], embeddings, index_name=index_name)