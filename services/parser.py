import json
from bot.bot import NotionBot
from database import schemas, crud
from sqlalchemy.orm import Session

bot = NotionBot()
def get_id_from_url(url:str) -> str:
    return url[-32:]

    
def init_parse_group(id : str, db: Session):
    group = crud.get_group_by_page_id(db,id)
    if group:
        return group
    blocks = bot.get_block(id)['results']
    print(json.dumps(blocks,ensure_ascii=False,indent=2))
    for block in blocks:
        try:
            title = block['child_database']['title']
            print(title)
            if title == '모임 현황':
                data = bot.get_database(block['id'])
                update_or_create_user(data)
                print(json.dumps(data,ensure_ascii=False,indent=2))

                # with open(file_path, 'w') as outfile:
                #     json.dump(bot.get_database(block['id']), outfile,ensure_ascii=False,indent=2)
        except KeyError:
            pass

def update_or_create_user(json : dict):
    pass