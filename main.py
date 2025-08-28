import click
from datetime import datetime
from crud import add_new_organizer,add_new_participant,add_new_event,add_event_participant,view_all_events,delete_event,view_all_organizers,delete_organizer



while True:
    click.secho("welcome to The community event manager app",fg='green')
    click.secho("Select an option before proceeding",fg='blue')
    click.secho("1 Event",fg='yellow')
    click.secho("2 organizer",fg='yellow')
    click.secho("3 participant",fg='yellow')
    click.secho("4 Event_participants",fg='yellow')
    click.secho("5 Exit",fg='red')


    user_input = click.prompt("Select option", type=int)
# OPTION 1 = MATTERS EVENT
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
                add_new_event(title,description,event_date,location)
                click.secho(f"event{title}added successfully")

            except Exception as e:
                click.secho(f"error adding event")

        if event_option==2:
            click.secho("view existing events",fg="green")
            view_all_events()


        if event_option==3:
            click.secho("Delete event",fg="red")
            title=click.prompt("enter event title")
            delete_event(title)
# INPUT 1 END CODE ..........


#INPUT 2 = MATTERS ORGANIZATION
    if user_input==2:
        click.secho("Organizer Options", fg='blue')
        click.secho("1 Add New Organizer", fg='yellow')
        click.secho("2 View  Organizers", fg='yellow')
        click.secho("3 Delete Organizer", fg='yellow')

        organizer_option=click.prompt("Organizers option",type=int)
        if organizer_option == 1:
            click.secho("Adding new organizer......",fg="yellow")
            name =click.prompt("enter organizers name")
            email = click.prompt("enter organizers email")
            phone = click.prompt("enter organizers phone")
            organization = click.prompt("enter organizers organization")
        try:
                add_new_organizer(name,email,phone,organization)
                click.secho(f"organizer with the name {name} added successfully")

        except Exception as e:
                click.secho(f"error adding organizer")


        if organizer_option==2:
            click.secho("view existing organizers",fg="green")
            view_all_organizers()
        
        if organizer_option==3:
            click.secho("Delete organizer",fg="red")
            organizer_id=click.prompt("enter organizers id" ,type=int)
            delete_organizer(organizer_id)
# INPUT 2 END CODE ...................
            

# INPUT 3 = PARTICIPANT 

    if user_input == 3 :
        click.secho("Welcome to participants option")
        click.secho("1 Add participant ",fg="green")
        click.secho("2 view participants",fg="green")
        click.secho("3 Delete participant ",fg="green")

        particpant_option = click.prompt("enter option",type=int)


        if particpant_option ==1:
            click.secho("adding new participant ............",fg="yellow")
            name=click.prompt("enter participants name ")
            email=click.prompt("enter participants email")
            phone=click.prompt("enter participants phone")
            age=click.prompt("enter participants age")
        try:
            add_new_participant(name,email,phone,age)
            click.secho(f"participant with the name {name} added successfully")
        except Exception as e:
            click.secho(f"error adding participant with the name {name}")








        



        
        