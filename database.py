from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# اتصال بقاعدة البيانات PostgreSQL
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1234@localhost/postgres"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# دالة لجلب السيشن
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
