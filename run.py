# phase 2

# import sys

# from bot.config import load_settings
# from bot.exceptions import ConfigurationError


# def main() -> None:
#     """
#     Application entry point.
#     """

#     try:
#         print("Starting Trading Bot...")

#         settings = load_settings()

#         print(f"Environment: {settings.environment}")
#         print(f"Base URL: {settings.base_url}")

#         print("Configuration loaded successfully.")

#     except ConfigurationError as error:
#         print(f"ERROR: {error}")

#         sys.exit(1)


# if __name__ == "__main__":
#     main()







# phase 3

import sys
import logging

from bot.config import load_settings
from bot.exceptions import ConfigurationError
from bot.logging_config import setup_logging


logger = logging.getLogger("run")


def main() -> None:
    """
    Application entry point.
    """

    try:
        # =========================
        # Setup Logging
        # =========================

        setup_logging()

        logger.info("Application starting...")

        # =========================
        # Load Settings
        # =========================

        settings = load_settings()

        logger.info(
            "Configuration loaded successfully."
        )

        logger.info(
            f"Environment: {settings.environment}"
        )

        logger.info(
            f"Base URL: {settings.base_url}"
        )

        logger.info(
            "Trading bot startup completed successfully."
        )

    except ConfigurationError as error:
        logger.error(
            f"Configuration error during startup: {error}"
        )

        sys.exit(1)

    except Exception:
        logger.exception(
            "Unexpected application error occurred."
        )

        sys.exit(1)


if __name__ == "__main__":
    main()