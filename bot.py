
from telegram import Update, ForceReply
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# 🎲 Initialize the SlotMachine class from slot.py
from slot import SlotMachine

slot_machine = SlotMachine()

def start(update: Update, _: CallbackContext) -> None:
    """👋 Send a welcome message and help text."""
    user = update.effective_user
    update.message.reply_text(f"Hi {user.first_name} 🎉, welcome to the Slot Casino! 🎰\n"
                              "Type /play 🔄 to spin the slot machine.\n"
                              "Type /credits 💰 to check your available credits.")

def play(update: Update, _: CallbackContext) -> None:
    """🎮 Simulate spinning the slot machine."""
    if not slot_machine.check_credit():
        update.message.reply_text("🚫 Sorry, you don't have enough credits to play.")
        return
    
    # 💸 Deduct the cash for this round
    slot_machine.credit -= slot_machine.cash
    
    # 🔄 Spin the slot machine
    wheel1, wheel2, wheel3 = slot_machine.spin()
    
    # 🎁 Calculate the reward
    reward = slot_machine.get_reward(wheel1, wheel2, wheel3)
    slot_machine.total_won += reward
    slot_machine.credit += reward
    
    update.message.reply_text(f"🎰 Result: {wheel1} {wheel2} {wheel3}\n"
                              f"🎉 Reward: {reward}\n"
                              f"💰 Total Credits: {slot_machine.credit}")

def credits(update: Update, _: CallbackContext) -> None:
    """💰 Check the available credits."""
    update.message.reply_text(f"💰 Total Credits: {slot_machine.credit}")

# 🤖 Initialize the Updater with the placeholder token
updater = Updater("6318638354:AAEv7LV_f46tAcVxj92LXjrPEKFX7s74Mhk", use_context=True)

# 📥 Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# 🛠 Register the command handlers
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("play", play))
dispatcher.add_handler(CommandHandler("credits", credits))

# 🏃‍♀️ Run the Bot until the user presses Ctrl-C
updater.start_polling()
updater.idle()
