# COMMUNITY EVENT MANAGER

## Author 
Felix waweru

## Description 
The Community Event Manager is a project that would help communities manage their events well and in a structured way

## Features

+ Event Management: Add, view, update, and delete events.

+ Participant Management: Add, view, update, and delete participants.

+ Organizer Management: Add, view, update, and delete organizers.

+ Event-Participant Linking: Assign participants to events with specific roles and registration dates and update event participant .

- Relational Database: Events are linked to organizers, and participants are linked to events.

## Database schema

The database schema includes four tables:

1 Organizers

 - id, name, email, phone, organization

2 Participants

- id, name, email, phone, age

3 Events

- id, title, description, date, location, organizer_id, capacity

4 Event Participants (linking table)

- id, event_id, participant_id, role, registration_date

5 Relationships:

 - One Organizer → Many Events

 - One Event → Many Participants (via EventParticipant)

 - One Participant → Many Event Participations


## Language 

Python

## Dependencies

SQLAlchemy

Alembic

Click

Pipenv 


## Installation & Setup

1. **Clone the repository**

   ```bash
   git clone <git@github.com:waweru-sdf/community-event-manager-.git>
   cd community-event-manager
   open in vscode code .

2. install dependencies 
   
   - pipenv install
   - pipenv 
   
3. Run migrations 

   - alembic upgrade head

4. Seed database

   - python seed.py

3. Run app 

   - python main.py

## usage 

1 Event Options
- 1 View Events
- 2 Add Event
- 3 Delete Event
- 4 Update Event


2 organizer option
- 1 View Organizers
- 2 Add Organizer
- 3 Delete Organizer
- 4 Update Organizer

3 Participant option
- 1 View Participants
- 2 Add Participant
- 3 Delete Participant
- 4 Update Participant

4 Event participant option
- 1 Add EventParticipant
- 2 Update EventParticipant

## License

MIT License


Copyright (c) 2025 Felix Waweru


Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:


THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND.

