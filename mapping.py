from sqlalchemy import (
    create_engine, 
    Integer,
    String,
    Table, 
    Column,
    ForeignKey
)
from sqlalchemy.orm import relationship, registry, sessionmaker
from models import User, Car

engine = create_engine('sqlite:///:memory:', echo=True)

mapper_registry = registry()
metadata = mapper_registry.metadata

Session = sessionmaker(bind=engine)

users_table = Table('users', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(250)),
                    Column('email', String)
                    )

cars_table = Table('cars', metadata,
                   Column('id', Integer, primary_key=True),
                   Column('name', String(250)),
                   Column('user', Integer, ForeignKey('users.id'))
                   )


mapper_registry.map_imperatively(
    User, 
    users_table,
    properties={
        'things': relationship(
            Car,
        )
    }
)

mapper_registry.map_imperatively(Car, cars_table)

user = User('Hussam', 'o.hussam@gmail.com')
user.add_thing(Car(name="Ford"))

metadata.create_all(engine)

with Session() as session:
    session.add(user)
    session.add(User('amani', 'amani.aljaber@gmail.com',))
    session.commit()
    print(session.query(User).all())
    for user in session.query(User).all():
        print(f"id: {user.id}, name:{user.name}, email: {user.email}, things: {user.things}")


if __name__ == "__main__":
    pass

