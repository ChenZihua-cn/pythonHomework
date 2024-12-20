import numpy as np
import matplotlib.pyplot as plt

# 参数设置
L = 1.0  # 绳子长度，单位m
m = 1.0  # 小球质量，单位kg
g = 9.8  # 重力加速度，单位m/s²
omega_drive = 0.05 * np.pi  # 驱动力频率，单位rad/s
amplitude = 0.1  # 驱动力幅值，单位m
time_step = 0.001  # 时间步长，单位s
total_time = 10.0  # 总时间，单位s
num_steps = int(total_time / time_step)  # 总时间步数

# 初始条件
theta = np.pi / 4  # 初始角度，单位rad
omega = 0.0  # 初始角速度，单位rad/s
theta_list = []  # 记录角度
omega_list = []  # 记录角速度
t_list = []  # 记录时间
x_list = []  # 记录x坐标
y_list = []  # 记录y坐标

# 时间循环
for i in range(num_steps):
    t = i * time_step
    drive_force = amplitude * np.cos(omega_drive * t)  # 正弦驱动力对系统的贡献

    # 动力学方程（刚体绳子）
    alpha = -(g / L) * np.sin(theta) + (drive_force / L) * np.cos(theta)  # 角加速度
    omega += alpha * time_step  # 更新角速度
    theta += omega * time_step  # 更新角度

    # 记录数据
    x = L * np.sin(theta)
    y = -L * np.cos(theta)
    theta_list.append(theta)
    omega_list.append(omega)
    x_list.append(x)
    y_list.append(y)
    t_list.append(t)

# 绘制结果
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# 图1: 半径和角度变化
axs[0].plot(t_list, theta_list, label=r"$\theta$ (Angle)")
axs[0].set_xlabel("Time (s)")
axs[0].set_ylabel("Angle (rad)")
axs[0].legend()
axs[0].grid()

# 图2: 笛卡尔坐标轨迹
axs[1].plot(x_list, y_list, label="Trajectory")
axs[1].set_xlabel("X (m)")
axs[1].set_ylabel("Y (m)")
axs[1].legend()
axs[1].grid()

# 图3: 频谱分析
from scipy.fftpack import fft
freqs = np.fft.fftfreq(len(theta_list), time_step)
fft_vals = fft(theta_list)
positive_freqs = freqs[freqs > 0]
positive_amplitudes = 2 * np.abs(fft_vals[freqs > 0]) / len(theta_list)

axs[2].plot(positive_freqs, positive_amplitudes, label="Frequency Spectrum")
axs[2].set_xlabel("Frequency (Hz)")
axs[2].set_ylabel("Amplitude")
axs[2].legend()
axs[2].grid()

plt.tight_layout()
plt.show()
