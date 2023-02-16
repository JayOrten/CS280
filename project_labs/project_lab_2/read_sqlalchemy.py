from models.config import Session #You would import this from your config file
from models.users import User


session = Session()

#This will retrieve all of the users from the database
session.query(User).all() 

#This will retrieve the user who's username is NASA
nasaUser = session.query(User).filter(User.username == "NASA").first()

#You can then print the username of the user you retrieved
print(nasaUser.username)

#We recommend that you reassign the user to a variable so that you can use it later
nasaUsername = nasaUser.username

#This will close the session that you opened at the beginning of the file.

session.close()