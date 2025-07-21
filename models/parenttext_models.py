from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel
from parenttext_pipeline.models.parenttext_models import *
from typing import List




del ComicBlockModel
del TipsBlockModel

class ComicBlockModel(ParserModel):
    intro: list[str] = []
    file_name: str = ""
    n_attachments: str = ""
    next_button: str = ""
    text: list[str] = []

class TipsBlockModel(ParserModel):
    intro: list[str] = []
    next_button: str = ""
    message: list[TipModel] = []
