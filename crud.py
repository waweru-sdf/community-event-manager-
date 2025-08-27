from models import Organizer, Event, EventParticipant, Participant,session



def add_new_organizer( organizer_id  ,name ,email, phone,organization )
    new_organizer= Organizer(organizer_id=organizer_id ,name=name ,email=email, phone=phone,organization=organization )
    session.add(new_organizer)
    session.commit()


def add_new_participant( event_id  ,name ,email, phone,age )
    new_participant=Participant(organizer_id=organizer_id ,name=name ,email=email, phone=phone,age=age )
    session.add(new_participant)
    session.commit()


def add_new_event(event_id,title,description,date,location,organization_id=none)
    new_event=Event(event_id=event_id,title=title,description=description,date=date,location=location,organization_id=organization_id)
    session.add(new_event)
    session.commit()




def add_event_participant(event_participant_id, event_id, participant_id, role="attendee",date=none):
    event_participant = EventParticipant(
        event_participant_id=event_participant_id
        event_id=event_id,
        participant_id=participant_id,
        role=role,
        date=date
    )
    session.add(event_participant)
    session.commit()
