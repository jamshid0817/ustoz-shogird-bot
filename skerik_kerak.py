from aiogram import types, Bot, executor, Dispatcher
from aiogram.dispatcher.filters import Text
from config import TOKEN
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
TOKEN = "6620061783:AAFCM8r_PXzBGnaZJbu-DTd6pwSlnW6SoN0"

storage = MemoryStorage()

bot = Bot(token=TOKEN)


dp = Dispatcher(bot=bot, storage=storage)



class SherikkerakState(StatesGroup):
    ism_familya = State() 
    texnologiya = State()
    telefon_raqam= State()
    hudud = State()
    narxi = State()
    kasbi = State()
    murojaat_qilish_vaqti = State()
    maqsad = State()


async def on_startup(_):
    print("Bot muvaffaqiyatli ishga tushurildi")


reply_buttons = ReplyKeyboardMarkup(resize_keyboard=True)
knop1 = KeyboardButton(text="Sherik kerak")




@dp.message_handler(commands=['start'])
async def start_func(message: types.Message):
    user = types.User.get_current()
    await message.answer(text=f"<b>Assalom aleykum {user['first_name']}\nUstozShogird kanaliga xush kelibsiz</b>,\n\n/help yordam buyrug'i orqali nimalarga qodirligimni bilib oling!", reply_markup=reply_buttons, parse_mode="HTML")
   


@dp.message_handler(Text(equals="Sherik kerak"))
async def Sherik_kerak(message: types.Message):
    await message.answer(text=f"<b>Sherik topish uchun ariza berish</b> \n\nHozir sizga bir nechta savollar beriladi.\nHar biriga javob bering\nOxirida hammasi to'g'ri bo'lsa, HA tugmasini bosing va arizangiz Adminga yuboriladi.\n\n<b>Ism, familiyangizni kiriting?<b>", parse_mode="HTML")
    await SherikkerakState.ism_familya.set()



dp.message_handler(state=SherikkerakState.ism_familya)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(ism_familya=message.text)
    await message.answer(text="Texnologiya kiriting?")
    await SherikkerakState.next()

dp.message_handler(state=SherikkerakState.texnologiya)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(texnologiya=message.text)
    await message.answer(text="telefon_raqam kiriting?")
    await SherikkerakState.next()

dp.message_handler(state=SherikkerakState.telefon_raqam)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(telefon_raqam=message.text)
    await message.answer(text="hudud kiriting?")
    await SherikkerakState.next()

dp.message_handler(state=SherikkerakState.hudud)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(hudud=message.text)
    await message.answer(text="Narxni kiriting?")
    await SherikkerakState.next() 

dp.message_handler(state=SherikkerakState.narx)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(narx=message.text)
    await message.answer(text="kasbni  kiriting?")
    await SherikkerakState.next()

dp.message_handler(state=SherikkerakState.kasbi)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(kasbi=message.text)
    await message.answer(text="murojaat qilish vaqtini kiriting?")
    await SherikkerakState.next()

dp.message_handler(state=SherikkerakState.murojaat_qilish_vaqti)
async def set_name(message:types.Message,state:FSMContext):
    await state.update_data(murojaat_qilish_vaqti=message.text)
    data = await state.get_data()
    text = f"""<b>Sherik kerak:</b>\n\n 🏅 Sherik: {data["ism_familya"]}\n 📚 Texnologiya: {data["texnologiya"]}\n 🇺🇿 Telegram: {data["telegram"]}\n 📞 Aloqa:  {data["telefon_raqam"]}\n
      🌐 Hudud: {data["hudud"]}\n 💰 Narxi: {data["narxi"]}\n
      👨🏻‍💻 Kasbi: {data["kasbi"]}\n 
    🕰 Murojaat qilish vaqti: {data["murojaat_qilish_vaqti"]}\n 
    🔎 Maqsad: {data["maqsad"]}]\n 
    """
    await message.answer(text="")


def start_keyboard() -> types.ReplyKeyboardMarkup:
    """Create reply keyboard with main menu."""
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(
        types.KeyboardButton("First Button "),
    )
    return keyboard




if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True,on_startup=on_startup)