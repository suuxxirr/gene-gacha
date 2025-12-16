# -*- coding: utf-8 -*-
import data, sys, game_play, input_validation as iv
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

    while True:
        choice = iv.input_menu_123("번호를 입력해주세요 (1/2/3) => ")

        if choice == 1:
            return
        elif choice == 2:
            game_description()
        elif choice == 3: 
            sys.exit()
       

        
def game_description():
    print(data.divider)
    print("<게임 설명>")
    print("- 소개팅을 통해 귀여운 캐릭터와 결혼하고 자손을 낳아보세요")
    print("- 캐릭터의 외모가 아름다울수록 청혼 성공 확률이 높아집니다.")
    print("- 청혼에 성공하면, 부모의 외모 특성을 물려받은 자손을 얻을 수 있습니다.")
    print("- 소개팅에 실패하면 즉시 게임오버가 됩니다.")
    print("- 언제든지 우리 가문의 가계도를 확인하며 가문의 역사를 이어갈 수 있습니다.")
    print("\n")
    # choice = iv.input_menu_123("번호를 입력해주세요 (1/2/3) => ",)

