import os
from flask import Flask
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables
load_dotenv()

# Read Supabase credentials from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route('/')
def home():
    return {"message": "Flask API connected to Supabase"}

if __name__ == '__main__':
    app.run(debug=True)
