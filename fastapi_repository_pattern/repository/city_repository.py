from typing import List, Optional, Type

from models.city import City
from pydantic import UUID4
from schemas.city_schema import CityInput, CityOutput, CityInDb
from schemas.region_schema import RegionOutput
from sqlalchemy.orm import Session


class CityRepository:
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: CityInput) -> CityInDb:
        city = City(**data.model_dump(exclude_none=True))
        self.session.add(city)
        self.session.commit()
        self.session.refresh(city)
        return CityInDb(**city.__dict__)

    def get_all(self) -> List[Optional[CityOutput]]:
        cities = self.session.query(City).all()
        return self._map_city_to_schema_list(cities)

    def get_all_by_region(self, region_id: UUID4) -> List[Optional[CityOutput]]:
        cities = self.session.query(City).filter_by(region_id=region_id).all()
        return self._map_city_to_schema_list(cities)

    def get_by_id(self, _id: UUID4) -> Type[City]:
        return self.session.query(City).filter_by(id=_id).first()

    def city_exists_by_name(self, name: str) -> bool:
        city = self.session.query(City).filter_by(name=name).first()
        return bool(city)

    def city_exists_by_id(self, _id: UUID4) -> bool:
        city = self.session.query(City).filter_by(id=_id).first()
        return bool(city)

    def update(self, city: Type[City], data: CityInput) -> CityInput:
        for key, value in data.model_dump(exclude_none=True).items():
            setattr(city, key, value)
        self.session.commit()
        self.session.refresh(city)
        return CityInput(**city.__dict__)

    def delete(self, city: Type[City]) -> bool:
        self.session.delete(city)
        self.session.commit()
        return True
        
    @staticmethod
    def _map_city_to_schema_list(cities: List[Type[City]]) -> List[CityOutput]:
        return [
            CityOutput(
                id=city.id,
                name=city.name,
                region=RegionOutput(
                    id=city.region.id, name=city.region.name
                )
            )
            for city in cities
        ]