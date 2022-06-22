from email.policy import default
from unicodedata import category
from uuid import uuid4
from sqlalchemy import JSON, Column, Float, Integer
from sqlalchemy import Text
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import func


from config import postgres_conection

Base = postgres_conection.declarative_base()


class BaseModel(Base):
    __abstract__ = True

    active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    deleted_at = Column(DateTime(timezone=True), onupdate=func.now())


def generate_uuid():
    return str(uuid4())


class Profile(BaseModel):
    """."""

    __tablename__ = 'profile'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text, default=None)

    user_profile = relationship(
        'UserProfile', backref='profile', order_by="UserProfile.id")

    def __repr__(self):
        return "<Profile(id='%s', name='%s')>" % (
            self.id, self.name)


class UserProfile(BaseModel):
    """."""

    __tablename__ = 'user_profile'

    id = Column(Integer, primary_key=True)

    profile_id = Column(ForeignKey("profile.id"))
    user_id = Column(ForeignKey("user.id"))

    def __repr__(self):
        return "<UserProfile(id='%s')>" % (self.id)


class User(BaseModel):
    """."""

    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    first_name = Column(Text)
    last_name = Column(Text)
    nid = Column(Text)

    address = Column(Text)

    phone = Column(Text)
    email = Column(Text)

    user_profile = relationship('UserProfile', backref='user', order_by="UserProfile.id")
    products = relationship('Product', backref='user', order_by="Product.id")

    @property
    def list_profile(self):
        return [value.profile.name for value in self.user_profile]

    def __repr__(self):
        return "<User(id='%s', email='%s',nid='%s')>" % (
            self.id, self.email, self.nid)


class Product(BaseModel):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    quantity = Column(Integer, default=0)
    sku = Column(Text, nullable=False)
    brand = Column(Text, nullable=False)
    initial_value = Column(Float, default=0)
    description = Column(Text, default=None)
    profit_percentage = Column(Text, default=None)
    extra_data = Column(Text, nullable=False)
    history_query = Column(Integer, default=0)

    user_id = Column(ForeignKey("user.id"))
    category_id = Column(ForeignKey("category_product.id"))

    def __repr__(self):
        return "<Product(id='%s', name='%s',sku='%s',brand='%s')>" % (
            self.id, self.name, self.sku, self.brand)

    @property
    def category_name(self):
        return self.category.name


class CategoryProduct(BaseModel):

    __tablename__ = 'category_product'

    id = Column(Integer, primary_key=True)
    name = Column(Text)
    description = Column(Text, default=None)

    category = relationship('Product', backref='category', order_by="Product.id")

    def __repr__(self):
        return "<CategoryProduct(id='%s', name='%s')>" % (
            self.id, self.name)
