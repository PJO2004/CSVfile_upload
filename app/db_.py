from db.database import SessionLocal, engine, Base
from db.modelling import file_modeling, in_data
from db import models

Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if __name__ == "__main__":
    tn, df, columns, index = file_modeling()
    in_data(tn=tn, df=df, columns=columns, index=index)
