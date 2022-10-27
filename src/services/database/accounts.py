from src.database.models import Accounts
from src.services.database import session


def get_accounts() -> list[Accounts]:
    """
        Get all saved account
    :return:
    """
    return session.query(Accounts).all()
