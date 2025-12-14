from piccolo.table import Table
from piccolo.columns  import Varchar,Text, Float, Integer,Timestamptz ,Decimal
from datetime import datetime

class Course(Table):
    name = Varchar(length=200)
    description = Text()
    instructor = Varchar(length=100)
    rating = Float(default=0.0)
    #task 3 price data types changes Integer to Decimal
    price = Decimal()
    created_on = Timestamptz(default=datetime.utcnow())
    
