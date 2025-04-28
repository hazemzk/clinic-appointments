from pydantic import BaseModel
from datetime import datetime

# ====== مرضى ======
class PatientBase(BaseModel):
    name: str
    age: int
    phone: str

class PatientCreate(PatientBase):
    pass

class Patient(PatientBase):
    id: int

    class Config:
        orm_mode = True

# ====== مواعيد ======
class AppointmentBase(BaseModel):
    date_time: datetime
    reason: str
    patient_id: int

class AppointmentCreate(AppointmentBase):
    pass

class Appointment(AppointmentBase):
    id: int

    class Config:
        orm_mode = True
