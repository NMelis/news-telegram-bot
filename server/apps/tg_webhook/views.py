from rest_framework.views import APIView


class TelegramSetWebHook(APIView):
    def get(self):
        bot.remove_webhook()
        sleep(1)
        try:
            return str(bot.set_webhook(
                '{}{}'.format(os.getenv('WEBHOOK_TELEGRAM'),
                              os.getenv('TELEGRAM_BOT_TOKEN')))), 200
        except telebot.apihelper.ApiException:
            pass
        return '', 200
