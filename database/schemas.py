from pydantic import BaseModel



class ParticipantBase(BaseModel):
    user : int
    group : int

class ParticipantCreate(ParticipantBase):
    pass
class Participant(ParticipantBase):
    id : int
    class Config:
        orm_mode = True
#Group
class GroupBase(BaseModel):
    title : str
    page_id : str

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id : int
    participants: list[Participant] = []
    class Config:
        orm_mode = True

#User
class UserBase(BaseModel):
    key: str


class UserCreate(UserBase):
    name: str


class User(UserBase):
    id: int
 
    participants: list[Participant] = []

    class Config:
        orm_mode = True