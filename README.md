# Option_Pricing_Models
Black-Scholes, Binomial and Monte Carlo simulation  
<br/>
Đây là kết quả của đề tài Đồ án 2 thực hiện tại Đại Học Bách Khoa Hà Nội năm học 2024-2025

## Black-Scholes Model
Công thức Black-Scholes (hay mô hình Black-Scholes-Merton) là một mô hình toán học dùng để định giá quyền chọn (options), được phát triển bởi Fischer Black, Myron Scholes và Robert Merton. Đây là một trong những mô hình cơ bản và phổ biến nhất trong tài chính.
<br/>
Dưới đây là cách giải thích công thức này, cùng với các thành phần chính của nó:
### 1. Công thức Black-Scholes
Giá của quyền chọn mua (call option) được tính theo công thức:
<br/><br/>
**C = S<sub>0</sub>.N(d<sub>1</sub>) - K.e<sup>-rT</sup>.N(d<sub>2</sub>)**
<br/><br/>
Giá của quyền chọn bán (put option) được tính theo công thức:
<br/><br/>
**P = K.e<sup>-rT</sup>.N(-d<sub>2</sub>) - S<sub>0</sub>.N(-d<sub>1</sub>)**
<br/><br/>
Với:
<br/><br/>
**d<sub>1</sub> = [ln(S<sub>0</sub>/K) + ln(r + σ<sup>2</sup>/2)T] / σ.sqrt(T)**
<br/>
**d<sub>2</sub> = d<sub>1</sub> - σ.sqrt(T)**
### 2. Ý nghĩa của các ký hiệu:
*C: Giá của quyền chọn mua (call option).<br/>*
*P: Giá của quyền chọn bán (put option).<br/>*
*S<sub>0</sub>: Giá hiện tại của tài sản cơ sở (underlying asset).<br/>*
*K: Giá thực hiện (strike price) của quyền chọn.<br/>*
*T: Thời gian còn lại đến ngày đáo hạn (maturity) tính bằng năm.<br/>*
*r: Lãi suất phi rủi ro liên tục (risk-free rate).<br/>*
*σ: Độ biến động (volatility) của giá tài sản cơ sở.<br/>*
*N(d): Hàm phân phối xác suất tích lũy chuẩn (cumulative normal distribution function), biểu thị xác suất mà biến ngẫu nhiên chuẩn hoá có giá trị nhỏ hơn hoặc bằng d.<br/>*
### 3. Kết quả:
Thuật toán mô hình Black-Scholes được cài đặt trong [file này](https://github.com/Haipham2002/Option_Pricing_Models/blob/main/Option_Pricing_Model/Black_Scholes/blackscholes.py)
<br/>
Ứng dụng đinh giá quyền chọn bằng mô hình Black-Scholes: [https://haipham-bsmmodel.streamlit.app/](https://haipham-bsmmodel.streamlit.app/)
<br/>
Ứng dụng vẽ mặt phẳng Implied Volatility (Bề mặt độ biến động): [https://haipham-volatility.streamlit.app/](https://haipham-volatility.streamlit.app/)
<br/>

## Binomial Option Pricing Model:
Mô hình định giá quyền chọn nhị thức (Binomial Option Pricing Model) là một phương pháp phổ biến để định giá các quyền chọn tài chính. Mô hình này được phát triển dựa trên việc mô phỏng các chuyển động giá của tài sản cơ sở theo từng bước thời gian và được sử dụng rộng rãi nhờ tính minh bạch, linh hoạt và dễ áp dụng.
<br/><br/>
Chi tiết về thuật toán được giải thích trong [báo cáo Đồ án 2](https://github.com/Haipham2002/Option_Pricing_Models/blob/main/Ph%E1%BA%A1m_L%C3%A2n_H%E1%BA%A3i_20203880_%C4%90A2.docx)
<br/>
Source code và các kết quả sau khi cài đặt thuật toán xem [tại đây](https://github.com/Haipham2002/Option_Pricing_Models/tree/main/Option_Pricing_Model/Binomial)

## Monte-Carlo Simulation:
Monte Carlo Simulation (Mô phỏng Monte Carlo) là một phương pháp toán học và thống kê sử dụng để mô phỏng và phân tích các hệ thống phức tạp hoặc các hiện tượng ngẫu nhiên. Nó được đặt theo tên của sòng bạc Monte Carlo ở Monaco, vì tính chất ngẫu nhiên của trò chơi may rủi tại đây phản ánh ý tưởng cốt lõi của phương pháp.
<br/><br/>
### 1. Mục đích của Monte Carlo Simulation
Monte Carlo Simulation giúp:
<br/>
- Dự đoán các kết quả có thể xảy ra của một quá trình ngẫu nhiên.<br/>
- Đánh giá rủi ro và sự không chắc chắn trong các mô hình dự đoán.<br/>
- Ra quyết định dựa trên các kịch bản và phân bố xác suất.<br/>
<br/>
Ví dụ, có thể dùng Monte Carlo Simulation để:
<br/>
- Dự báo giá cổ phiếu.<br/>
- Phân tích rủi ro tài chính.<br/>
- Đánh giá hiệu suất của hệ thống kỹ thuật (như sản xuất hoặc giao thông).<br/>
<br/>

### 2. Nguyên lý cơ bản
- Lặp lại các thử nghiệm ngẫu nhiên nhiều lần: Mỗi thử nghiệm đại diện cho một kịch bản có thể xảy ra.<br/>
- Sử dụng phân phối xác suất: Xác định các biến đầu vào không chắc chắn (như giá trị, thông số, hoặc các yếu tố ngẫu nhiên).<br/>
- Tính toán và ghi lại kết quả: Với mỗi lần thử nghiệm, kết quả được ghi nhận và phân tích để tạo thành một tập hợp các kết quả.<br/>
- Phân tích dữ liệu: Từ tập hợp kết quả, ta có thể tính toán các chỉ số quan trọng như trung bình, độ lệch chuẩn, xác suất xảy ra của các kết quả cụ thể.<br/>
<br/>

Chi tiết về thuật toán được giải thích trong [báo cáo Đồ án 2](https://github.com/Haipham2002/Option_Pricing_Models/blob/main/Ph%E1%BA%A1m_L%C3%A2n_H%E1%BA%A3i_20203880_%C4%90A2.docx)
<br/>
Source code và các kết quả sau khi cài đặt thuật toán xem [tại đây](https://github.com/Haipham2002/Option_Pricing_Models/tree/main/Option_Pricing_Model/Monte_Carlo)
