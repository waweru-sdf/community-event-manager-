from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey,create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

Base = declarative_base()

class Organizer(Base):
    __tablename__ = "organizers"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    organization = Column(String(100))

    events = relationship("Event", back_populates="organizer")

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    age = Column(Integer)

    event_participations = relationship("EventParticipant", back_populates="participant")

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    description = Column(Text)
    date = Column(Date)
    location = Column(String(100))
    organizer_id = Column(Integer, ForeignKey("organizers.id"))
    capacity = Column(Integer, nullable=True)

    organizer = relationship("Organizer", back_populates="events")
    participants = relationship("EventParticipant", back_populates="event")

class EventParticipant(Base):
    __tablename__ = "event_participants"

    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey("events.id"))
    participant_id = Column(Integer, ForeignKey("participants.id"))
    role = Column(String(20))  # attendee, volunteer, speaker
    registration_date = Column(Date)
    event = relationship("Event", back_populates="participants")
    participant = relationship("Participant", back_populates="event_participations")


engine = create_engine("sqlite:///Events.db",echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()

