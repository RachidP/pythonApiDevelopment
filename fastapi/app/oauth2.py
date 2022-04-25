from jose import JWSError, jwt
from pydantic import SecretBytes
from datetime import datetime, timedelta

# SECRET_KEY
# Algorithm
# expration time

# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "a3bab119c3d0330538acdb7e397606d25ff18bdfb1ab38541ecb99a0baac8f8d"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
