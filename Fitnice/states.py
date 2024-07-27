from aiogram.fsm.state import StatesGroup, State


class FitnesState(StatesGroup):
    main_page = State()
    male_female = State()
    month = State()
    weekdays_1 = State()
    weekdays_2 = State()
    weekdays_3 = State()
    weekdays_4 = State()