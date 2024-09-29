from sqlalchemy import Column, Integer, String, create_engine, or_, and_, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
import os

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_str = 'sqlite:///'+os.path.join(BASE_DIR, 'site.db')

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    addresses = relationship('Address',back_populates='user')

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship('User', back_populates='addresses')
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
    
user = User(name="Hussam", fullname="Hussam Ghunaim", nickname="hos")
print(user)

engine = create_engine(connection_str, echo=True)
Session = sessionmaker(bind=engine)

# SessinFactory()
if not os.path.exists('site.db'):
    Base.metadata.create_all(bind=engine)
with Session() as session:
    user.addresses =[
        Address(email_address="o.hussam@gmail.com", ),
        Address(email_address="o.hussam@fg.gov.sa", ),
    ]
    session.add(user)
    
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')
    ])
    session.commit()
    r = session.query(User.name).order_by(User.fullname).all()
    for row in session.query(User).filter(and_(~User.name.in_(['Hussam', 'mary']), User.nickname.like('%fr%'))):
        print(row.addresses)
    print(session.query(User).where(User.name == "Hussam").one().addresses)
    session.commit()
    print(r)

# if os.path.exists('site.db'):
#     os.remove('site.db')