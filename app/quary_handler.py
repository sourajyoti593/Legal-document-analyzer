from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.vectorstores import Pinecone

llm = ChatOpenAI(temperature=0.2)
retriever = Pinecone.from_existing_index("legal-docs", OpenAIEmbeddings()).as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

def answer_query(question: str):
    return qa_chain.run(question)
