<h1>Melon Web Scraping</h1> 
<br>
<hr>
<div align="center">
<h2>Tech Stack</h2>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white">
<img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=JSON%20web%20tokens&logoColor=white">
</div>
<hr>
<h2>🌟introduction🌟</h2><br>
  <br>1. 순위 표시
  <br>2. 순위 1위부터 100위까지위 곡들의 정보 가져오기
  <br>(순위, 노래제목, 가수, 앨범정보)
  <hr>
  <br><h3>(추가중인 기능)</h3>
  앨범 정보를 가져와서 화면 전환시에 song_id를 가져오지 못한것에 대한 기능 추가 예정
  <br>
  <img src="https://github.com/user-attachments/assets/98d0c031-c8ad-4c1d-afe8-ac91b3078cc2">
<hr>
<br>
<h2>📊ERD📊</h2><br>
<img src="https://www.plantuml.com/plantuml/png/VP5DQzH06CVl-HGFlQY7-07s8BMYY5WGTy53AMLCnsJivCMPYHL4g58zsDGNs4Cfkv85TLrGYEiBUn3yFfd9Tp0P9uanq6F8_7_Fx_a_wrmW9cAVMX5ozf2BOUqElWj3Xw681EuQFBO00BPSB7PyJCDWn_7AmFaBss3Rbs2BuGSnve9lmm3KwLWjlu1A3zMBsTcn3OnYGUx5T1Z6KPMzFjgy2KMIgAElrXEhbRb64T-3or54YOC42OF6IFynkFwO4YaN4pbBGMMVYfShaCUPcdul3ZF8imELhjJ9-toLzL4tI70VmGZx4KK2jshF9yKuaHz_WqmJUJoMywSTpph0ZLyVfEbQxw8dV5gHMoVrSoBJ3ntYrKS2im1H66Bsa3WjkUdSC3UhnU5AHORoTfpKsgDRvYGTxWOBzpbc3Sry6rYlx_zHEjD_fTCjoxIcfc_bqOzg_3cuZQb-oZqISKjBQsUZ3FPkk1-Ka7ex6DIdArwTb3Mf-O66MdhuFxF1PiJrH1dLbTUDmw0z5UJBBF_sws_UI3O3UxnoyBFFwdIXthqnMuFCNdSsMiV1RkpJFm00">
<hr>
<br>
<h2>🕸️Web Scraping🕸️</h2><br>
<h3><em>get_melon_chart():</em></h3> 멜론 차트 웹 페이지에서 데이터를 스크래핑하여 반환합니다.<br>
<h3><em>requests:</em></h3> HTTP 요청을 통해 멜론 차트 페이지 HTML을 가져옵니다.<br>
<h3><em>BeautifulSoup:</em></h3> HTML을 파싱하여 필요한 데이터를 추출합니다.<br>
<h3><em>Flask:</em></h3> 웹 서버로 사용자 요청을 처리하고 HTML을 반환합니다.<br>
<h3><em>Jinja Template:</em></h3> 데이터를 HTML 템플릿에 삽입해 렌더링합니다.<br>
<h3><em>chart.html:</em></h3> 멜론 차트 데이터를 보여줄 HTML 템플릿입니다.<br>
<h3><em>Melon Chart Website:</em></h3> 데이터를 제공하는 외부 웹사이트입니다.<br>
<h3><em>Browser:</em></h3> 사용자가 요청을 보내고 HTML 응답을 받는 웹 브라우저입니다.<br>
