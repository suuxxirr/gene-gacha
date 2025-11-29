import data, sys, game_play
import time


def show_intro():
    print(r"""
                  _                          
    __      _____| | ___ ___  _ __ ___   ___ 
    \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
     \ V  V /  __/ | (_| (_) | | | | | |  __/
      \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                                    
    """)

    time.sleep(2)
    print(data.divider)
    time.sleep(2)

    print(r"""                               
     _ __ ___   ___ _ __  _   _ 
    | '_ ` _ \ / _ \ '_ \| | | |
    | | | | | |  __/ | | | |_| |
    |_| |_| |_|\___|_| |_|\__,_|
                                
        """)
    
    print("1. 게임 시작")
    print("2. 게임 설명")
    print("3. 게임 종료")
    print(data.divider)

    choice = int(input("번호를 입력해주세요 => "))
    if choice == 1:
       return
    elif choice == 2:
        game_description()
    elif choice == 3: 
        sys.exit()
       

        
def game_description():
    print(data.divider)
    print("게임 설명 작성 예정")
    print("소개팅을 통해 귀여운 캐릭터와 결혼하고 자손을 낳아보세요")
    print("캐릭터의 외모가 예쁠수록 청혼 성공 확률이 높아집니다")
    print("청혼에 성공하면 부모의 외모 특성을 물려받은 자손을 얻을 수 있습니다람쥐")
    print("\n")
    choice = input("번호를 입력해주세요 => ")

