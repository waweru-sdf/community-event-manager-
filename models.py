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

class Event(Base):
    _tablename_="event"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    description=Column(Text)
    date=Column(DateTime)
    location=Column(String)
    organizer_id=Column(Integer,ForeignKey('organaizer.id'))


    organizer= relationship('Organizer' back_populates='employees')

class EventParticipant(Base):
    _tablename_="eventparticipant"
    id=Column(Integer,primary_key=True)
    event_id=Column(Integer,ForeignKey('event'))
    Participant_id=Column(Integer,ForeignKey('participant'))
    role=Column(String)
    registration_dat=Column(DateTime)

    event = relationship('Event',back_populates='employees')
    participant=relationship('Participant',back_populates='participants')


class Participant(Base):
    _tablename_="participant"
    id=Column(Integer,primary_key=True)
    name=ColumnI(String(20))
    email=Column(String(40))
    phone=Column(Integer)
    age=Column(Integer)
    event_id=Column(Integer,ForeignKey('event'))

    event=relationship('Event',back_populates='events')
    

