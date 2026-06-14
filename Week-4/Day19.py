# Environment Variables & Security
# n NEVER put API keys in code
# n pip install python-dotenv
# n Create .env: ANTHROPIC_API_KEY=...
# n from dotenv import load_dotenv
# n Add .env to .gitignore IMMEDIATELY
# n .gitignore: .env, __pycache__, *.pyc, venv/

# Environment Variables & Security

import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("Key_Test")

if api_key:
    print(f"✅ Key loaded successfully: {api_key[:3]}...")
else:
    print("❌ No key found — check your .env file")
