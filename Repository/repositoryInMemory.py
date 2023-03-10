from Domain.entity import Entity
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entities = {}

    def read(self, id_entity=None):
        if id_entity is None:
            return list(self.entities.values())

        if id_entity in self.entities:
            return self.entities[id_entity]
        else:
            return None

    def create(self, entity: Entity):
        if self.read(entity.id_entity) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entities[entity.id_entity] = entity

    def update(self, entity: Entity):
        if self.read(entity.id_entity) is None:
            raise KeyError("Nu exista o entitate cu id-ul dat!")
        self.entities[entity.id_entity] = entity

    def delete(self, id_entity):
        if self.read(id_entity) is None:
            raise KeyError("Nu exista o entitate cu id-ul dat!")
        del self.entities[id_entity]
