# Keras Notify Callback

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![PyPI version](https://badge.fury.io/py/keras-notify.svg)](https://badge.fury.io/py/keras-notify)


A Tensorflow/Keras callback which sends information about your model training, on various messaging platforms.

## Installation

Using `pip`:

```bash
pip install keras-notify
```

## Usage

Import the required module and add it to the list callbacks while training your model.

**Example:**

```python
>>> from keras-notify import TelegramCallback
>>> telegram_callback = TelegramCallback('<BotToken>',
                                         '<ChatID>',
	                                 'CNN Model',
	                                 ['loss', 'val_loss'],
	                                 ['accuracy', 'val_accuracy'],
	                                 True)
>>> model.fit(x_train, y_train,
              batch_size=32,
              epochs=10,
              validation_data=(x_test, y_test),
              callbacks=[telegram_callback])
```

### Telegram

1. Create a telegram bot using BotFather
	* Search for @BotFather on telegram.
	* Send `/help` to get list of all commands.
	* Send `/newbot` to create a new bot and complete the setup.
	* Copy the **bot token** after creating the bot.
2. Get the **chat ID**
	* Search for the bot you created and send it any random message.
	* Go to this URL `https://api.telegram.org/bot<BOT_TOKEN>/getUpdates` (replace <BOT_TOKEN> with your bot token)
	* Copy the `chat id` of the user you want to send messages to.
	* You receive the `chat id` only if you send the message first and then go to the above url.
3. Use the `TelegramCallback()` class.

```python
TelegramCallback(bot_token=None, chat_id=None, modelName='model', loss_metrics=['loss'], acc_metrics=[], getSummary=False):
```

**Arguments:**

* `bot_token` : unique token of Telegram bot `{str}`
* `chat_id` : Telegram chat id you want to send message to `{str}`
* `modelName` : name of your model `{str}`
* `loss_metrics` : loss metrics you want in the loss graph `{list of strings}`
* `acc_metrics` : accuracy metrics you want in the accuracy graphs `{list of strings}`
* `getSummary` : Do you want message for each epoch (False) or a single message containing information about all epochs (True). `{bool}`

### Slack

1. Create a Slack workspace
2. Create a new channel
3. Search for the **Incoming Webhooks** in the Apps and install it.
4. Copy the **Webhook URL**
5. Use the `SlackCallback()` class.

```python
SlackCallback(bot_token=None, chat_id=None, modelName='model', loss_metrics=['loss'], acc_metrics=[], getSummary=False):
```

**Arguments:**

* `webhookURL` : unique webhook URL of the app `{str}`
* `channel` :  channel name or username you want to send message to `{str}`
* `modelName` : name of your model `{str}`
* `loss_metrics` : loss metrics you want in the loss graph `{list of strings}`
* `acc_metrics` : accuracy metrics you want in the accuracy graph `{list of strings}`
* `getSummary` : Do you want message for each epoch (False) or a single message containing information about all epochs (True). `{bool}`

*Sending images in Slack is not supported currently.*

## ToDo

* WhatsApp
* E-Mail
* Zulip
* Messages

