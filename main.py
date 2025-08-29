from datetime import datetime
import click
from crud import (add_new_event, view_all_events, delete_event, add_participant, view_all_participants, delete_participant, add_organizer, view_all_organizers, delete_organizer,add_event_participant)


while True:
    click.secho("Welcome to The Community Event Manager App", fg='green')
    click.secho("Select an option before proceeding", fg='blue')
    click.secho("1 Event", fg='yellow')
    click.secho("2 Participant", fg='yellow')
    click.secho("3 Organizer", fg='yellow')
    click.secho("4 Event Participants", fg='yellow')
    click.secho("5 Exit", fg='red')

    user_input = click.prompt("Select option", type=int)

    # ---------------- EVENT MENU ----------------
    if user_input == 1:
        click.secho("Event Options", fg='blue')
        click.secho("1 View Events", fg='yellow')
        click.secho("2 Add Events", fg='yellow')
        click.secho("3 Delete Event", fg='yellow')

        event_option = click.prompt("Select event option", type=int)

        if event_option == 1:
            click.secho("Viewing existing events...", fg="yellow")
            view_all_events()



        elif event_option == 2:
            click.secho("Adding new event......", fg="yellow")
            title = click.prompt("Enter event title")
            description = click.prompt("Enter events description")
            date = click.prompt("Enter events date (dd/mm/yyyy)")
            location = click.prompt("Enter events location")

            try:
                event_date = datetime.strptime(date, "%d/%m/%Y").date()
                add_new_event(title, description, event_date, location)
                click.secho(f"Event '{title}' added successfully!", fg="green")
            except ValueError:
                click.secho("Invalid Date format. Use dd/mm/yyyy", fg="red")
            except Exception:
                click.secho("Error adding event", fg="red")

        elif event_option == 3:
            click.secho("Delete event", fg="red")
            title = click.prompt("Enter event title")
            delete_event(title)

    # ---------------- PARTICIPANT MENU ----------------
    elif user_input == 2:
        click.secho("Participant Options", fg='blue')
        click.secho("1 Add Participant", fg='yellow')
        click.secho("2 View Participants", fg='yellow')
        click.secho("3 Delete Participant", fg='yellow')

        participant_option = click.prompt("Select participant option", type=int)

        if participant_option == 1:
            name = click.prompt("Enter participant name")
            email = click.prompt("Enter participant email")
            phone = click.prompt("Enter participant phone")
            age = click.prompt("Enter participant age")
            add_participant(name, email, phone,age)
            click.secho("PARTICIPANT ADDED SUCCESSFULLY",fg="green")
        elif participant_option == 2:
            view_all_participants()
        elif participant_option == 3:
            pid = click.prompt("Enter participant ID", type=int)
            delete_participant(pid)

    # ---------------- ORGANIZER MENU ----------------
    elif user_input == 3:
        click.secho("Organizer Options", fg='blue')
        click.secho("1 Add Organizer", fg='yellow')
        click.secho("2 View Organizers", fg='yellow')
        click.secho("3 Delete Organizer", fg='yellow')

        organizer_option = click.prompt("Select organizer option", type=int)

        if organizer_option == 1:
            name = click.prompt("Enter organizer name")
            email = click.prompt("Enter organizer email")
            phone = click.prompt("Enter organizer phone")
            organization = click.prompt("Enter organization")
            add_organizer(name, email, phone, organization)
        elif organizer_option == 2:
            view_all_organizers()
        elif organizer_option == 3:
            oid = click.prompt("Enter organizer ID", type=int)
            delete_organizer(oid)

    # ---------------- EVENT PARTICIPANT MENU ----------------

    elif user_input == 4:
        click.secho("Event Participants Options", fg='blue')
        click.secho("1 Assign Participant to Event", fg='yellow')

        ep_option = click.prompt("Select event participant option", type=int)

        if ep_option == 1:
            event_id = click.prompt("Enter event ID", type=int)
            participant_id = click.prompt("Enter participant ID", type=int)
            role = click.prompt("Enter role (e.g., Speaker, Attendee, Volunteer)")
            registration_date_str = click.prompt("Enter registration date (DD-MM-YYYY)")

        try:
            
            registration_date = datetime.strptime(registration_date_str, "%d-%m-%Y").date()
            add_event_participant(event_id, participant_id, role, registration_date)
            click.secho("Event participant added successfully!", fg="green")
        except ValueError:
            click.secho("Invalid Date format. Use DD-MM-YYYY", fg="red")



            #--------------------------------EXIT APP -------------------------

    elif user_input == 5:
        click.secho("Exiting program...", fg="red")
        break
