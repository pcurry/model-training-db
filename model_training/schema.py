import sqlalchemy as sa

from sqlalchemy.orm import DeclarativeBase

# declarative base class
class Base(DeclarativeBase):
    pass


class Railroad(Base):
    __tablename__ = "railroad"

    

class Manufacturer(Base):
    __tablename__ = "manufacturer"


class Gauge(Base):
    __tablename__ = "track_gauge"
    

class Product(Base):
    # Has a Manufacturer
    # Has an Item_Number
    # (Manufacturer, Item_Number) should be unique but I'm not sure yet
    # Might have a Gauge
    
    pass
    
class TrainSet(Base):
    # Is a product
    # Has zero to many of
    #  - engines
    #  - cars
    #  - track sections
    #  - power supplies
    #  - controllers
    pass

class TrackSection(Base):
    # has a gauge
    # is a type of track
    pass


class TrackInventory(Base):
    # Has a tracksection ID, foreign key to TrackSection
    # has a count of how many of those sections are currently present
    pass


class Layout(Base):
    """The thing with all the track where the model trains actually roll around.
    """


class LayoutInventory(Base):
    # possibly how we indicate which items are part of which layout?
    
    
    
                 
