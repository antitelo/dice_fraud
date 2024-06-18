import asyncio
import os

from aiogram import Bot, Dispatcher, F
from aiogram.enums import DiceEmoji
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv("API_TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "сколько ты хочешь чтобы выпало на кубике?"
    )


@dp.message(F.text)
async def dice(message: Message):
    if message.text in ["1", "2", "3", "4", "5", "6"]:
        ans = await message.answer_dice(DiceEmoji.DICE)
        dice_value = ans.dice.value
        print(dice_value)
        while str(dice_value) != message.text:
            # await ans.delete()
            # you can't delete a dice message that's not older than 1d
            ans = await message.answer_dice(DiceEmoji.DICE)
            dice_value = ans.dice.value
            print(dice_value)
    else:
        await message.answer("такого неь на кубике 😑")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
