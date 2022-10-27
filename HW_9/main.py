from bot_commands import *

app = ApplicationBuilder().token("***").build()

app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("sub", sub_command))
app.add_handler(CommandHandler("div", div_command))
app.add_handler(CommandHandler("mult", mult_command))

app.run_polling()