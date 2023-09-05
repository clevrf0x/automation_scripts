# Work timer is a small script for reminding to take a break after X number of minutes of coding by
# leveraging notification daemon provided by the operating system.

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


def main() -> None:
    try:
        session_time: int = get_session_time()
        print(f"Program will notify after {session_time} minutes. Do not close the terminal")
        session_time_in_seconds: int = session_time * 60
        sleep(session_time_in_seconds)  # sleep until session is over
        notification.notify(
            app_name="Work Timer", title="Work Timer",
            message=f"You have been working {session_time} Minutes, Take a break",
            timeout=10
        )
        print("Notified user successfully")
except KeyboardInterrupt:
        print("Program terminated by user")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == '__main__':
    main()
