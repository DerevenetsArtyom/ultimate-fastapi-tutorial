from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

connection_uri = settings.DATABASE_URI

# Heroku workaround: https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres
if connection_uri.startswith("postgres://"):
    connection_uri = connection_uri.replace("postgres://", "postgresql://", 1)
    engine = create_engine(connection_uri)

# For running PostgreSQL locally
elif connection_uri.startswith("postgresql://"):
    engine = create_engine(connection_uri)

# For running SQLite locally
else:
    engine = create_engine(
        connection_uri,
        # this config is necessary to work with SQLite - this is a common gotcha because FastAPI can access the database
        # with multiple threads during a single request, so SQLite needs to be configured to allow that.
        connect_args={"check_same_thread": False},
    )

# In the most general sense, the Session establishes all conversations with the database and
# represents a “holding zone” for all the objects which you’ve loaded or associated with it during its lifespan.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
