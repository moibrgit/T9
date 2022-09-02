# pip install sqlalchemy

from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, create_engine
from sqlalchemy import desc 

import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)


# Define DB Information
connection_string = "sqlite:///wbs.db"

# Base Class to create Tables (Schema)
Base = declarative_base()

# DB Engine
engine = create_engine(connection_string, echo = True)

# DB Session
Session = sessionmaker()


class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer(), primary_key=True)    
    
    username = Column(String(25), nullable = False, unique = True)
    password = Column(String(25), nullable = False, unique = False)
    email = Column(String(100), nullable = True, unique = False)
    
    
    
    def __repr__(self):
        return f"User--->{self.email} - {self.username}"
    
    
def create_db():
      Base.metadata.create_all(engine)
    
def  add_new_user():
    local_session = Session(bind=engine)
    
    new_user = User(id = 1, username = "Thomas", password = "ABCD1", email="thomas@wbs.com")
    
    local_session.add(new_user)
    
    local_session.commit()
    
def add_several_users():
    local_session = Session(bind=engine)
    
    users = [
        {
            "id": 2,
            "username": "Sven",
            "password" : "ABCD",
            "email": "sven@wbs.com"
        },
        {
            "id": 3,
            "username": "Sara",
            "password" : "ABCD",
            "email": "Sara@wbs.com"
        },
    ]  
    
    for user in users:
        new_user = User(id = user["id"], username = user["username"], password = user["password"], email=user["email"])
        local_session.add(new_user)    
        local_session.commit()
    

def retrieve_all_records():
    local_session = Session(bind=engine)
    
    #users = local_session.query(User).all()[:3]
    users = local_session.query(User).all()
    print(type(users)) # <class 'list'>
    
    
    for user in users:
        print(user, type(user))
        
def retrieve_signle_records():
    local_session = Session(bind=engine)
    
    sara = local_session.query(User).filter(User.username == "Sara").first()
    
    print(sara) # User--->Sara@wbs.com - Sara
    print(type(sara)) # <class '__main__.User'>
    
def update_record():
    local_session = Session(bind=engine)
    
    sara = local_session.query(User).filter(User.username == "Sara").first()   
    
    sara.email = "Sara2@wbs.com"
    
    local_session.commit()
    
def delete_record():
    local_session = Session(bind=engine)
    
    sara = local_session.query(User).filter(User.username == "Sara").first()   
    
    local_session.delete(sara)
        
    local_session.commit()
  
def main():
    
    # create_db()
    
    # add_new_user()

    # add_several_users()
    
    # retrieve_all_records()
    
    # retrieve_signle_records()
    
    # update_record()
    
    delete_record()
    
if __name__ == "__main__":
    main()