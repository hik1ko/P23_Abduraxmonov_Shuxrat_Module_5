from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from aiogram import html, Router
from sqlalchemy import select, insert
from sqlalchemy.orm import Session

from Fitnice.buttons import main_page_button, male_female_btn, months_btn, week_days_btn
from Fitnice.db.models import User
from Fitnice.for_bs4 import beautiful_soup
from Fitnice.states import FitnesState

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message, state: FSMContext, session: Session) -> None:
    is_exists = session.execute(select(User).where(User.user_id == message.from_user.id)).scalar()
    if not is_exists:
        user = {
            "user_id": message.from_user.id,
            "username": message.from_user.username,
            "full_name": message.from_user.full_name
        }
        session.execute(insert(User).values(**user))
        session.commit()
    await state.set_state(FitnesState.main_page)
    await message.answer_photo(photo='https://telegra.ph/file/ed4fe2cb2b9fcb52ae435.png',
                               caption="""Assalamu alaykum! 
Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi""", reply_markup=main_page_button())


@main_router.message(FitnesState.main_page)
async def main_page_handler(message: Message, state: FSMContext, session: Session) -> None:
    if message.text == 'NewsPost 📄':
        soup = beautiful_soup('https://www.fitnessblender.com/')
        rows = soup.find_all('div', {"class": 'title-card-group'})
        for row in rows:
            await message.answer(row.text)
    elif message.text == 'Filial 📍':
        await message.answer_location(latitude=41.3048225634428, longitude=69.25289279629752)
    elif message.text == 'Admin 👨🏻‍💻':
        await message.answer("https://t.me/Absaitov_Dilshod")
    elif message.text == 'Start ✅':
        await state.set_state(FitnesState.male_female)
        await message.answer("Iltimos, quyidagilardan birini tanlang!", reply_markup=male_female_btn())


@main_router.message(FitnesState.male_female)
async def main_page_handler(message: Message, state: FSMContext, session: Session) -> None:
    if message.text == 'Back 🔙':
        await state.set_state(FitnesState.main_page)
        await message.answer_photo(photo='https://telegra.ph/file/ed4fe2cb2b9fcb52ae435.png',
                                   caption="""Assalamu alaykum! 
        Bu bo'timiz sizga kunlik qiladigan 🏋️ mashqlarni ko'rsatib beradi""", reply_markup=main_page_button())
    elif message.text == 'Man 🧑🏻‍💼':
        await state.set_state(FitnesState.month)
        await message.answer("Iltimos, oy raqamini tanlang!", reply_markup=months_btn())
    elif message.text == 'Woman 🤵‍♀️':
        await message.answer("Womanga vaqt yetmadi")


@main_router.message(FitnesState.month)
async def main_page_handler(message: Message, state: FSMContext, session: Session) -> None:
    if message.text == 'Back 🔙':
        await state.set_state(FitnesState.male_female)
        await message.answer("Iltimos, quyidagilardan birini tanlang!", reply_markup=male_female_btn())
    elif message.text == '1-oy':
        await state.set_state(FitnesState.weekdays_1)
        await message.answer("Iltimos, hafta kunini tanlang!", reply_markup=week_days_btn())
    elif message.text == '2-oy':
        await state.set_state(FitnesState.weekdays_2)
        await message.answer("Iltimos, hafta kunini tanlang!", reply_markup=week_days_btn())
    elif message.text == '3-oy':
        await state.set_state(FitnesState.weekdays_3)
        await message.answer("Iltimos, hafta kunini tanlang!", reply_markup=week_days_btn())
    elif message.text == '4-oy':
        await state.set_state(FitnesState.weekdays_4)
        await message.answer("Iltimos, hafta kunini tanlang!", reply_markup=week_days_btn())
