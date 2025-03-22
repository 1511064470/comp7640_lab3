import telegram
from telegram.ext import Updater, MessageHandler, Filters
import configparser
import logging


def main():
    # 加载配置文件
    config = configparser.ConfigParser()
    config.read('config.ini')

    # 获取访问令牌
    token = config['TELEGRAM']['ACCESS_TOKEN']

    # 创建 Updater 和 Dispatcher
    updater = Updater(token=token, use_context=True)
    dispatcher = updater.dispatcher

    # 设置日志记录
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    # 注册消息处理程序
    echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
    dispatcher.add_handler(echo_handler)

    # 启动机器人
    updater.start_polling()
    updater.idle()


def echo(update, context):
    # 回显消息
    reply_message = update.message.text.upper()
    logging.info("Update: " + str(update))
    logging.info("Context: " + str(context))
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply_message)


if __name__ == '__main__':
    main()