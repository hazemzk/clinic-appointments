from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    age = Column(Integer)
    phone = Column(String)

    appointments = relationship("Appointment", back_populates="patient")  # مريض له مواعيد

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    date_time = Column(DateTime, nullable=False)
    reason = Column(String)
    patient_id = Column(Integer, ForeignKey("patients.id"))  # ربط بالمريض

    patient = relationship("Patient", back_populates="appointments")  # ميعاد مرتبط بمريض
