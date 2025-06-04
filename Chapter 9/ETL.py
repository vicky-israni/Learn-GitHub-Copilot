# Build a Python script to read a CSV, validate rows using Pydantic, 
# and insert valid records into PostgreSQL.”
import csv
import os
import psycopg2
from pydantic import BaseModel, ValidationError
from typing import List, Optional
from dotenv import load_dotenv
from datetime import datetime
# Load environment variables from .env file
load_dotenv()
# Database connection parameters
DB_HOST = os.getenv('DB_HOST')
DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_PORT = os.getenv('DB_PORT')
# Define the Pydantic model for validation

class Record(BaseModel):
    id: int
    name: str
    email: str
    age: Optional[int] = None
    created_at: datetime = datetime.now()
    # Add more fields as per your CSV structure
# Define a function to read the CSV file and validate records
def read_and_validate_csv(file_path: str) -> List[Record]:
    valid_records = []
    invalid_records = []
    with open(file _path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                record = Record(**row)
                valid_records.append(record)
            except ValidationError as e:
                print(f"Validation error for row {row}: {e}")
                invalid_records.append(row)
    return valid_records, invalid_records

              