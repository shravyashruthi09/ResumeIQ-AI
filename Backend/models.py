from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from database import Base


# -------------------------
# Users Table
# -------------------------
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)


# -------------------------
# Resume Table
# -------------------------
class Resume(Base):
    __tablename__ = "resumes"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))

    filename = Column(String)

    resume_text = Column(Text)

    # NEW
    job_description = Column(Text)


# -------------------------
# Analysis Table
# -------------------------
class Analysis(Base):
    __tablename__ = "analysis"

    id = Column(Integer, primary_key=True, index=True)

    resume_id = Column(Integer, ForeignKey("resumes.id"))

    ats_score = Column(Float)

    missing_skills = Column(Text)

    improved_resume = Column(Text)

    feedback = Column(Text)