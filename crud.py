from models import Organizer, Event, EventParticipant, Participant, session


def add_new_organizer(name, email, phone, organization):
    new_organizer = Organizer(
        name=name,
        email=email,
        phone=phone,
        organization=organization
    )
    session.add(new_organizer)
    session.commit()


def add_new_participant(name, email, phone, age):
    new_participant = Participant(
        name=name,
        email=email,
        phone=phone,
        age=age
    )
    session.add(new_participant)
    session.commit()


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
    


def add_event_participant(event_id, participant_id, role="attendee", registration_date=None):
    event_participant = EventParticipant(
        event_id=event_id,
        participant_id=participant_id,
        role=role,
        registration_date=registration_date
    )
    session.add(event_participant)
    session.commit()
