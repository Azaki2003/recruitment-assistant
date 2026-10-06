import os
from dotenv import load_dotenv

load_dotenv()

print("Ollama model:", os.getenv("OLLAMA_MODEL"))

import googleapiclient
import pypdf
import docx
import ollama
print("All libraries imported successfully")