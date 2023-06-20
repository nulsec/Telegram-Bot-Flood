import requests
import time
import random


chatid = "5620684141"
bot_token = "bot6071249463:AAGxUzAK5sR3nqhN0MYj0astREDdcR42uD0"
url = " https://api.telegram.org/" + bot_token + "/sendMessage?parse_code=markdown&chat_id=" + chatid

while True:
    random_number_11 = str(random.randint(10**10, (10**11)-1))
    random_number_4 = str(random.randint(10**3, (10**4)-1))

    message = "Pesan masuk. Dari: " + random_number_11 + ", Pesan: token code: " + random_number_4
    params = {
        "text": message
    }

    response = requests.get(url, params=params)
    print(response.content)

#    time.sleep(1)  # Tunggu 1 detik sebelum mengirim permintaan lagi