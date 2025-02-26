from core.models.abs.character import Character


class NPC(Character):
    _location_id_nullable: bool = True
    _location_back_populates = "npcs"
