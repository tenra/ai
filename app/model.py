# -*- coding: utf-8 -*-
# モデルの定義
from sqlalchemy import Column, Integer, String
from pydantic import BaseModel
from db import Base
from db import ENGINE


# userテーブルのモデルUserTableを定義
class UserTable(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    age = Column(Integer)
    email = Column(String(128), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    #delete_flag = Column(Boolean, default=0)
    #created_at = Column(DateTime)
    #updated_at = Column(DateTime)


# POSTやPUTのとき受け取るRequest Bodyのモデルを定義
class User(BaseModel):
    id: int
    name: str
    age: int
    email: str
    password: str
    delete_flag: bool
    #created_at: datetime.datetime
    #updated_at: datetime.datetime


def main():
    # テーブルが存在しなければ、テーブルを作成
    Base.metadata.create_all(bind=ENGINE)


if __name__ == "__main__":
    main()
