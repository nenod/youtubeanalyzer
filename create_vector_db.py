from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import Chroma
from chromadb.utils import embedding_functions
import os
import youtube_transcriptor as yttrans
import shutil
import credentials as creds


def create_db(video_url):
    os.environ["OPENAI_API_KEY"] = creds.openai_api_key

    transcript = yttrans.get_transcript(video_url)

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)

    texts = text_splitter.split_text(transcript)

    embeddings = OpenAIEmbeddings()

    docsearch = Chroma.from_texts(texts,
                                  embeddings,
                                   metadatas=[{"source": f"Text chunk {i} of {len(texts)}"} for i in range(len(texts))], 
                                persist_directory="db")

    
