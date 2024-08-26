from typing import Optional

from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List, Optional

class DocumentMetaData(BaseModel):
    Publisher: str
    Contact_Name: Optional[str] = None
    Contact_Email: Optional[str] = None
    Bureau_Code: str
    Program_Code: str
    Public_Access_Level: str
    Geographic_Coverage: str
    Temporal_Applicability: str
    Theme: str
    Language: str
    Homepage: Optional[str] = None
    Issued: str
    References: Optional[List[str]] = None
    Unique_Identifier: str
    Last_Update: str
