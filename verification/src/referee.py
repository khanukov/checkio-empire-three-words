from checkio_referee import RefereeBase

from checkio_referee import covercodes, representations


import settings_env
from tests import TESTS


class Referee(RefereeBase):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "three_words"
    FUNCTION_NAMES = {
        "javascript": "threeWords"
    }
    CALLED_REPRESENTATIONS = {
        "python_3": representations.unwrap_arg_representation,
        "javascript": representations.unwrap_arg_representation,
    }
