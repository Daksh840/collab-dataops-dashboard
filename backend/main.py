from fastapi import FastAPI, Depends
from typing import List
from sqlmodel import Field, SQLModel, create_engine, Session, select
from pydantic import BaseModel
from database import create_db_and_tables, get_session

app = FastAPI()

# SQLModel ORM class (database table)
class Pipeline(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    status: str
    last_updated: str

# Pydantic input model (client sends this JSON)
class PipelineCreate(BaseModel):
    name: str
    status: str
    last_updated: str

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/pipelines", response_model=List[Pipeline])
def get_pipelines(session: Session = Depends(get_session)):
    return session.exec(select(Pipeline)).all()

@app.post("/pipelines", response_model=Pipeline)
def create_pipeline(pipeline_data: PipelineCreate, session: Session = Depends(get_session)):
    new_pipeline = Pipeline(**pipeline_data.dict())
    session.add(new_pipeline)
    session.commit()
    session.refresh(new_pipeline)
    return new_pipeline

@app.put("/pipelines/{pipeline_id}", response_model=Pipeline)
def update_pipeline(pipeline_id: int, updated_data: PipelineCreate, session: Session = Depends(get_session)):
    pipeline = session.get(Pipeline, pipeline_id)
    if not pipeline:
        return {"error": "Pipeline not found"}

    pipeline.name = updated_data.name
    pipeline.status = updated_data.status
    pipeline.last_updated = updated_data.last_updated

    session.add(pipeline)
    session.commit()
    session.refresh(pipeline)

    return pipeline

@app.delete("/pipelines/{pipeline_id}")
def delete_pipeline(pipeline_id: int, session: Session = Depends(get_session)):
    pipeline = session.get(Pipeline, pipeline_id)
    if not pipeline:
        return {"error": "Pipeline not found"}
    
    session.delete(pipeline)
    session.commit()
    return {"message": f"Pipeline with ID {pipeline_id} deleted"}
