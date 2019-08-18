from celery import shared_task


@shared_task
def tg_message(update):
    print('Privet 222')
    update.message.reply_text("Welcome to my awesome bot!")
