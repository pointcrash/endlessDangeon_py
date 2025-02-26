from core.models.abs.character import Character


class Enemy(Character):
    __tablename__ = "enemies"

    _location_id_nullable: bool = True
    _location_back_populates = "enemies"
