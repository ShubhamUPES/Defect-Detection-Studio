from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pathlib import Path

APP_DIR = Path(__file__).parent
DB_PATH = APP_DIR / "inspectx.db"

engine = create_engine(f"sqlite:///{DB_PATH}", echo=False, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)


def init_db():
    from app.database.models import Base
    Base.metadata.create_all(engine)


def get_session():
    return Session()
