# -*- coding:utf-8 -*-
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ParseMode, MessageEntity, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

token = Updater(
    '5702618547:AAFsBZZTGLM3Yf-utpXIgHh9FMAtueZZ0PY', use_context=True)


send_index = 0
re = 0
block = []


def start(update, context):
    botton_call_back = [[InlineKeyboardButton(
        'ارتباط با ما 📞', callback_data='1')], ]
    reply_markup = InlineKeyboardMarkup(botton_call_back)

    if update.message.chat_id != 81335179:
        context.bot.send_message(chat_id=update.message.chat_id, text='سلام {} به ربات چت من خوش آمدید.'.format(
            update.message.from_user.first_name), reply_markup=reply_markup)
    else:
        context.bot.send_message(
            chat_id=update.message.chat_id, text='تو که ادمینی ما رو ایسگا کردی ؟')


def send(update, context):
    global send_index, re, sender, block

    botton_answer = [[InlineKeyboardButton(
        'پاسخ 🗣', callback_data='2'), InlineKeyboardButton('بلاک 🚫', callback_data='4')], [InlineKeyboardButton('آنبلاک کردن ✅', callback_data="5")]]
    replay_markup_answer = InlineKeyboardMarkup(botton_answer)

    botton_send_message = [
        [InlineKeyboardButton('ارسال پیام', callback_data='3')]]
    replay_markup_send_message = InlineKeyboardMarkup(botton_send_message)

    if send_index != 0:
        if update.message.chat_id not in block:
            context.bot.send_message(
                chat_id=81335179, text=update.message.text, reply_markup=replay_markup_answer)
            sender = update.message.chat_id
            context.bot.send_message(
                chat_id=81335179, text="این پیام از طرف https://t.me/{} میباشد.".format(update.message.from_user.username))
            context.bot.send_message(
                chat_id=update.message.chat_id, text="پیام شما ارسال گردید.")
            send_index = 0
        else:
            context.bot.send_message(
                chat_id=update.message.chat_id, text="شما بلاک شده اید.")

    if re != 0:
        context.bot.send_message(
            chat_id=sender, text="پاسخ ادمین به شما : \n {}".format(update.message.text))
        context.bot.send_message(
            chat_id=81335179, text="پاسختان ارسال شد.".format(update.message.text), reply_markup=replay_markup_send_message)
        re = 0


def contact_bottons(update, context):
    global send_index, re, block, sender
    query = update.callback_query

    if query.data == '1':
        send_index = 1
        context.bot.send_message(
            chat_id=query.message.chat_id, text="پیام خود را وارد کنید.")

    if query.data == '2':
        context.bot.send_message(
            chat_id=81335179, text="پاسخ خود را وارد کنید.")
        re = 1

    if query.data == '3':
        context.bot.send_message(
            chat_id=81335179, text="پیام خود را بنویسید")

    if query.data == '4':
        block.append(sender)
        context.bot.send_message(
            chat_id=81335179, text='کاربر مورد نظر با چت آیدی {} بلاک شد.'.format(sender))

    if query.data == '5':
        if sender in block:
            block.remove(sender)
            context.bot.send_message(
                chat_id=81335179, text='کاربر مورد نظر با چت آیدی {} آنبلاک شد.'.format(sender))
        else:
            context.bot.send_message(
                chat_id=81335179, text='کاربر مورد نظر بلاک نبوده است.')


token.dispatcher.add_handler(CommandHandler('start', start))
token.dispatcher.add_handler(MessageHandler(Filters.text, send))
token.dispatcher.add_handler(CallbackQueryHandler(contact_bottons))

token.start_polling()
token.idle()
