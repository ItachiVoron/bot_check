import logging
from aiogram import Bot, Dispatcher
import config

# Configure logging
logging.basicConfig(level=logging.INFO)

# prerequisites
if not config.Token:
    exit("No token provided")

# init
bot = Bot(token=config.Token, parse_mode="HTML")
dp = Dispatcher(bot)