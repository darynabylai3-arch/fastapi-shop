import re
from sqlalchemy import Column , Integer , String 
from sqlalchemy.orm import relationship 
from ..database import Base 

class Category(Base):
    _tablename_ = 'categories'

    id = Column(Integer,primaty_key = True,index = True)
    name = Column(String,unique = True ,nullable = False,index = True)
    slug = Column(String,unique = True ,nullable = False,index = True)

    products = relationship("Product",back_populates='category')

    def __repr__(self):
        return f"<Category(id={self.id}, name = '{self.name}')"