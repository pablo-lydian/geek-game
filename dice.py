


class Dragon:

    @staticmethod
    def performs_action():
        return False

    @staticmethod
    def can_perform_action(game_state):
        return False

    @staticmethod
    def oposite():
        return SuperHero


class Heart:

    @staticmethod
    def performs_action():
        return True

    @staticmethod
    def can_perform_action(game_state):
        return True

    @staticmethod
    def index():
        return FortyTwo


class Rocket:

    @staticmethod
    def performs_action():
        return True

    @staticmethod
    def can_perform_action(game_state):
        return False

    @staticmethod
    def index():
        return Troll


class Troll:

    @staticmethod
    def performs_action():
        return True

    @staticmethod
    def can_perform_action(game_state):
        return False

    @staticmethod
    def index():
        return Rocket

\
class FortyTwo:

    @staticmethod
    def performs_action():
        return False

    @staticmethod
    def can_perform_action(game_state):
        return False

    @staticmethod
    def index():
        return Heart


class SuperHero:

    @staticmethod
    def performs_action():
        return True

    @staticmethod
    def can_perform_action(game_state):
        return False

    @staticmethod
    def index():
        return Troll

