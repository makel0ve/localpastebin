from datetime import datetime

from sqlalchemy import MetaData, Table, Column, Integer, String, TIMESTAMP, Unicode


metadata = MetaData()


link = Table(
    "link",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("url", Unicode, index=True, unique=True, nullable=False),
    Column("hashid", String, index=True, unique=True, nullable=False),
    Column("start_life", TIMESTAMP, default=datetime.utcnow),
    Column("end_life", TIMESTAMP, default=datetime.utcnow)
)