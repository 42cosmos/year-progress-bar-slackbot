from datetime import date
from slack_messanger import SlackMessenger


def progress_bar(progress, total, length=24):
    filled_length = int(length * progress // total)
    bar = '█' * filled_length + '#' * (length - filled_length)
    percent = progress / total * 100

    return f'Progress: |{bar}| {percent:.1f}% Complete'


if __name__ == "__main__":
    slack = SlackMessenger(test=False)
    today = date.today()
    current_year = today.year

    start_date = date(current_year, 1, 1)

    delta = today - start_date
    days = delta.days
    progress = (days / 365) * 100

    message = progress_bar(progress, 100)

    slack.send_msg(message)
