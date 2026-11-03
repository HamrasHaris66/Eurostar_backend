import logging
import sys

logger = logging.getLogger("eurostar_app")


def setup_logging() -> None:
    if logger.handlers:
        return
    logger.propagate = False
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(
        logging.Formatter("%(asctime)s | %(levelname)s | %(name)s | %(message)s")
    )
    logger.addHandler(handler)