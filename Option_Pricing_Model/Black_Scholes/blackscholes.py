import numpy as np
from scipy.stats import norm

def black_scholes(S, K, T, r, sigma, option_type="call"):
    """
    Tính giá quyền chọn theo mô hình Black-Scholes.
    
    Parameters:
        S (float): Giá hiện tại của tài sản cơ sở
        K (float): Giá thực hiện
        T (float): Thời gian đến đáo hạn (tính bằng năm)
        r (float): Lãi suất phi rủi ro (dạng thập phân, ví dụ: 0.05 cho 5%)
        sigma (float): Độ biến động (dạng thập phân, ví dụ: 0.2 cho 20%)
        option_type (str): Loại quyền chọn, "call" cho quyền chọn mua, "put" cho quyền chọn bán
    
    Returns:
        float: Giá quyền chọn
    """
    # Tính d1 và d2
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    
    if option_type == "call":
        # Công thức cho quyền chọn mua
        price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == "put":
        # Công thức cho quyền chọn bán
        price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    else:
        raise ValueError("Loại quyền chọn phải là 'call' hoặc 'put'")
    
    return price

# Ví dụ sử dụng:
S = 100  # Giá tài sản cơ sở
K = 105  # Giá thực hiện
T = 1    # Thời gian đến đáo hạn (1 năm)
r = 0.05  # Lãi suất phi rủi ro (5%)
sigma = 0.2  # Độ biến động (20%)

# Tính giá quyền chọn mua và quyền chọn bán
call_price = black_scholes(S, K, T, r, sigma, option_type="call")
put_price = black_scholes(S, K, T, r, sigma, option_type="put")

print(f"Call option price: {call_price:.2f}")
print(f"Put option price: {put_price:.2f}")