def send_email(message: str, recipient: str, sender = "university.help@gmail.com"):
    if "@" not in sender or not sender.endswith((".com", ".ru", ".net")):
        print(f"Невозможно вывести письмо с адреса {sender} на адрес {recipient} ")
    elif "@" not in recipient or not recipient.endswith((".com", ".ru", ".net")):
        print(f"Невозможно вывести письмо с адреса {sender} на адрес {recipient} ")
    elif sender == recipient:
        print(f"Нельзя отправить письмо самому себе!")
    elif sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ: Письмо отправлено с адреса {sender} на адрес {recipient}")


def main():
    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')


if __name__ == '__main__':
    main()