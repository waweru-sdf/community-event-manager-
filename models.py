from sqlalchemy import Integer,String,Column,Text,DateTime
from sqlalchemy.orm import relationships,declarative_base 


Base = declarative_base()

class Organaizer(Base):
    _tablename_="organizer"
    id= Column(Integer,primary_key=True)
    name=Column(String(20),nullable=False)
    email=Column(String(40),nullable=False)
    Phone=Column(Integer)
    organization=Column(String(20))
