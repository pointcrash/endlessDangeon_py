from .character_abs import Character
from .mixins.user_relation import UserRelationMixin


class PlayerCharacter(Character, UserRelationMixin):
    _user_id_unique = True
    _user_back_populates = "character"
