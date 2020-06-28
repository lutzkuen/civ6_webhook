"""
Open limit orders in Oanda Account

"""

from .main import run_service


def test_run_service(): # pylint: disable=unused-argument
    """
    Test entrypoint for cloud function execution

    Parameters
    ----------
    arg1
    arg2

    Returns
    -------

    """
    run_service('test arg', 'test arg')

