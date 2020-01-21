import asyncpgsa
from sqlalchemy import (
            MetaData, Table, Column, ForeignKey,
                Integer, String, DateTime, Date, VARCHAR
                
        )
from sqlalchemy.sql import select

metadata = MetaData()

projects = Table(
    'projects', metadata,

    Column('id', Integer, primary_key=True),
    Column('name', VARCHAR(255)),
    Column('company', VARCHAR(255)),
    Column('author_id', Integer),
    Column('presentation', VARCHAR(255)),
    Column('deadline', VARCHAR(255)), 
    Column('gift', VARCHAR(255)),
    Column('video', VARCHAR(255)),

)

class Project:

    @staticmethod
    async def get_all_projects(db):
        project = await db.fetch(
            projects.select()
        )
        return project

    @staticmethod
    async def get_project_by_id(db, project_id):
        project = await db.fetchrow(
           projects.select().where(projects.c.id == project_id)
        )
        return project
    
    @staticmethod
    async def get_project_by_userid(db, user_id):
        project = await db.fetchrow(
            projects.select().where(projects.c.author_id == user_id)
        )
        return project
