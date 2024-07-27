import asyncio
import logging
import sys
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from aiogram.fsm.context import FSMContext

from aiogram import Bot, Dispatcher, html, Router, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message

from buttons import email_btn

async def mail_sender(receiver: str, text: str):
    sender_email = "shuhratabduraxmonov08@gmail.com"
    receiver_email = "shuhratabduraxmonov08@gmail.com"
    password = "cwuizmdpacctxffm"
    message = MIMEMultipart("alternative")
    message["Subject"] = "Module_5 exam"
    message["From"] = sender_email
    message["To"] = receiver
    html = f"""
    <html>
      <body>
        <h1>{text}<br>
        <h1>
      </body>
    </html>
    """
    part2 = MIMEText(html, "html")
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


TOKEN = "7037879367:AAG0ISCCehaD3XKZT8K6Ka7D0Rk-w14gS_0"
bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

main_router = Router()


class EmailState(StatesGroup):
    email = State()
    receiver = State()
    text = State()

rcv_address = ''

@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=email_btn())


@main_router.callback_query(F.data == 'email')
async def mail_receiver (message: Message, state: FSMContext):
    await state.set_state(EmailState.email)
    await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
    await bot.send_message(chat_id=message.from_user.id, text="send me a mail address that you want to send")


@main_router.message(EmailState.email, F.text)
async def receiver_email(message: Message, state: FSMContext):
    await state.set_state(EmailState.receiver)
    rcv_address = message.text
    await state.set_data(data={'email': message.text})
    await bot.send_chat_action(chat_id=message.from_user.id, action="typing")
    await bot.send_message(chat_id=message.from_user.id, text="Good, now send me a text that you want to send")


@main_router.message(EmailState.receiver, F.text)
async def text_message(message: Message, state: FSMContext):
    await state.set_data(data={'text': message.text})
    data = await state.get_data()
    mail = data.get('email')
    txt = data.get('text')
    txt_mail = message.text
    await mail_sender(rcv_address, txt_mail)
    await message.answer('mail sent successfully')
    await state.clear()
    if message.text == ".":
        await message.chat.pin_message(message_id=message.reply_to_message.message_id)
    else:
        await message.chat.pin_message(message.message_id, disable_notification=True)




async def main() -> None:
    dp = Dispatcher()
    dp.include_router(main_router)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())