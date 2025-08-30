# crud.py
from sqlalchemy import Column, Integer, String, Text, Date, ForeignKey
from sqlalchemy.orm import relationship
from models import session, Organizer, Participant, Event, EventParticipant

# -------------------- CRUD OPERATIONS FOR ORGANIZERS -------------------- #

def add_organizer(name, email, phone, organization):
    new_organizer = Organizer(name=name, email=email, phone=phone, organization=organization)
    session.add(new_organizer)
    session.commit()

def view_all_organizers():
    organizers = session.query(Organizer).all()
    if not organizers:
        print("No organizers found.")
        return
    print("\n--- All Organizers ---")
    for organizer in organizers:
        print(f"ID: {organizer.id}")
        print(f"Name: {organizer.name}")
        print(f"Email: {organizer.email}")
        print(f"Phone: {organizer.phone}")
        print(f"Organization: {organizer.organization}")
        print("------------------")

def delete_organizer(organizer_id):
    organizer = session.query(Organizer).filter_by(id=organizer_id).first()
    if not organizer:
        print(f"Organizer with id {organizer_id} not found.")
        return False
    session.delete(organizer)
    session.commit()
    print(f"Organizer '{organizer_id}' deleted successfully.")
    return True

def update_organizer(organizer_id, name=None, email=None, phone=None, organization=None):
    organizer = session.query(Organizer).filter_by(id=organizer_id).first()
    if not organizer:
        print(f"Organizer with id {organizer_id} not found.")
        return False
    if name is not None:
        organizer.name = name
    if email is not None:
        organizer.email = email
    if phone is not None:
        organizer.phone = phone
    if organization is not None:
        organizer.organization = organization
    session.commit()
    print(f"Organizer '{organizer_id}' updated successfully.")
    return True

# -------------------- CRUD OPERATIONS FOR PARTICIPANTS -------------------- #

def add_participant(name, email, phone, age):
    new_participant = Participant(name=name, email=email, phone=phone, age=age)
    session.add(new_participant)
    session.commit()

def view_all_participants():
    participants = session.query(Participant).all()
    if not participants:
        print("No participants found.")
        return
    print("\n--- All Participants ---")
    for participant in participants:
        print(f"ID: {participant.id}")
        print(f"Name: {participant.name}")
        print(f"Email: {participant.email}")
        print(f"Phone: {participant.phone}")
        print(f"Age: {participant.age}")
        print("------------------")

def delete_participant(participant_id):
    participant = session.query(Participant).filter_by(id=participant_id).first()
    if not participant:
        print(f"Participant with id {participant_id} not found.")
        return False
    session.delete(participant)
    session.commit()
    print(f"Participant '{participant_id}' deleted successfully.")
    return True

def update_participant(participant_id, name=None, email=None, phone=None, age=None):
    participant = session.query(Participant).filter_by(id=participant_id).first()
    if not participant:
        print(f"Participant with id {participant_id} not found.")
        return False
    if name is not None:
        participant.name = name
    if email is not None:
        participant.email = email
    if phone is not None:
        participant.phone = phone
    if age is not None:
        participant.age = age
    session.commit()
    print(f"Participant '{participant_id}' updated successfully.")
    return True

# -------------------- CRUD OPERATIONS FOR EVENTS -------------------- #

def add_new_event(title, description, date, location, capacity, organizer_id=None):
    new_event = Event(title=title, description=description, date=date, location=location, capacity=capacity, organizer_id=organizer_id)
    session.add(new_event)
    session.commit()

def view_all_events():
    events = session.query(Event).all()
    if not events:
        print("No events found.")
        return
    print("\n--- All Events ---")
    for event in events:
        print(f"ID: {event.id}")
        print(f"Title: {event.title}")
        print(f"Description: {event.description}")
        print(f"Date: {event.date}")
        print(f"Location: {event.location}")
        print(f"Capacity: {event.capacity}")
        print(f"Organizer ID: {event.organizer_id}")
        print("------------------")

        # Organizer details
        if event.organizer:
            print(f" Organizer: {event.organizer.name} ({event.organizer.email})")
        else:
            print(" Organizer: None")

        
        
    
def delete_event(title):
    event = session.query(Event).filter_by(title=title).first()
    if not event:
        print(f"Event with title '{title}' not found.")
        return False
    session.delete(event)
    session.commit()
    print(f"Event '{title}' deleted successfully.")
    return True

def update_event(event_title, title=None, description=None, date=None, location=None, capacity=None, organizer_id=None):
    event = session.query(Event).filter_by(title=event_title).first()
    if not event:
        print(f"Event with title '{event_title}' not found.")
        return False
    if title is not None:
        event.title = title
    if description is not None:
        event.description = description
    if date is not None:
        event.date = date
    if location is not None:
        event.location = location
    if capacity is not None:
        event.capacity = capacity
    if organizer_id is not None:
        event.organizer_id = organizer_id
    session.commit()
    print(f"Event '{event_title}' updated successfully.")
    return True

# -------------------- OPERATION FOR EVENT PARTICIPANTS -------------------- #

def add_event_participant(event_id, participant_id, role, registration_date):
    event_participant = EventParticipant(event_id=event_id, participant_id=participant_id, role=role, registration_date=registration_date)
    session.add(event_participant)
    session.commit()

def update_event_participant(event_participant_id, event_id=None, participant_id=None, role=None, registration_date=None):
    event_participant = session.query(EventParticipant).filter_by(id=event_participant_id).first()
    if not event_participant:
        print(f"Event Participant with id {event_participant_id} not found.")
        return False
    if event_id is not None:
        event_participant.event_id = event_id
    if participant_id is not None:
        event_participant.participant_id = participant_id
    if role is not None:
        event_participant.role = role
    if registration_date is not None:
        event_participant.registration_date = registration_date
    session.commit()
    print(f"Event Participant '{event_participant_id}' updated successfully.")
    return True