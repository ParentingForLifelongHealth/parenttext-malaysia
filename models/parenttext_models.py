from rpft.parsers.creation.datarowmodel import DataRowModel
from rpft.parsers.common.rowparser import ParserModel



from parenttext_pipeline.models.parenttext_models import *
from typing import List





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

class PlhContentModel(DataRowModel):
    module_name: str = ""
    pause_id: str = ""
    survey_start_id: str = ""
    survey_end_id: str = ""    
    introduction: IntroductionBlockModel = IntroductionBlockModel()
    importance: ImportanceBlockModel = ImportanceBlockModel()
    quiz: QuizBlockModel = QuizBlockModel()
    tips: TipsBlockModel = TipsBlockModel()
    comic: ComicBlockModel = ComicBlockModel()
    home_activity: HomeActivityBlockModel = HomeActivityBlockModel()
    video: VideoBlockModel = VideoBlockModel()
    audio: AudioBlockModel = AudioBlockModel()
    congratulations: CongratulationsBlockModel = CongratulationsBlockModel()
    opt_video: OptVideoBlockModel = OptVideoBlockModel()
    audio_tip: AudioTipBlockModel = AudioTipBlockModel()
    attached_single_doc: str = ""