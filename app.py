from flask import Flask, render_template
from melon import get_melon_chart

app = Flask(__name__)

# 라우트 정의
@app.route('/')
def home():
    chart_data = get_melon_chart()  # 차트 데이터를 가져옴
    return render_template('chart.html', chart_data=chart_data)  # 템플릿에 데이터 전달

if __name__ == '__main__':
    app.run(debug=True)