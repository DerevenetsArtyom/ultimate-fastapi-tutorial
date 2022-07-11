from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URI = "sqlite:///example.db"

engine = create_engine(
    DATABASE_URI,
    # this config is necessary to work with SQLite - this is a common gotcha because FastAPI can access the database
    # with multiple threads during a single request, so SQLite needs to be configured to allow that.
    connect_args={"check_same_thread": False},
)

# In the most general sense, the Session establishes all conversations with the database and
# represents a “holding zone” for all the objects which you’ve loaded or associated with it during its lifespan.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
