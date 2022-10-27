from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from src.database.config import SQLITE_ENGINE_URL
from src.database.models import Base


engine = create_engine(SQLITE_ENGINE_URL)
Base.metadata.create_all(engine)

session = Session(bind=engine)
