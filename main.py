import click
from datetime import datetime
from crud import add_new_organizer,add_new_participant,add_new_event,add_event_participant



while True:
    click.secho("welcome to The community event manager app",fg='green')
    click.secho("Select an option before proceeding",fg='blue')
    click.secho("1 Event",fg='yellow')
    click.secho("2 Participant",fg='yellow')
    click.secho("3 Organizer",fg='yellow')
    click.secho("4 Event_participants",fg='yellow')
    click.secho("5 Exit",fg='red')


    user_input = click.prompt("Select option", type=int)

    if user_input ==1:
        click.secho("Event Options", fg='blue')
        click.secho("1 Add New event", fg='yellow')
        click.secho("2 View  event", fg='yellow')
        click.secho("3 Delete event", fg='yellow')

        event_option= click.prompt("select event option",type=int)

        if event_option == 1:
            click.secho("Adding new event......",fg="yellow")
            title =click.prompt("enter event title")
            description = click.prompt("enter events description")
            date = click.prompt("enter events date")
            location = click.prompt("enter events location")
            try:
                event_date = datetime.strptime(date, "%d/%m/%Y").date()
            except ValueError:
                print(" Date format inavalid")
        
            try:
                print("Beginning of Try")
                add_new_event(title,description,event_date,location)
                click.secho(f"event{title}added successfully")

            except Exception as e:
                click.secho(f"error adding department")

        if event_option==2:
            click.secho("view existing events",fg="pink")




        
        