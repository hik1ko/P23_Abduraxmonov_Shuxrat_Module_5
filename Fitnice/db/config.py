from sqlalchemy import create_engine


class Db:
    DB_USER = 'postgres'
    DB_PORT = 5432
    DB_HOST = 'localhost'
    DB_PASSWORD = '7484728'
    DB_NAME = 'postgres'
    URL = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(Db.URL)