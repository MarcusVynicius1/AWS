from pydantic import BaseModel

class LivroBase(BaseModel):
    titulo: str
    autor: str
    ano: int

class LivroCreate(LivroBase):
    pass

class LivroResponse(LivroBase):
    id: int

    class Config:
        from_attributes = True
