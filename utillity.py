from langchain_google_genai import ChatGoogleGenerativeAI
from models import list_name_date
import csv
from dotenv import load_dotenv
load_dotenv()
def get_details(text:str, output_filename:str):
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        temperature=0,
        max_tokens=None,
        timeout=None,
        max_retries=2,
        
    ).with_structured_output(list_name_date)

    d=llm.invoke(f"get all list of name, dates and location from given text {text}")

    with open(output_filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["name", "date", "location"])
        writer.writeheader()
        for item in d.list_name_date:
            writer.writerow(item.dict())

    return d.model_dump()



