import os

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")

engine = create_engine(SQLALCHEMY_DATABASE_URI)
res = engine.execute("SELECT 1").scalar()
print(res)
