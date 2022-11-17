from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ParseMode, MessageEntity, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

token = Updater(
    '5702618547:AAFsBZZTGLM3Yf-utpXIgHh9FMAtueZZ0PY', use_context=True)


def start(update, context):
    inline_bottom_list = [[InlineKeyboardButton('ارتباط با ادمین', callback_data="1")], [
        InlineKeyboardButton('ارتباط با برنامه نویس', callback_data='2')]]
    inline_keyboard_markup = InlineKeyboardMarkup(inline_bottom_list)

    bottom_list: list = [['ارتباط با برنامه نویس'], ['ارتباط با ادمین']]
    reply_keyboard_markup = ReplyKeyboardMarkup(bottom_list)

    context.bot.send_message(text='سلام {} .به اولین ربات برنامه نویسی من خوش آمدید \n برای اطلاعات بیشتر روی /help کلیک کنید'.format(
        update.message.from_user.username), chat_id=update.message.chat_id, reply_markup=reply_keyboard_markup, )

    context.bot.send_message(chat_id=update.message.chat_id,
                             text=' id : {} \n user: @{} \n firstName: {} \n lastName: {}'.format(update.message.chat_id,
                                                                                                  update.message.from_user.username,
                                                                                                  update.message.from_user.first_name,
                                                                                                  update.message.from_user.last_name))

    context.bot.send_message(chat_id=update.message.chat_id,
                             text='یکی از گزینه ها را انتخاب کنید', reply_markup=inline_keyboard_markup)

    if update.message.chat_id != 81335179:
        context.bot.send_message(chat_id=81335179, text='کاربری با نام کاربری {} وارد ربات شد.'.format(
            update.message.from_user.first_name))


def touch(update, context):
    query = update.callback_query
    if query.data == "1":
        context.bot.send_message(chat_id = query.message.chat_id , text = '@Btsedamusiks')
    if query.data == '2':
        context.bot.send_message(chat_id = query.message.chat_id , text = '@Mohsen_ghaffariii')


def recive_message(update, context):

    if update.message.text == 'ارتباط با برنامه نویس':
        context.bot.send_message(
            chat_id=update.message.chat_id, text='@Mohsen_ghaffariii')
    elif update.message.text == 'ارتباط با ادمین':
        context.bot.send_message(
            chat_id=update.message.chat_id, text='@Btsedamusiks')


def help(update, context):
    context.bot.send_message(chat_id=update.message.chat_id,
                             text='برای دسترسی به پنل ادمین از دستور /admin استفاده کنید.')


def admin(update, context):
    if update.message.chat_id == 81335179:
        context.bot.send_message(chat_id=81335179, text='شما ادمین هستید')
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text='شما کاربر عادی هستید')


def antiLink(update, context):
    list = [MessageEntity.URL]
    if update.message.parse_entities(types=list) or update.message.caption_entities[0]['type'] == 'url':
        context.bot.delete_message(
            chat_id=update.message.chat_id, message_id=update.message.message_id)


# def antiLink_File(update, context):
#     if update.message.caption_entities[0]['type'] == 'url':
#         context.bot.delete_message(
#             chat_id=update.message.chat_id, message_id=update.message.message_id)


token.dispatcher.add_handler(CommandHandler('start', start))
token.dispatcher.add_handler(CommandHandler('help', help))
token.dispatcher.add_handler(CommandHandler('admin', admin))
# token.dispatcher.add_handler(MessageHandler(Filters.all, antiLink))
token.dispatcher.add_handler(MessageHandler(Filters.text, recive_message))
# token.dispatcher.add_handler(MessageHandler(Filters.all, antiLink_File))
token.dispatcher.add_handler(CallbackQueryHandler(touch))

token.start_polling()
token.idle()
