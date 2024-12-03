import numpy as np
import matplotlib.pyplot as plt

# 参数定义
m1, m2 = 1.0, 1.0  # 两球质量
k = 1000.0  # 绳子的弹性系数
L0 = 1.0  # 绳子的自然长度
mu = 0.1  # 绳子的线密度
dt = 0.001  # 时间步长
T = 100.0  # 模拟时间

# 初始条件
x1, x2 = -0.5, 0.5  # 两球的初始位置
v1, v2 = 0.0, 0.0  # 初始速度
N = int(T / dt)  # 时间步数

# 数据存储
x1_arr, x2_arr = [x1], [x2]

# 数值模拟
for _ in range(N):
    # 计算两段的拉力
    L = abs(x2 - x1)  # 当前绳子长度
    T1 = k * max(0, L - L0) * (x2 - x1) / L  # 球1到球2的拉力
    T2 = k * max(0, L - L0) * (x1 - x2) / L  # 球2到球1的拉力（对称）

    # 更新位置和速度
    a1 = T1 / m1  # 球1的加速度
    a2 = T2 / m2  # 球2的加速度
    v1 += a1 * dt
    v2 += a2 * dt
    x1 += v1 * dt
    x2 += v2 * dt

    # 记录数据
    x1_arr.append(x1)
    x2_arr.append(x2)

# 绘图
plt.plot(np.linspace(0, T, len(x1_arr)), x1_arr, label="Ball 1")
plt.plot(np.linspace(0, T, len(x2_arr)), x2_arr, label="Ball 2")
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.legend()
plt.show()
