
init_xpos = 2
init_ypos = -2
init_zpos = -178
init_rpos = 45

init_CoinWeight = -41



# dType.SetPTPCmd 복사용
# dType.SetPTPCmd(api, 2, init_xpos, init_ypos, init_zpos, 0, 1)
#                 api,모드,   x좌표,    y 좌표,  z 좌표, 엔드 이펙터 회전각도 ,행동모드
# dType.SetEndEffectorSuctionCup 복사용

def enable_suction_cup():
    dType.SetEndEffectorSuctionCup(api, 1, 1, 1)
# 흡입컵을 켜는 함수

def disable_suction_cup():
    dType.SetEndEffectorSuctionCup(api, 1, 0, 1)
# 흡입컵을 끄는 함수


 ## 모든 시작점은 다 같음 x, y 자표만 수정 하면 됨

def paper_millon(repeat):
    for i in range(repeat):
        dType.SetPTPCmd(api, 2, init_xpos, init_ypos, init_zpos, 0, 1)
        dType.SetPTPCmd(api, 2, 43, -316, -52, 0, 1)
        # 금액 집는 곳
        enable_suction_cup()
        dType.SetPTPCmd(api, 2, init_xpos, init_ypos, init_zpos, 0, 1)
        dType.SetPTPCmd(api, 2, 189, -2, -5, 0, 1)
        disable_suction_cup()


def coin_five(repeat, count):
    index = count % 5
    for i in range(repeat):
        height = index * -2
        dType.SetPTPCmd(api, 2, init_xpos, init_ypos, init_zpos, 0, 1)
        dType.SetPTPCmd(api, 2, 43, -316, -52+height, 0, 1)
        # 금액 집는 곳
        enable_suction_cup()
        dType.SetPTPCmd(api, 2, init_xpos, init_ypos, init_zpos, 0, 1)
        dType.SetPTPCmd(api, 2, 189, -2, -5, 0, 1)
        # 내려놓을때 쌓을건지 대충 떨어트릴건지 생각해야됨
        # 높이 적당히 잡으면 될듯?
        disable_suction_cup()
        if index == 0:
            index = 5
        else:
            index = index-1

