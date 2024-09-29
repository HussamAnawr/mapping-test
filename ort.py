from sqlalchemy import Column, Integer, String, create_engine, or_, and_, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f"<User(id={self.id}, name={self.name}, fullname={self.fullname}, nickname={self.nickname})>"

class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    
    user = relationship(User, back_populates='addresess')
    def __repr__(self):
        return "<Address(email_address='%s')>" % self.email_address
    
User.addresess = relationship(Address, back_populates='user')

user = User(name="Hussam", fullname="Hussam Ghunaim", nickname="hos")
print(user)

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

# SessinFactory()
Base.metadata.create_all(bind=engine)
with Session() as session:
    session.add(user)
    
    session.add_all([
        User(name='wendy', fullname='Wendy Williams', nickname='windy'),
        User(name='mary', fullname='Mary Contrary', nickname='mary'),
        User(name='fred', fullname='Fred Flintstone', nickname='freddy')
    ])
    session.commit()
    r = session.query(User.name).order_by(User.fullname).all()
    for row in session.query(User).filter(and_(~User.name.in_(['Hussam', 'mary']), User.nickname.like('%fr%'))):
        print(row.addresess)
    print(r)
