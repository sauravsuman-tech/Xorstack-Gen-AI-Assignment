from fastapi import FastAPI, UploadFile, File
import os, uvicorn
from utillity import get_details
app = FastAPI(title="Xorstack Gen-AI Assignment API")

# if not os.path.exists("input_files"):
#     os.makedirs("input_files")
# if not os.path.exists("output_files"):
#     os.makedirs("output_files")

@app.post("/process-file/")
async def process_file(file: UploadFile = File(...)):

    content = await file.read()
    text_content = content.decode("utf-8")
    d=get_details(text_content,"output_data.csv")
    return d
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
