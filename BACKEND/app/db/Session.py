from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase

import config

engine = create_engine(
    config.DATABASE_URL,
    echo= True
)


class Base(DeclarativeBase):
    pass

def get_db():
    with Session(engine) as session:
        yield session