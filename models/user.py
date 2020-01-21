import asyncpgsa
from sqlalchemy import (
            MetaData, Table, Column, ForeignKey,
                Integer, String, DateTime, Date, VARCHAR
                
        )
from sqlalchemy.sql import select

metadata = MetaData()

users = Table(
    'users', metadata,

    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(255)),
    Column('secondname', VARCHAR(255)),
    Column('email', VARCHAR(255), unique=True),
    Column('phone', Integer, unique=True),
    Column('birthday', Date),
    Column('occupation', VARCHAR(255)),
    Column('city', VARCHAR(40)),
    Column('groups_id', Integer),
    Column('password', Integer)
)

groups = Table(
    'groups', metadata,
     
    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(255))
)




class User:

    @staticmethod 
    async def get_all_users(db):
        records = await db.fetch(
            users.select()
        )
        return records
    
    @staticmethod
    async def get_user_by_email(db, email):
        user = await db.fetchrow(
            users.select().where(users.c.email == email)
        )
        return user

    @staticmethod
    async def get_user_by_id(db, user_id):
        user = await db.fetchrow(
            users.select().where(users.c.id == user_id)
        )
        return user
    
    @staticmethod
    async def create_user(db, name, secondname, email, birthday, phone, occupation, city, password):
        new_user = users.insert().values(name = name, secondname = secondname, email = email, phone = phone, birthday = birthday, occupation = occupation, city = city, password = password)
        await db.execute(new_user)
