# reminder is a small script for reminding a specific message from user after an user 
# specified time intervel by utilizing current operating systems notification daemon.

from plyer import notification
from time import sleep


def get_session_time() -> int:
    while True:
        try:
            session_time: int = int(input("Enter session time in minutes: "))
            if session_time <= 0:
                print("You cannot provide a negative number, please input valid number")
            else:
                return session_time
        except ValueError:
            print("Invalid input, please provide a valid number")


def get_message() -> str:
    while True:
        message: str = input("Enter the message to remind: ").strip()
        if not message or message == '':
            print("No message were given, please try again")
        else:
            return message


def main() -> None:
    try:
        session_time: int = get_session_time()
        message: str = get_message()
        print(f"Program will notify after {session_time} minutes. Do not close the terminal")
        session_time_in_seconds: int = session_time * 60
        sleep(session_time_in_seconds)  # sleep until session is over
        notification.notify(
            title="Reminder",
            message=message,
            timeout=10
        )
        print("Notified user successfully")
    except KeyboardInterrupt:
        print("Program terminated by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
