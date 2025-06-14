from altair import Chart
import streamlit as st
st.title("🌲모터스 매거진 5월호:evergreen_tree:\n **역대급 현대가더비 5월31일 전북현대VS울산HD 심층분석**")
st.header("👋 1. 매치 프리뷰")
st.image("https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTBfMTUy/MDAxNzQ5NTQzMjIyMDk1.5SRiq6lFSDbIyzCX3Tl4IMfWiySRwnswhynPJ2fpqYYg.LdDKGzyjO4Xn-I2NWP6jQgQSvhLdsUFYxYk13KTUwMQg.PNG/001.png?type=w800", caption="전북 현대 모터스,울산HD 엠블럼", width=500)
st.write("""
거스 포옛 감독을 선임하면서 명가 재건을 선언한 :green[전북현대]가 디펜딩 챔피언인 :blue[울산HD]를 만났다. \n
전북은 시즌 초 포옛 감독의 K리그 적응기에 울산과 만나 무기력한 패배를 당하며 시즌 스타트를 좋지 않은 분위기에서 끊었다.
하지만 포옛 감독은 선수들의 안 좋은 습관에 대해 꾸준히 이야기하며 위닝멘탈리티를 최우선 과제로 팀을 수습해 나갔고, \n
그 결과 3월 15일 안양전 이후 약 두 달간 무패행진을 하면서 자신의 능력을 증명했다.""")
st.divider()
st.write("**:green[​기세가 하늘을 찌르는 이 시기에 :green[전북]은 울산을 홈으로 불러들였다.]**")
st.write("""
**:green[전주 월드컵 경기장은 구단 역사상 최초로 매진되었고  \n 팬들은 라이벌 울산을 잡기 위한 압도적인 분위기를 조성하며 전북은 3 대 1 대승을 거두었다.]**""")
st.divider()
st.header("2. 🏟 매치 정보")
col1, col2 = st.columns(2)
with col1:
    st.image(
        "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FPYSE.img?w=768&h=512&m=6",
        use_container_width=True
    )
with col2:
    st.image(
        "https://img-s-msn-com.akamaized.net/tenant/amp/entityid/AA1FQ6o8.img?w=768&h=512&m=6",
        use_container_width=True
    )
