# Xorstack Gen-AI Assignment

## Setup Instructions
1. Clone this repo
   ```bash
   git clone https://github.com/<your-username>/xorstack-genai-assignment.git
   cd xorstack-genai-assignment

2. Create virtual environment and install dependencies
   ```bash
    python -m venv venv
    source venv/bin/activate   # Mac/Linux
    venv\Scripts\activate      # Windows
    pip install -r requirements.txt

4. Add your Google API key in .env
   ```bash
    GOOGLE_API_KEY=your_google_api_key

6. Run the FastAPI server
   ```bash
   uvicorn main:app --reload

8. Test the API
   ```bash
    Open http://127.0.0.1:8000/docs in your browser to access the API documentation and test the API.



## API Usage

## Upload a text file:

    curl -X POST "http://127.0.0.1:8000/process-file/" \
         -F "file=@example_input.txt"

## Sample Response
{
  "list_name_date": [
    {"name": "Alice", "date": "2024-01-10", "location": "Delhi"},
    {"name": "Bob", "date": "", "location": ""},
    {"name": "Charlie", "date": "2024-02-15", "location": "Bangalore"}
  ]
}



## Output is also saved in output_files/output_data.csv.

