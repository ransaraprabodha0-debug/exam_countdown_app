from datetime import datetime
import webbrowser

from kivy.app import App
from kivy.clock import Clock
from kivy.properties import StringProperty, ListProperty

EXAM_DATE = datetime(2025, 11, 9, 0, 0, 0)  # local time

class CountdownApp(App):
    days_text = StringProperty("")
    time_text = StringProperty("")
    days_color = ListProperty([1, 0, 0, 1])  # red RGBA

    def on_start(self):
        self._event = Clock.schedule_interval(self.update_countdown, 1)
        self.update_countdown(0)

    def update_countdown(self, _dt):
        now = datetime.now()
        time_left = EXAM_DATE - now

        if time_left.total_seconds() > 0:
            days = time_left.days
            hours, remainder = divmod(time_left.seconds, 3600)
            minutes, seconds = divmod(remainder, 60)

            self.days_text = f"{days} Days"
            self.time_text = f"{hours:02d}h : {minutes:02d}m : {seconds:02d}s"
            self.days_color = [0.55, 0, 0, 1] if days < 10 else [1, 0, 0, 1]
        else:
            self.days_text = "🎉 Exam Day!"
            self.time_text = "Good Luck 🍀"
            if hasattr(self, "_event"):
                self._event.cancel()

    def open_truecoder(self):
        webbrowser.open("https://www.youtube.com/@truecoder_RP")

if __name__ == "__main__":
    CountdownApp().run()
