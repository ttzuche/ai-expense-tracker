import os
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from supabase import create_client, Client

# Load environment variables
load_dotenv()

# Read Supabase credentials from .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Initialize Supabase client
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Flask API connected to Supabase"}), 200

@app.route('/get-expenses', methods=['GET'])
def get_expenses():
    response = supabase.table('expenses').select("*").execute()
    return jsonify(response.data), 200

@app.route('/add-expense', methods=['POST'])
def add_expense():
    try:
        data = request.get_json()
        
        if "title" not in data or "amount" not in data:
            return jsonify({"error": "Title and amount are required"}), 400
        
        response = supabase.table('expenses').insert({
            "title": data["title"],
            "amount": data["amount"],
            "category": data.get("category", "Other"),
            "date": data.get("date")
        }).execute()

        return jsonify({"message": "Expense added", "data": response.data}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)
