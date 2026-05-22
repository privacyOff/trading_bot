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









# phase 7

# import sys
# import logging

# from cli import main as cli_main

# from bot.config import load_settings
# from bot.exceptions import ConfigurationError
# from bot.logging_config import setup_logging
# from bot.client import BinanceFuturesClient
# from decimal import Decimal
# from bot.models import OrderRequest


# def main() -> None:
#     """
#     Application bootstrap entry point.
#     """

#     try:
#         # =========================
#         # Setup Logging
#         # =========================

#         setup_logging()

#         logger = logging.getLogger("run")

#         logger.info("Application starting...")

#         # =========================
#         # Load Configuration
#         # =========================

#         settings = load_settings()

#         logger.info(
#             "Configuration loaded successfully."
#         )

#         logger.info(
#             "Environment: %s",
#             settings.environment,
#         )

#         logger.info(
#             "Base URL: %s",
#             settings.base_url,
#         )

#         # =========================
#         # Initialize Binance Client
#         # =========================

#         client = BinanceFuturesClient(
#             settings
#         )

#         # =========================
#         # Connectivity Test
#         # =========================

#         client.ping()

#         # =========================
#         # Authentication Test
#         # =========================

#         client.test_authentication()

#         # =========================
#         # Payload Builder Tests
#         # =========================

#         from decimal import Decimal

#         from bot.models import OrderRequest

#         # ---------------------------------
#         # MARKET Payload Test
#         # ---------------------------------

#         market_order = OrderRequest(
#             symbol="BTCUSDT",
#             side="BUY",
#             order_type="MARKET",
#             quantity=Decimal("0.001"),
#         )

#         market_payload = (
#             client._build_payload(
#                 market_order
#             )
#         )

#         logger.info(
#             "MARKET payload: %s",
#             market_payload,
#         )

#         # ---------------------------------
#         # LIMIT Payload Test
#         # ---------------------------------

#         limit_order = OrderRequest(
#             symbol="BTCUSDT",
#             side="BUY",
#             order_type="LIMIT",
#             quantity=Decimal("0.001"),
#             price=Decimal("75000"),
#         )

#         limit_payload = (
#             client._build_payload(
#                 limit_order
#             )
#         )

#         logger.info(
#             "LIMIT payload: %s",
#             limit_payload,
#         )

#         # =========================
#         # MARKET Order Test
#         # =========================

#         logger.info(
#             "Submitting test MARKET order."
#         )

#         response = client.create_order(
#             market_order
#         )

#         logger.info(
#             "Order response: %s",
#             response,
#         )

#         # =========================
#         # LIMIT Order Test
#         # =========================

#         logger.info(
#             "Submitting test LIMIT order."
#         )

#         limit_response = client.create_order(
#             limit_order
#         )

#         logger.info(
#             "LIMIT order response: %s",
#             limit_response,
#         )

#         # =========================
#         # Launch CLI
#         # =========================

#         # cli_main()

#     except ConfigurationError as error:
#         logging.getLogger("run").error(
#             "Configuration error during startup: %s",
#             error,
#         )

#         sys.exit(1)

#     except Exception:
#         logging.getLogger("run").exception(
#             "Unexpected application startup error."
#         )

#         sys.exit(2)


# if __name__ == "__main__":
#     main()








# phase 8

import logging
import sys

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

        logger.info(
            "Application starting..."
        )

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