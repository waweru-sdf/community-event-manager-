import click

from crud import add_new_organizer,add_new_participant,add_new_event,add_event_participant



while True:
    click.secho("welcome to The community event manager app",fg='white')
    click.secho("Select an option before proceeding",fg='blue')
    click.secho("1 Event",fg='yellow')
    click.secho("2 Participant",fg='yellow')
    click.secho("1 Organizer",fg='yellow')
    click.secho("1 Event_participants",fg='yellow')


    user_input = click.prompt("Select option", type=int)