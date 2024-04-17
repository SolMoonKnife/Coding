import tkinter as tk
from tkinter import messagebox
import time


def rgb_to_hex(R, G, B) -> str:
    return '#{0:02x}{1:02x}{2:02x}'.format(R, G, B)

MYPINK = rgb_to_hex(255, 123, 166)
MYBLUE = rgb_to_hex(153, 217, 234)

class PomodoroTimer:
    def __init__(self, master):
        self.master = master
        self.master.title("Pomodoro 타이머")

        self.master.configure(bg="white")

        self.work_time = tk.IntVar(value=25)  # 작업 시간을 나타내는 변수, 기본값은 25분
        self.rest_time = tk.IntVar(value=5)   # 휴식 시간을 나타내는 변수, 기본값은 5분

        self.minutes = self.work_time.get()
        self.seconds = 0
        self.state = "working"
        self.setworktime = self.work_time.get()
        self.setresttime = self.rest_time.get()

        self.label = tk.Label(master, text=self.format_time(), font=("Helvetica", 48), bg="white")
        self.label.grid(row=0, column=0, columnspan=4, padx=100, pady=40)


        self.work_label = tk.Label(master, text="작업 (분):", justify="center", bg="white")
        self.work_label.grid(row=1, column=0, padx=5, pady=10, sticky="e")

        self.work_slider = tk.Scale(master, from_=1, to=60, orient="horizontal", variable=self.work_time, state="normal", bg='white')
        self.work_slider.grid(row=1, column=1, columnspan=2, padx=5, pady=10, sticky="we")

        self.rest_label = tk.Label(master, text="휴식 (분):", justify="center", bg="white")
        self.rest_label.grid(row=2, column=0, padx=5, pady=10, sticky="e")

        self.rest_slider = tk.Scale(master, from_=1, to=60, orient="horizontal", variable=self.rest_time, state="normal", bg='white')
        self.rest_slider.grid(row=2, column=1, columnspan=2, padx=5, pady=10, sticky="we")

        self.start_button = tk.Button(master, text="시작", command=self.start_timer)
        self.start_button.grid(row=3, column=1, padx=10, pady=10)

        self.stop_button = tk.Button(master, text="정지", command=self.stop_timer, state="disabled")
        self.stop_button.grid(row=3, column=2, padx=10, pady=10)

    def start_timer(self):
        if self.state == "paused_w":
            self.master.configure(bg=MYPINK)
            self.label.configure(bg=MYPINK)
            self.work_label.configure(bg=MYPINK)
            self.rest_label.configure(bg=MYPINK)
            if self.setworktime != self.work_time.get():
                self.setworktime = self.work_time.get()
                self.minutes = self.work_time.get()
                self.seconds = 0
            self.state = "working"
        elif self.state == "paused_r":
            self.master.configure(bg=MYBLUE)
            self.label.configure(bg=MYBLUE)
            self.work_label.configure(bg=MYBLUE)
            self.rest_label.configure(bg=MYBLUE)
            if self.setresttime != self.rest_time.get():
                self.setresttime = self.rest_time.get()
                self.minutes = self.rest_time.get()
                self.seconds = 0
            self.state = "in_rest"
        else:
            self.minutes = self.work_time.get()
            self.master.configure(bg=MYPINK)
            self.label.configure(bg=MYPINK)
            self.work_label.configure(bg=MYPINK)
            self.rest_label.configure(bg=MYPINK)
            self.state = "working"
        self.work_slider.config(state="disabled", bg='grey')
        self.rest_slider.config(state="disabled", bg='grey')
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        self.run_timer()

    def stop_timer(self):
        self.master.configure(bg="white")
        self.label.configure(bg="white")
        self.work_label.configure(bg="white")
        self.rest_label.configure(bg="white")
        if self.state == "working":
            self.state = "paused_w"
        elif self.state == "in_rest":
            self.state = "paused_r"
        self.work_slider.config(state="normal", bg='white')
        self.rest_slider.config(state="normal", bg='white')
        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")

    def run_timer(self):
        while self.state == "working" or self.state == "in_rest":
            self.label.config(text=self.format_time())
            self.master.update()
            time.sleep(1)
            if self.minutes == 0 and self.seconds == 0:
                if self.state == "working":
                    # messagebox.showinfo("완료", "작업 시간이 끝났습니다. 휴식 시간으로 전환합니다.")
                    self.minutes = self.rest_time.get()
                    self.master.configure(bg=MYBLUE)
                    self.label.configure(bg=MYBLUE)
                    self.work_label.configure(bg=MYBLUE)
                    self.rest_label.configure(bg=MYBLUE)
                    self.setresttime = self.rest_time.get()
                    self.state = "in_rest"
                elif self.state == "in_rest":
                    # messagebox.showinfo("완료", "휴식 시간이 끝났습니다. 작업 시간으로 전환합니다.")
                    self.minutes = self.work_time.get()
                    self.master.configure(bg=MYPINK)
                    self.label.configure(bg=MYPINK)
                    self.work_label.configure(bg=MYPINK)
                    self.rest_label.configure(bg=MYPINK)
                    self.setworktime = self.work_time.get()
                    self.state = "working"
            else:
                self.decrement_time()

    def decrement_time(self):
        if self.seconds == 0:
            self.minutes -= 1
            self.seconds = 59
        else:
            self.seconds -= 1

    def format_time(self):
        return f"{self.minutes:02d}:{self.seconds:02d}"


def main():
    root = tk.Tk()
    app = PomodoroTimer(root)
    root.mainloop()


if __name__ == "__main__":
    main()
