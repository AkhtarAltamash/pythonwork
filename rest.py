from plyer import notification
import time

if __name__ == '__main__':
    while True:
        notification.notify(
            title="****** Take Some Rest *********",
            message="the remainder. You bring these bags in, and I'll bring the rest",
            app_icon="D:/python work/sleep_rest.ico",
            timeout=5
        )
        time.sleep(10)
