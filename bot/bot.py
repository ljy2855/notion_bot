import logging
import os
import dotenv
from notion_client import APIErrorCode, APIResponseError, Client
from notion_client.typing import SyncAsync

from typing import TYPE_CHECKING, Any
import json

pages = ['229925e222d446fca49f36afa3cc0ca6',
         #'516a26456d394573865700b7f2fe19a9'
         ]

file_path = "./sample.json"
debug = False
dotenv.load_dotenv()

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

    def get_all_databases(self):
        databases = self.notion.search

    def get_database(self,id,start_cursor=None,filter=None) -> SyncAsync[Any]:
        
        kwargs = {
        "database_id": id,
        "filter": filter,
        "start_cursor" : start_cursor,
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
                logging.error(error)
            else:
                # Other error handling code
                logging.error(error)

    def update_page(self,id,new_property:dict):
        page  = self.get_page(id)
        properties = page['properties']
        properties.update(new_property)
        print(properties)
        self.notion.pages.update(page_id=id,properties=properties)
    
    def get_block(self,id):
        try:
            block = self.notion.blocks.children.list(block_id=id)
            return block
        except APIResponseError as error:
            if error.code == APIErrorCode.ObjectNotFound:
                logging.error(error)
            else:
                # Other error handling code
                logging.error(error)
    def init_group(self,id):
        pass

        
    
if __name__ == "__main__":
    bot = NotionBot()
    id = os.environ['PAGE_ID']
    for page in pages:
        blocks = bot.get_block(page)['results']
        print(json.dumps(blocks,ensure_ascii=False,indent=2))
        for block in blocks:
            try:
                title = block['child_database']['title']
                print(title)
                if title == '모임 현황':
                    with open(file_path, 'w') as outfile:
                        json.dump(bot.get_database(block['id']), outfile,ensure_ascii=False,indent=2)
            except KeyError:
                pass
        

    
    # temp = []
    # for page in data:
    #     try:
    #         if page['properties']['진행 상황']['select']['name'] == '진행':
    #             temp.append(page)
    #     except TypeError:
    #         pass
    # for group in temp:
    #     group