st.write("*경기날짜: 2025년 5월31일 17시  \n 경기장소: 전주 월드컵 경기장  \n 관중수: 31,830명  \n 최근 전적: 전북 1승 1무 3패*")
st.divider()
st.header("2.🏆 경기결과")
st.write("**:green[3:1 전북 승]**")
st.write("**경기지표**")
import pandas as pd
df = pd.DataFrame(
    {
        "팀":       ["전북 현대",     "울산 현대"],
        "점유율":   ["46%",           "54%"],
        "슈팅":     [9,                9],
        "유효슈팅": [7,                4],
        "코너킥":   [4,                6],
        "파울":     [11,               5],
        "경고":     [2,                1],
        "퇴장":     [0,                0],
    }
)
df
st.divider()
st.header("3.♟️전술 분석 ")
st.subheader("*수준 높은 지략 대결을 보여준 양팀 감독*")
st.write("'소문난 잔치에 먹을게 많다'라는 말처럼 양팀의 대결에는 볼거리가 풍부했다.  \n 양 팀 감독의 전술을 3가지 측면에서 분석해보았다.")
st.write(":green[**(1) 전북의 수비**]")
st.caption("K리그 최소실점 팀")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTFfMTg2/MDAxNzQ5NjE3NDM0NjU4.yC_2_7NgPdZhz0Kt_XD_Mx-TB3F86UfJ98EjHkfYRjIg.3nqWtuwC8ToL74hUaRF2zm5J32Ft59F-UgYfpxB9UcIg.PNG/%EC%A0%84%EB%B6%81_4141.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("전북은 수비 시에 4-1-4-1을 선택했다.  \n **전진우 강상윤 김진규 송민규**를 일정한 간격으로 배치해 중원으로 들어가는 패스길을 차단하고 최종 수비 라인과의 사이 공간을 박진섭이 차지했다. 이는 울산의 패스 선택지를 제한시켰다. 따라서 울산은 중원으로 적극적으로 볼 투입을 할 수 없었다. 또한 울산도 이와 같은 중원 압박을 펼치면서 이 경기는 **중원 싸움이 아주 치열한**경기였다.")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTFfNDQg/MDAxNzQ5NjIwMTc3ODgz.RSUKhOI74ctkyQ29FoxqtvGgw6zGvHe-HcI2nVIvel4g.Vzw91odBSqNm--EN44rlkK5DvKE2pmL_tgGQRRNz994g.PNG/%EB%B0%95%EC%A7%84%EC%84%AD_%EB%B0%95%EC%8A%A4_.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("울산이 충분한 전개를 진행한 후 볼을 깊은 지역까지 운반했을 때 **박진섭**은 박스 안으로 들어가 최종 수비라인을 구성한다. 이번 시즌 전북은 최소 실점 팀으로서 아주 막강한 수비력을 보여주고 있다. 그 수비에서 이번 시즌 가장 돋보이는 변화는 박진섭의 이런 시프트다. 박진섭이 박스로 내려와 골이 나올 수 있는 박스 안 공간을 차지하고 강상윤 김진규가 박스 밖에서 대기하는 상대 중원을 1:1로 방어한다. 이러한 전북의 짜임새 있는 수비는 이번 시즌 팀에 안정감을 가져다주었다. ")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMTc4/MDAxNzQ5NzA1MDg2Njg1.zy_GRpdq3fIJ82UF2Y149O-mIE4lMkh5tcJziPt1OTkg.1W7gX10su5FZFhrokkJwYJO04wQVKsIdAaYb9eW7wIUg.PNG/%EC%A0%84%EB%B6%81_%EB%B0%95%EC%8A%A4_%EC%88%98%EB%B9%843.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("후반에는 울산이 박스 안 공격 숫자를 더 늘렸다. 하지만 이미 수비 숫자가 많은 전북이었기에 울산이 숫자를 늘리더라도 수적 우위를 점할 수 없었다. 교체로 들어간 권창훈도 기존 강상윤이 하던 역할과 똑같이 박스 근처에 있는 상대 미드진들을 대인방어하며 세컨볼에 대한 대비를 했다. 이렇게 전북은 이번 시즌 박스에서의 실점을 줄여나가고 있다. 전북은 그냥 생각 없이 박스 안에 숫자만 늘리는 것이 아니라 굉장히 짜임새 있는 **조직적인 수비**를 하고 있다.  \n ")
st.write(":green[**(2) 포옛 감독의 대응**]")
st.caption("인버티드 윙어 전진우")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMjA2/MDAxNzQ5NzI5MzU0ODI4.44b0aDuTzqSYTO8U-TCWi-AgFiwKx1bK8doO5h8cVngg.qHs3OuNpg_3rw14CSfdaTEbACAJsdUAdQA9gpjWbJ-og.PNG/%EC%A0%84%EC%A7%84%EC%9A%B0_%EC%9D%B8%EB%B2%84%ED%8B%B0%EB%93%9C_%EA%B9%80%ED%83%9C%ED%99%98_%EA%B3%B5%EA%B0%84.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("**전북은 경기 초반 울산의 압박에 완전히 고전했다.** 후방으로 볼이 넘어갔다고 하더라도 서명관이 모든 것을 막아세웠다. 전북의 공격 패턴은 단순하게 표현하면 중원을 통해 측면으로 간결하면서도 다이렉트하게 전개하는 방식이다. 하지만 전북은 좀처럼 중원을 통과하지 못했다. 포옛 감독은 이에 대한 피드백을 빠르게 가져갔다. 중원에 가담하는 선수의 숫자를 늘렸다. 포옛은 최종적으로 측면 깊숙한 지역에서 측면 자원들이 볼을 잡고 박스 안으로 타격하는 방식을 포기하지 않았다.  \n ")
st.write("**포옛은 측면에 공간을 만들기 위해 전진우를 안으로 좁혔다.** 전진우가 안으로 들어오고 강상윤과 김진규를 중원에 더 밀집 시켜 중원에서의 **과부하**를 걸었다. 따라서 울산의 미드필더들은 중앙으로 들어온 전진우를 체크할 수 없었고 루빅손이 전진우를 막기 위해 중원으로 들어왔다. ")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMjMg/MDAxNzQ5NzI5NTUxNDI2.buMZgYST74KlqH1F2wA1_WGJ9b847zoI9swO3GT8Yo4g.S4wHTfjsJZpiQZJLjQur3HOEsVaJ-agmRW1PFpoS3z0g.PNG/%EB%A3%A8%EB%B9%85%EC%86%90_%EB%94%B8%EB%A0%A4_%EB%82%98%EC%98%B41.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("후반전도 마찬가지였다. 이청용이 중앙 미드필더에 가깝게 위치하면서 왼쪽은 루빅손 혼자 담당했다.  \n 김태환이 볼을 잡았을 때 김태환을 압박하는 선수가 없었기 때문에 자연스레 루빅손이 앞으로 나간다. **하지만 루빅손이 비우고 나온 자리에 대한 커버가 전혀 없었고 이 공간은 프리한 공간이 되었다.** 전북은 이렇게 측면에 공간을 만들어냈다.  \n ")
st.write(":green[**(3) 후반전 울산과 전북의 에너지 레벨 차이**]")
st.caption("울산의 패배 요인")
st.write("치열했던 경기의 승패를 가른 요인은 무엇이었을까, 기록을 살펴보면 김판곤 감독이 전술적으로 부족한 부분은 있지만 이 경기에서 동점골 실점 장면을 제외하면 전술적으로 전북이 울산을 압도했다고 보기는 힘들다. 하지만 준비가 더 잘 되어있는 팀은 전북이었다.  \n  \n")
st.write("**체력과 집중력**  \n  \n")
st.write("축구 선수들은 당연히 90분, 100분 뛸 체력이 충분하다. 하지만 90분 내내 같은 에너지 레벨과 압박 강도, 그리고 집중력을 유지할 수는 없다. 당연히 70분부터 선수들은 지친다. 하지만 지치는 정도가 어디까지냐에 근거해 우리는 그 선수의 체력에 대해 평가한다. 전북은 경기 템포를 보았을 때 전체적으로 경기 시작과 경기 종료 시점에 큰 차이가 없다. 지치긴 하지만 지치는 정도가 낮은 것이다. 반면 울산은 이 경기에서 지치는 정도가 높았다. ")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMTg2/MDAxNzQ5NzMwNjE1Mzgw.fJ5CyAtNFoSMIQPa5lQYI8h2ffrbMCnDpCaD5NXUK2Ug.rOHfGX3XA6oFF5hwmLqJyJyFHLLjxnisHF7K-XfXO60g.PNG/%EC%9A%B8%EC%82%B0_%EB%B0%95%EC%8A%A4_%EC%88%98%EB%B9%84.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("후반전 시작 직후 전북의 역습 장면이다. 울산의 중원과 공격수들은 빠르게 내려와 수비를 돕는다. 이때 미드필더 4명은 같은 선상을 유지하면서 조직적으로 박스를 방어한다.  이 역습에 대한 수비 방식은 울산이 전반전에도 똑같이 구사하며 전북의 공격 작업을 방해하고 상대를 뒤로 물렀다. ")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMjQw/MDAxNzQ5NzMwODY4MzQx.TE3rGoLRHeY_Kv6MkTXwDmP1H-u8YsLC5S83g1fY_FIg.lWsa2yodXjKXYiJPtHpWio3lZLv7i5enUGSS3qkNgqEg.PNG/%ED%9B%84%EB%B0%98_%EC%A0%95%EC%9A%B0%EC%98%81_%EC%84%BC%EB%B0%B1_%EB%B0%8F_%EC%A4%91%EC%9B%90_%EC%95%BD%ED%95%A8.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("반면 전북의 후반전 80분 역습 장면이다. 울산 선수들의 수비 복귀 속도는 경기 초반, 중반과 비교했을 때 약 2~3초가 차이 난다. **따라서 박스 안에 있는 이승우와 박스 근처에 있는 김태현은 프리한 상태가 되었다.**")
st.image(
        "https://mblogthumb-phinf.pstatic.net/MjAyNTA2MTJfMjEx/MDAxNzQ5NzMxMTA4Njcz.TTBrFtFwePI1YxojQ6Zi21bPplxFxbNpkftiFd2-Hqgg.aUe_SapbblTWej2dVd9Ns5INqSZ2QiwG9WLtBGxAnw4g.PNG/%EC%9A%B8%EC%82%B0_%ED%9B%84%EB%B0%98_%EC%95%95%EB%B0%95_%EA%B0%95%EB%8F%84_%EC%95%BD%ED%99%94.png?type=w800",
        use_container_width=True,
        caption=("쿠팡플레이")
    )
