from sqlalchemy import Column, ForeignKey, Integer, String, Double

from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Test(Base):
    __tablename__ = "test"

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    heartRate = Column(Double, nullable=False)
    activeEnergyBurned = Column(Double, nullable=False)
    distanceWalkingRunning = Column(Double, nullable=False)

    @property
    def serialize(self):
        return {
            'name': self.name,
            'heartRate': self.heartRate,
            'energy': self.activeEnergyBurned,
            'distance': self.distanceWalkingRunning
        }

