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

# 









# phase 7

import sys
import logging

from cli import main as cli_main

from bot.config import load_settings
from bot.exceptions import ConfigurationError
from bot.logging_config import setup_logging


def main() -> None:
    """
    Application bootstrap entry point.
    """

    try:
        # =========================
        # Setup Logging
        # =========================

        setup_logging()

        logger = logging.getLogger("run")

        logger.info("Application starting...")

        # =========================
        # Load Configuration
        # =========================

        settings = load_settings()

        logger.info(
            "Configuration loaded successfully."
        )

        logger.info(
            "Environment: %s",
            settings.environment,
        )

        logger.info(
            "Base URL: %s",
            settings.base_url,
        )

        # =========================
        # Launch CLI
        # =========================

        cli_main()

    except ConfigurationError as error:
        logging.getLogger("run").error(
            "Configuration error during startup: %s",
            error,
        )

        sys.exit(1)

    except Exception:
        logging.getLogger("run").exception(
            "Unexpected application startup error."
        )

        sys.exit(2)


if __name__ == "__main__":
    main()