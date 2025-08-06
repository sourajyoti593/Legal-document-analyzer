from fastapi import FastAPI, UploadFile
from app.ingest import ingest_pdf
from app.query_handler import answer_query

app = FastAPI()

@app.post("/upload")
def upload_doc(file: UploadFile):
    path = f"temp/{file.filename}"
    with open(path, "wb") as f:
        f.write(file.file.read())
    return ingest_pdf(path)

@app.get("/query")
def query(q: str):
    return {"answer": answer_query(q)}
