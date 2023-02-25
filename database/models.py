from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    key = Column(String, unique=True, index=True)
    email = Column(String, index=True)
    name = Column(String)
    is_active = Column(Boolean, default=True)

    


class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    user = relationship("User", foreign_keys=[user_id],uselist=False)
    group_id = Column(Integer,ForeignKey("groups.id"))
    group = relationship("Group", foreign_keys=[group_id], uselist=False)
    write_target = Column(Integer)
    write_process = Column(Integer)
    
    
class Group(Base):
    __tablename__ = "groups"

    id = Column(Integer, primary_key=True, index=True)
    dashboard_id = Column(String)
    board_id = Column(String)
    page_id = Column(String, unique=True)
    title = Column(String, index=True)
    description = Column(String, index=True)

    participants = relationship("Participant", uselist= True)
    
# class User(BaseModel):
#     nickname = str
#     id = str

# class Database(BaseModel):
#     id : str
#     name : str


# class GroupPage(BaseModel):
#     url = str
#     page_id = str
#     name = str
#     users = list[User] 
    

