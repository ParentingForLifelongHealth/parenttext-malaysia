from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel
from parenttext_pipeline.models.parenttext_models import *
from typing import List

class IdGeneratorModel(DataRowModel):
    success_msg: str = ''
    failure_msg: str = ''

class WebhookSettingsModel(DataRowModel):
    url: str = ''
    token: str = ''
#####
# content delivery data models (Malaysia specific)
class Language(ParserModel):
    eng: str = ""
    msa: str = ""

class GoalDataModel(DataRowModel):
    priority_c: str = ""
    priority_p: str = ""
    relationship: List[str] = []
    name_c: Language = Language()


class ModuleDataModel(DataRowModel):
    topic_ID: str = ""
    priority_in_topic: str = ""
    age: List[int] = []
    child_gender: List[str] = []
    name_c: Language = Language()

class GoalTopicLinkModel(DataRowModel):
    goal_id_c: str = ""
    priority_in_goal_c: str = ""
    goal_id_p: str = ""
    priority_in_goal_p: str = ""