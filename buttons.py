from aiogram import types

welcome_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
button1 = types.KeyboardButton("Bizning Kurslarimiz")
button2 = types.KeyboardButton("Biz bilan aloqa")
welcome_keyboard.add(button1)
welcome_keyboard.add(button2)


our_courses = types.ReplyKeyboardMarkup(resize_keyboard=True)
course1 = types.KeyboardButton("Ingliz tili")
course2 = types.KeyboardButton("Rus tili")
course3 = types.KeyboardButton("Arab tili")
course4 = types.KeyboardButton("Koreys tili")
#our_course.add(course1)
our_courses.add(course1)
our_courses.add(course2)
our_courses.add(course3)
our_courses.add(course4)

register_to_course = types.InlineKeyboardMarkup(resize_keyboard=True)
reg_button = types.InlineKeyboardButton("Kursga ro'yxatdan o'tish",callback_data="register_course")
register_to_course.add(reg_button)

#######
contact_us = types.ReplyKeyboardMarkup(resize_keyboard=True)
contact_us1 = types.KeyboardButton("📞Telefon raqam kiritish")
contact_us2 = types.KeyboardButton("📨Email kiritish")

contact_us.add(contact_us1)
contact_us.add(contact_us2)

to_contact_us = types.InlineKeyboardMarkup(resize_keyboard=True)
button = types.InlineKeyboardButton("Biz bilan bog'lanish",callback_data="Contact_us")
to_contact_us.add(button)