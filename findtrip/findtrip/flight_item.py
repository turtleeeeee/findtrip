from sqlalchemy import create_engine, Column, String, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class FlightItem(Base):
    __tablename__ = 'flights'

    id = Column(Integer, primary_key=True, autoincrement=True)
    site = Column(String(50))
    plane_info = Column(String)
    departure_time = Column(String(100))
    departure_airport = Column(String(100))
    arrive_time = Column(String(100))
    arrive_airport = Column(String(100))
    price = Column(String(100))
    cabin_class = Column(String(50))
    transfer_duration = Column(String(50))

# 创建数据库引擎
engine = create_engine('sqlite:///flights.db')  # 示例使用 SQLite，实际应用中可根据需要更改
Base.metadata.create_all(engine)

# 创建数据库会话
Session = sessionmaker(bind=engine)
