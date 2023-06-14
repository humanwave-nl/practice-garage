from google.cloud import ndb
from shared.system.base.model import BaseModel


class Car(BaseModel):
    """The Car model"""

    name = ndb.StringProperty()
    license_plate = ndb.StringProperty(required=True)

    brand = ndb.StringProperty()
    color = ndb.StringProperty()

    note = ndb.TextProperty(indexed=False)

    @classmethod
    def list(cls, garage, brand=None, limit=20):
        with cls.ndb_context():
            query = Car.query(ancestor=garage.key)
            if brand:
                query = query.filter(Car.brand == brand)
            if limit:
                return query.fetch(limit)
            return query.fetch()
