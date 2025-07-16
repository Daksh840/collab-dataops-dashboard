from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel
from typing import List
from datetime import datetime
from sqlalchemy import Column, String
from database import create_db_and_tables, get_session
from typing import Optional
from sqlalchemy import Column, String
from sqlmodel import SQLModel, Field

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# SQLModel ORM class (DB model)
class Pipeline(SQLModel, table=True):
    __tablename__ = "pipeline"
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    status: str
    last_updated: datetime  # ✅ use datetime, not string
    color: Optional[str] = Field(default=None, sa_column=Column(String))

# Pydantic input model
class PipelineCreate(BaseModel):
    name: str
    status: str
    last_updated: datetime  # ✅ parse ISO timestamp from frontend

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

# Get all pipelines
@app.get("/pipelines", response_model=List[Pipeline])
def get_pipelines(session: Session = Depends(get_session)):
    return session.exec(select(Pipeline)).all()

# Create a new pipeline
@app.post("/pipelines", response_model=Pipeline)
def create_pipeline(pipeline_data: PipelineCreate, session: Session = Depends(get_session)):
    new_pipeline = Pipeline(**pipeline_data.dict())
    session.add(new_pipeline)
    session.commit()
    session.refresh(new_pipeline)
    return new_pipeline

# Update existing pipeline
@app.put("/pipelines/{pipeline_id}", response_model=Pipeline)
def update_pipeline(pipeline_id: int, updated_data: PipelineCreate, session: Session = Depends(get_session)):
    pipeline = session.get(Pipeline, pipeline_id)
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")

    pipeline.name = updated_data.name
    pipeline.status = updated_data.status
    pipeline.last_updated = updated_data.last_updated

    session.add(pipeline)
    session.commit()
    session.refresh(pipeline)
    return pipeline

# Delete pipeline
@app.delete("/pipelines/{pipeline_id}")
def delete_pipeline(pipeline_id: int, session: Session = Depends(get_session)):
    pipeline = session.get(Pipeline, pipeline_id)
    if not pipeline:
        raise HTTPException(status_code=404, detail="Pipeline not found")

    session.delete(pipeline)
    session.commit()
    return {"message": f"Pipeline with ID {pipeline_id} deleted"}
