from models import Organizer, Event, EventParticipant, Participant, session


# -------------------- CRUD OPERATIONS FOR ORGANIZER -------------------- #

def add_organizer(name, email, phone, organization):
    new_organizer = Organizer(
        name=name,
        email=email,
        phone=phone,
        organization=organization
    )
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


# -------------------- CRUD OPERATIONS FOR PARTICIPANTS -------------------- #

def add_participant(name, email, phone, age):
    new_participant = Participant(
        name=name,
        email=email,
        phone=phone,
        age=age
    )
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


# -------------------- CRUD OPERATIONS FOR EVENTS -------------------- #

def add_new_event(title, description, date, location, organizer_id=None):
    new_event = Event(
        title=title,
        description=description,
        date=date,
        location=location,
        organizer_id=organizer_id
    )
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
        print(f"Organizer ID: {event.organizer_id}")
        print("------------------")


def delete_event(title):
    event = session.query(Event).filter_by(title=title).first()
    if not event:
        print(f"Event with title '{title}' not found.")
        return False
    session.delete(event)
    session.commit()
    print(f"Event '{title}' deleted successfully.")
    return True


# -------------------- OPERATION FOR EVENT PARTICIPANTS -------------------- #

def add_event_participant(event_id, participant_id, role, registration_date):
    event_participant = EventParticipant(
        event_id=event_id,
        participant_id=participant_id,
        role=role,
        registration_date=registration_date  
    )
    session.add(event_participant)
    session.commit()

