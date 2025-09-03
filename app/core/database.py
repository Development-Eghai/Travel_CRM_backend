from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
import os
import pymysql
pymysql.install_as_MySQLdb()


# ✅ Update the driver to pymysql
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:PixelAdvant%40123@localhost:3306/travel_crm"
)

# ✅ Create engine with pymysql
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# ✅ Session setup
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ Base class for models
Base = declarative_base()

# ✅ Dependency for DB session
def get_db():
    db: Session = SessionLocal()
    try:
        yield db
    finally:
        db.close()
