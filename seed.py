from datetime import date
from models import Organizer, Event, Participant, EventParticipant, Session

def seed_data():
    session = Session()

    # --- Organizers ---
    org1 = Organizer(name="Kilimani Youth Group", email="kilimaniyouth@gmail.com", phone="0712456789", organization="Youth Climate Action")
    org2 = Organizer(name="Westlands Sports Club", email="westlandsports@yahoo.com", phone="0723654321", organization="Community Sports")
    org3 = Organizer(name="Nairobi Tech Hub", email="info@nairobytech.co.ke", phone="0734987123", organization="Technology & Innovation")
    org4 = Organizer(name="Healthy Living Kenya", email="healthylife@ngo.org", phone="0745678912", organization="Health Awareness")
    org5 = Organizer(name="Eastlands Arts Collective", email="eastarts@gmail.com", phone="0756789123", organization="Local Arts & Culture")

    session.add_all([org1, org2, org3, org4, org5])
    session.commit()  # IDs generated

    # --- Events  ---
    event1 = Event(title="Tree Planting Day", description="Join us to plant 500 trees in Karura Forest.", date=date(2025, 9, 10), location="Karura Forest", capacity=120, organizer_id=org1.id)
    event2 = Event(title="Community Football Match", description="Local clubs come together for a friendly match.", date=date(2025, 9, 15), location="Westlands Grounds", capacity=60, organizer_id=org2.id)
    event3 = Event(title="Tech for Good Hackathon", description="Develop solutions to community challenges.", date=date(2025, 9, 20), location="iHub Nairobi", capacity=180, organizer_id=org3.id)
    event4 = Event(title="Health Awareness Walk", description="5km walk to promote healthy living and fitness.", date=date(2025, 9, 25), location="Uhuru Park", capacity=200, organizer_id=org4.id)
    event5 = Event(title="Community Art Fair", description="Showcasing local art, music and culture.", date=date(2025, 9, 30), location="Eastlands Community Hall", capacity=90, organizer_id=org5.id)

    session.add_all([event1, event2, event3, event4, event5])
    session.commit()  

    # --- Participants ---
    p1 = Participant(name="Brian Mwangi", email="brianmwangi@gmail.com", phone="0798456123", age=23)
    p2 = Participant(name="Cynthia Naliaka", email="cynthianaliaka@yahoo.com", phone="0789345612", age=21)
    p3 = Participant(name="George Kamau", email="georgekamau@outlook.com", phone="0723987456", age=27)
    p4 = Participant(name="Salma Hassan", email="salmahassan@gmail.com", phone="0734567812", age=25)
    p5 = Participant(name="Pauline Achieng", email="paulineachieng@gmail.com", phone="0712567894", age=29)

    session.add_all([p1, p2, p3, p4, p5])
    session.commit() 

    # --- Event Participants  ---
    ep1 = EventParticipant(event_id=event1.id, participant_id=p1.id, role="Volunteer", registration_date=date(2025, 9, 5))
    ep2 = EventParticipant(event_id=event1.id, participant_id=p2.id, role="Attendee", registration_date=date(2025, 9, 6))
    ep3 = EventParticipant(event_id=event2.id, participant_id=p3.id, role="Player", registration_date=date(2025, 9, 7))
    ep4 = EventParticipant(event_id=event3.id, participant_id=p4.id, role="Developer", registration_date=date(2025, 9, 8))
    ep5 = EventParticipant(event_id=event4.id, participant_id=p5.id, role="Walker", registration_date=date(2025, 9, 9))
    ep6 = EventParticipant(event_id=event5.id, participant_id=p1.id, role="Exhibitor", registration_date=date(2025, 9, 10))
    ep7 = EventParticipant(event_id=event3.id, participant_id=p2.id, role="Designer", registration_date=date(2025, 9, 11))
    ep8 = EventParticipant(event_id=event4.id, participant_id=p3.id, role="Volunteer", registration_date=date(2025, 9, 12))
    ep9 = EventParticipant(event_id=event5.id, participant_id=p4.id, role="Performer", registration_date=date(2025, 9, 13))
    ep10 = EventParticipant(event_id=event2.id, participant_id=p5.id, role="Coach", registration_date=date(2025, 9, 14))

    session.add_all([ep1, ep2, ep3, ep4, ep5, ep6, ep7, ep8, ep9, ep10])
    session.commit()

    session.close()
    print("Database seeded ")

if __name__ == "__main__":
    seed_data()
