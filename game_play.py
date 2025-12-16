# -*- coding: utf-8 -*-
import intro, data, item, character, family, date, input_validation as iv
import random, time, sys, os, locale

# my 캐릭터 생성 
def character_born(family_name):

    time.sleep(2)
    print("\n*:･ﾟ✧由*:･ﾟ✧\n")
    
    text = "캐 릭 터 생 성 중\n\n"
    for ch in text:
        print(ch, end="", flush = True)
        time.sleep(1)
    print()

    # 생성
    eyes = random.choice(item.eyes)
    mouth = random.choice(item.mouth)
    acc = random.choice(item.outside_acc)
    body = random.choice(item.body)
    
    player = character.Character(eyes, mouth, acc, body)
    player.set_face()
    player.calculate_beauty()

    # 가계도 생성
    my_family = family.Family(family_name)
    my_family.add_family(player) # 가계도에 추가 

    print("♥ 캐릭터가 태어났어요 ♥\n")
    time.sleep(2)
    # 출력
    print("─────────────────\n")
    print("  " + player.face)
    print("\n─────────────────\n")
    name = iv.input_text("이름을 정해주세요 => ", 1, 15)
    player.set_name(name)

    time.sleep(2)
    print(f"이름 [{name}](을)를 부여받았습니다!")

    return player, my_family
    
# 메뉴 
def menu():
    while True:
        print(data.divider)
        time.sleep(2)
        print(f'=====[{player.name}(과)와 함께]=====\n')
        time.sleep(2)

        print("1. 소개팅 하기")
        print("2. 가계도 보기")
        print()

        choice = iv.input_menu_12("번호를 입력해주세요 => ")
        if choice == 1:
            return date.date(player, my_family) # 소개팅 하기
        elif choice == 2:
            my_family.print_family_tree() # 가계도 보기
 


# 캐릭터 생성 
def make_character():
    eyes = random.choice(item.eyes)
    mouth = random.choice(item.mouth)
    acc = random.choice(item.outside_acc)
    body = random.choice(item.body)
    name = random.choice(item.names)
    
    char = character.Character(eyes, mouth, acc, body)
    char.set_face()
    char.set_name(name)
    char.calculate_beauty()

    return char

# 게임 오버
def game_over(my_family):
    print(data.divider)
    print('소개팅에 실패했습니다...')
    time.sleep(1)
    print(f'{my_family.family_name} 가문의 대가 끊겼습니다')
    print()
    print()
    time.sleep(2)
    print(f'                <THE {my_family.family_name} FAMILY>\n\n')
    for index, member in enumerate(my_family.family_list, start=1):
        if index % 2 == 1: # 홀수
            print(member.face , "* * * * * * * * * ", end = '')
            face_len = len(member.face) # 얼굴 길이 기억
        elif index % 2 == 0: # 짝수
            print(member.face)
            if index < len(my_family.family_list):
                space = face_len + 8
                for i in range(6):
                    print(" " * space + "*")

    print("   X")
    print()
    print()
    time.sleep(5)
    print(r"""                                                  
  __ _  __ _ _ __ ___   ___    _____   _____ _ __ 
 / _` |/ _` | '_ ` _ \ / _ \  / _ \ \ / / _ \ '__|
| (_| | (_| | | | | | |  __/ | (_) \ V /  __/ |   
 \__, |\__,_|_| |_| |_|\___|  \___/ \_/ \___|_|   
 |___/                                              
                                                   
          """)
    time.sleep(5)
    print(data.divider)
    time.sleep(3)
    sys.exit()


# 가문명 정하기
def set_family_name():
    family_name = iv.input_text("가문명을 정해주세요 => ", 1, 20)
    print(f"가문명 [{family_name}](을)를 부여받았습니다!")
    return family_name


def setup_console():
    # 현재 인코딩 확인
    current_encoding = sys.stdout.encoding or locale.getpreferredencoding(False)

    if os.name == "nt":
        try:
            # 명령 프롬프트 코드 페이지 UTF-8로 변경
            os.system("chcp 65001 >NUL")
        except Exception:
            pass

        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            # 출력, 입력 코드 페이지를 UTF-8로 설정
            kernel32.SetConsoleOutputCP(65001)
            kernel32.SetConsoleCP(65001)
        except Exception:
            pass

    # 파이썬 표준 입출력 인코딩 재설정 
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        # 파이썬 3.7 미만이거나 reconfigure 미지원 환경인 경우
        pass


# =====================================================

# 메인 
if __name__ == "__main__":
    setup_console()
    intro.show_intro()

    print(data.divider)

    family_name = set_family_name()

    descendant, my_family = character_born(family_name) 

    while True:
        player = descendant 
        time.sleep(2)
        descendant = menu()






    


