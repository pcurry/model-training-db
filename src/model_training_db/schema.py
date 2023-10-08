

from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, ForeignKey, Mapped, mapped_column, relationship

# class User(Base):
#     __tablename__ = "user_account"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     name: Mapped[str] = mapped_column(String(30))
#     fullname: Mapped[Optional[str]]
#     addresses: Mapped[List["Address"]] = relationship(back_populates="user")
#     def __repr__(self) -> str:
#         return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

# class Address(Base):
#     __tablename__ = "address"
#     id: Mapped[int] = mapped_column(primary_key=True)
#     email_address: Mapped[str]
#     user_id = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped[User] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# declarative base class
class Base(DeclarativeBase):
    pass


class Railroad(Base):
    __tablename__ = "railroad"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    abbreviation: Mapped[str]


class Manufacturer(Base):
    __tablename__ = "manufacturer"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    products: Mapped[list["Product"]] = relationship(back_populates="manufacturer")


class Scale(Base):
    __tablename__ = "scale"
    name: Mapped[str] = mapped_column(String(2), primary_key=True)


class Product(Base):
    __tablename__ = "product"

    id: Mapped[int] = mapped_column(primay_key=True)
    manufacturer_id = mapped_column(ForeignKey("manufacturer.id"))
    manufacturer: Mapped[Manufacturer] = relationship(back_populates="products")

    # Has a Manufacturer
    # Has an Item_Number
    # (Manufacturer, Item_Number) should be unique but I'm not sure yet
    #
    # Might have a Gauge


class TrainSet(Base):
    __tablename__ = "trainset"

    # Is a product
    # Has zero to many of
    #  - engines
    #  - cars
    #  - track sections
    #  - power supplies
    #  - controllers


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
    pass



