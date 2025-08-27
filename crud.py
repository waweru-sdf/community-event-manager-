from models import Organizer, Event, EventParticipant, Participant,session



def add_new_organizer( organizer_id id ,name ,email, phone,age )
    new_organizer= Organizer(organizer_id=organizer_id ,name=name ,email=email, phone=phone,age=age )
    session.add(new_organizer)
    session.commit()