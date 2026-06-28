from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("secret_key")
ALGORITHM = os.getenv("algorithm")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("access_token_expire_minutes", 30))
DATABASE_URL = os.getenv("database_url")