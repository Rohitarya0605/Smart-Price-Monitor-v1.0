from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# ====================================
# DATABASE CONFIG
# ====================================
DATABASE_URL = "sqlite:///./price_monitor.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


# ====================================
# OPTIONAL DB SESSION HELPER
# ====================================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()