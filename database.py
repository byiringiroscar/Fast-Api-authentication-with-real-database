import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

# Create a declarative base class
DATABASE_URL = "sqlite:///./database.db"

# Create a declarative base class
engine = _sql.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Base = _declarative.declarative_base()

# Create a session class
SessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)



