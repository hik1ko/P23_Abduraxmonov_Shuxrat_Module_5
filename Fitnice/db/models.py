from datetime import datetime

from sqlalchemy import BigInteger, VARCHAR, Column, DateTime
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

from Fitnice.db.config import engine


class Base(DeclarativeBase):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower() + 's'

class CreatedModel(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)

class User(CreatedModel):
    user_id: Mapped[int] = mapped_column(BigInteger, unique=True)
    username: Mapped[str] = mapped_column(VARCHAR(255), nullable=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255))
    is_admin: Mapped[bool] = mapped_column(default=False)

    def __repr__(self):
        return self.full_name

Base.metadata.create_all(engine)