st.write("울산의 체력이 떨어지며 최전방과 중원 사이 공간이 벌어지기 시작했다. 특히 전방 압박 강도가 약해지면서 전북은 비교적 쉽게 중원에서 탈압박을 하고 경기를 풀어나갔다.  \n 이후 전북이 2골을 연달아 득점하며 끝까지 **뒷심**을 발휘한 전북현대가 승리를 가져갔다.")
st.divider()
st.header("4.🥇 Man of the match ")
st.subheader("*전북의 캡틴, 로컬보이 no.4 박진섭*")
st.image(
        "https://jbhd-upload-file.s3.ap-northeast-2.amazonaws.com/uploadFile/newBoard/2025/05/image_483a42c5-a4b8-423c-9632-7f4dc4087eb0.jpg",
        use_container_width=True,
        caption=("전북현대 공식 홈페이지")
    )
st.write("박진섭의 경기력은 이 경기에서 볼만한 포인트였다. 박진섭은 이 경기에서 울산의 중원을 상대로 자신이 왜 국가대표인지를 확실하게 보여줬다. 이 경기에서 박진섭은 **인터셉트 3회, 볼 획득 11회**라는 아주 좋은 스탯을 기록했다. 페이퍼상으로 보더라도 박진섭은 이날 최고의 활약을 펼쳤고 **MOM**으로 선정되었다. ")
st.write("  \n  \n**:green[박진섭의 매치 기록]**  \n **공식평점 8.9**")
import pandas as pd
col1, col2, col3 = st.columns(3)
col1.metric("득점", "1득점(결승골)")     
col2.metric("유효슈팅", "1회") 
col3.metric("패스정확도", "93%") 
import pandas as pd
col1, col2, col3 = st.columns(3)
col1.metric("파이널써드 패스", "6회")     
col2.metric("인터셉트", "3회") 
col3.metric("볼 획득", "11회") 
import pandas as pd
col1, col2, col3 = st.columns(3)
col1.metric("지상경합", "4/6 (67%)")     
col2.metric("공중경합", "3/3 (100%)") 
col3.metric("파울", "2회") 
st.divider()
st.header("5. 📝전북의 2025년 리그 기록")
st.subheader("*리그최상위, 최다득점, 최소실점*")
st.write("**:green[(1)리그 성적]**")
import pandas as pd
import numpy as np
Chart_data = pd.DataFrame(
    [18, 11, 5, 2, 30, 12], 
    index=["1.경기수","2.승리","3.무승부","4.패배","5.득점","6.실점"],
    columns=["2025시즌"]
    )
