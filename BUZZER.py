from machine import Pin, PWM
from utime import sleep

# Khởi tạo chân GPIO 27 để điều khiển buzzer với PWM
buzzer = PWM(Pin(27))

# Đặt tần số cho buzzer (ví dụ: 1000 Hz)
buzzer.freq(1000)

def beep(duration=0.5):
    buzzer.duty_u16(32768)  # Điều chỉnh độ rộng xung (âm thanh phát ra)
    sleep(duration)         # Kêu trong thời gian xác định
    buzzer.duty_u16(0)      # Tắt âm thanh
    sleep(duration)         # Ngừng kêu trong khoảng thời gian xác định

# Tạo âm thanh 5 lần
for i in range(5):
    beep(0.5)  # Kêu 0.5 giây, sau đó ngừng 0.5 giây


