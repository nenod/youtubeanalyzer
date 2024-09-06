from langchain.chains.qa_with_sources.retrieval import RetrievalQAWithSourcesChain
from langchain_openai import OpenAI
from langchain_community.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
import os
import credentials as creds

os.environ["OPENAI_API_KEY"] = creds.openai_api_key

embeddings = OpenAIEmbeddings()

docsearch = Chroma(persist_directory="db", embedding_function=embeddings)

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0),
                                                    chain_type="stuff",
                                                    retriever=docsearch.as_retriever(search_kwargs={"k": 1}))

def get_analysis(user_input):
    result = chain({"question": user_input}, return_only_outputs=True)
    return result["answer"]