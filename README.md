
## Requirement 
```bash
pip install -r requirements.txt
```
## Run 
```bash
python run.py
```

## Endpoint 
```bash
# URL Endpoint 1
http://localhost:5002/api/v1/assignment/add
# URL Endpoint 2
http://localhost:5002/api/v1/assignment/query
```

# Test
```bash
# Run test
pytest
```
# Summary
    - Có nhiều method tính toán quantile, wiki liệt kê ra 9 định nghĩa
    - 3 method R1, R2, R3 có sự phân mảnh, không liên tục, dựa trên làm tròn dữ liệu.
    - 6 method R4-9 có sự liên tục, dưa trên hàm nội suy tuyến tính
    - Quantile trong thư viện numpy implement method R7
    - P2 Algorithm cũng là method tính toán quantile
      khác biệt là nó tiếp đi theo hướng tối ưu storing
    - Đây là version đáp ứng yêu cầu đề bài và còn nhiều vấn đề cải tiến.  