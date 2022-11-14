# 1)Создайте программу при помощи виртуального окружения и PIP( можно любую задачу, главное файл с библиотекой чтобы был в формате тхт).
# 2)Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор( можно добавить работу с рациональными и комплексными числами), организовать меню, добавив в неё систему логирования

from bot_commands import *

app = ApplicationBuilder().token("***").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("mult", mult_command))

app.run_polling()