from types import NoneType


class Creature:
    name = None
    inventory = "ei mitään"

    def joop(self, jotain)


koira = Creature()
koira.name = "Musti"
kissa = 123
messages = {
    "joohjuuh": "Koira oli {actor.name} ja kissoja {kissa}. Taskussa {actor.name}lla oli {actor.inventory}."
}


def joohjuuh(actor, kissa):
    karhu = 456
    print(messages["joohjuuh"].format(**locals()))
    print(str.format(messages["joohjuuh"], **locals()))





joohjuuh(koira, kissa)

