import logging
import os
from notion_client import APIErrorCode, APIResponseError, Client
from notion_client.typing import SyncAsync

from typing import TYPE_CHECKING, Any

debug = False


class NotionBot():
    notion : Client

    def __init__(self) -> None:
        try:
            api_key = os.environ["NOTION_API_KEY"]
            if debug is True:
                self.notion = Client(auth=api_key,log_level=logging.DEBUG)
            else:
                self.notion = Client(auth=api_key)
        except KeyError as error:
            logging.error(error)

    def get_user_info(self) -> None:
        print(self.notion.users.list())
    def update_database(self,id,):
        self.notion.databases.update()

    def get_database(self,id,filter=None) -> SyncAsync[Any]:
        
        kwargs = {
        "database_id": id,
        "filter": filter,
        }
        try:
            database = self.notion.databases.query(
                **kwargs
            )
            return database['results']
        except APIResponseError as error:
            if error.code == APIErrorCode.ObjectNotFound:
                ...  # For example: handle by asking the user to select a different database
            else:
                # Other error handling code
                logging.error(error)
        
    def get_page(self,id) -> SyncAsync[Any]:
        try:
            page = self.notion.pages.retrieve(page_id=id)
            return page
        except APIResponseError as error:
            if error.code == APIErrorCode.ObjectNotFound:
                ...  # For example: handle by asking the user to select a different database
            else:
                # Other error handling code
                logging.error(error)

    def update_page(self,id,new_property:dict):
        page  = self.get_page(id)
        properties = page['properties']
        properties.update(new_property)
        print(properties)
        self.notion.pages.update(page_id=id,properties=properties)

class NotionManager():
    bot : NotionBot

        
    
    