st.bar_chart(Chart_data) 
st.write("**:green[(2)리그 지표]**")
st.write("**- 공격지표**")
import pandas as pd
col1, col2, col3 = st.columns(3)
col1.metric("경기당 득점", "1.7","12팀 중 1위")     
col2.metric("기대득점", "26.4","12팀 중 3위") 
col3.metric("경기당 슈팅", "3.9","12팀 중 3위") 
st.write("**- 수비지표**")
import pandas as pd
col1, col2, col3 = st.columns(3)
col1.metric("경기당 실점", "0.7","-12팀 중 12위")     
col2.metric("기대실점", "17.9","-12팀 중 11위") 
col3.metric("클린시트", "8","리그1위") 
st.divider()
st.header("6. 📝마치며")
st.subheader("*각자가 가진 책임감으로 함께 만든 결과*")
st.write("이 경기를 보면서 팬으로서도 굉장히 재밌었던 경기라는 생각이 든다. 실제로 양 팀은 파울도 잦고 슈팅도 많이 가져가면서 3만 명의 관중들 앞에서 재밌는 경기를 펼쳤다.  \n 국가대표 급 선수들이 즐비한 전북과 울산은 서로의 빌드업과 압박에 잘 대응하며 수준 높은 경기를 펼쳤다. ")
col1, col2 = st.columns(2)
with col1:
    st.image(
        "https://pbs.twimg.com/media/GsR6eSiaMAIg0XQ?format=jpg&name=900x900",
        use_container_width=True
    )
with col2:
    st.image(
        "https://jbhd-upload-file.s3.ap-northeast-2.amazonaws.com/uploadFile/newBoard/2025/05/image_580368f9-a908-4206-b423-04e877d82499.jpg",
        use_container_width=True
    )
st.write(":green[전북]은 프리시즌 체력훈련을 한 효과가 제대로 나왔다. 80분이 되어서도 선수들은 집중력을 잃지 않고 고강도 압박을 유지했고 지친 선수들은 포옛이 빠르게 캐치해 교체 카드를 사용하며 강도를 유지했다. ")
st.write("  \n더불어 이런 경기에 항상 빛을 보는 슈퍼스타 이승우가 후반전에 들어가 지친 울산의 중원을 상대로 최고의 활약을 펼쳤다. **살아나야 할 선수들이 살아나고 있고 팀 분위기가 아주 좋은 포옛의 전북의 앞으로의 시즌이 더욱 기대가 된다.** 하지만 이제 여름이 시작되고 경기 수가 많아지기 때문에 이 여름을 어떻게 버티는지가 중요할 것 같다. ")
st.write("  \n반면 :blue[울산]은 이제 **클럽월드컵**에 참가한다. 대한민국의 대표, 아시아의 대표로서 좋은 성적을 거두고 오길 바란다. 대회 종료 후에도 울산은 피로도를 잊고 다시 리그에 집중해야 한다. 이 여름을 어떻게 버티는지에 따라 시즌의 결과가 달라질 것이다. 여름 이적시장에서 울산의 행보도 기대해 본다.  ")