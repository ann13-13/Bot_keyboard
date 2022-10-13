from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage


API_TOKEN = '5716740580:AAF8NGJT0O893WivrHYR5j4dfLLZm5OgizU'

bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

if __name__ == '__main__':
    from handler import dp, send_to_admin
    executor.start_polling(dp, on_startup=send_to_admin)



