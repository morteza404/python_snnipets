from typing import List

from fastapi import APIRouter, Depends
from pydantic import UUID4
from sqlalchemy.orm import Session
from config.database import get_db
from schemas.region_schema import RegionOutput, RegionInput
from service.region_service import RegionService


router = APIRouter(
    prefix="/location/region",
    tags=["location"]
)


@router.post("", status_code=201, response_model=RegionOutput)
def create_region(
        data: RegionInput,
        session: Session = Depends(get_db),
):
    _service = RegionService(session)
    return _service.create(data)


@router.get("", status_code=200, response_model=List[RegionOutput])
def get_regions(session: Session = Depends(get_db)) -> List[RegionOutput]:
    _service = RegionService(session)
    return _service.get_all()


@router.delete("/{_id}", status_code=204)
def delete_region(
        _id: UUID4,
        session: Session = Depends(get_db),
):
    _service = RegionService(session)
    return _service.delete(_id)


@router.put("/{_id}", status_code=200, response_model=RegionInput)
def update_region(
        _id: UUID4,
        data: RegionInput,
        session: Session = Depends(get_db),
):
    _service = RegionService(session)
    return _service.update(_id, data)