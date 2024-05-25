from sqlalchemy import create_engine
from sqlalchemy.orm import Session, DeclarativeBase, MappedAsDataclass

import config

engine = create_engine(
    config.DATABASE_URL,
    echo= True
)


class Base(DeclarativeBase, MappedAsDataclass):
    pass

def get_db():
    with Session(engine) as session:
        yield session