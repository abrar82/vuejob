from typing import Optional
from pydantic import BaseModel



class JobBase(BaseModel):
    job_name:  Optional[str] = None
    description:  Optional[str] = None
    role:  Optional[str] = None



class JobAdd(JobBase):
    job_id: str
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    # streaming_platform: Optional[str] = None
    # membership_required: bool
    #  job_name: Optional[str] = None
    # description: Optional[str] = None
    # role: Optional[str] = None
    experience: Optional[str] = None
    qualification: Optional[str] = None
    job_location: Optional[str] = None
    salary: Optional[str] = None
    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True

class ApplicationBase(BaseModel):
    job_id:str
    application_id:str


class JobApply(ApplicationBase):
    
    job_name:Optional[str] = None
    
    applicant_id:Optional[str] = None
    applicant_name:Optional[str] = None
    applicant_phone:Optional[str] = None
    applicant_email:Optional[str] = None
    applied_time:Optional[str] = None

    class Config:
        orm_mode = True



class Application(JobApply):
    id:int
    class Config:
        orm_mode = True


class Job(JobAdd):
    id: int

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True


class UpdateJob(BaseModel):
    # Optional[str] is just a shorthand or alias for Union[str, None].
    # It exists mostly as a convenience to help function signatures look a little cleaner.
    # job_name: Optional[str] = None
    # description: Optional[str] = None
    # role: Optional[str] = None
    experience: Optional[str] = None
    qualification: Optional[str] = None
    job_location: Optional[str] = None
    salary: Optional[str] = None

    # Behaviour of pydantic can be controlled via the Config class on a model
    # to support models that map to ORM objects. Config property orm_mode must be set to True
    class Config:
        orm_mode = True
