from datetime import datetime
from pytz import timezone


format = "%Y-%m-%d %H:%M:%S"

# Получаем время UTC +0
now_utc = datetime.now(timezone('UTC'))


# Convert to Asia/Vladivostok time zone
now_asia = now_utc.astimezone(timezone('Asia/Vladivostok'))

print("Владивосток:")
print(now_asia.strftime(format))

print("Москва: ")
moscow = now_utc.astimezone(timezone('Europe/Moscow'))
print(moscow.strftime(format))


# Написать функцию, которая принимает часовой пояс, например 'Asia/Vladivostok'

# и возвращает время и дату в нужном формате (%Y-%m-%d %H:%M:%S)


