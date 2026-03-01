from dataclasses import dataclass

@dataclass
class Post:
    title : str
    content : str
    category_id : str
    id: int | None = None
