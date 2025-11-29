import data, game_play, calculate, descendant
import time

# 소개팅 
def date(player, my_family):
    print(data.divider)

    time.sleep(2)
    print("소개팅에 참여합니다\n")
    time.sleep(2)


    # 파트너 생성 
    partner_1 = game_play.make_character()
    partner_2 = game_play.make_character()
    partner_3 = game_play.make_character()

    # 이름이 중복되면 다시 생성
    while True:
        if (partner_1.name == partner_2.name):
            partner_1 = game_play.make_character()
        elif (partner_1.name == partner_3.name):
            partner_1 = game_play.make_character()
        elif (partner_2.name == partner_3.name):
            partner_2 = game_play.make_character()
        else: break

    partners = [partner_1, partner_2, partner_3]
    reject_check =[False, False, False] # 거절 체크 

    # 청혼 
    while True:
        # 전부 거절 체크
        if(all(reject_check)):
            game_play.game_over(my_family)

        # 파트너 출력 
        for idx, partner in enumerate(partners, start=1):
            print(f'{idx}.')
            print()
            print(partner.face)
            time.sleep(1)
            print()
            print(data.speech_ballon_upper)
            print(f' 안녕! 나는 {partner.name}(이)야')
            print(data.speech_ballon_down)
            print()
            time.sleep(2)


        print(data.divider)
        choice = int(input("청혼할 상대를 골라주세요 (1/2/3) => "))
        if reject_check[choice-1]: #이미 거절함
            print()
            print(f'! [{partners[choice-1].name}]에게 다시 청혼할 수 없습니다')
            time.sleep(2)
            print()
            print('다른 상대에게 다시 청혼해주세요\n')
            print()
            time.sleep(2)
            continue

        fiancee = partners[choice-1]
        time.sleep(1)
        print(f'[{fiancee.name}]에게 청혼합니다')
        time.sleep(1)
        print()
        print()
        print(fiancee.face + "       @>-- " + player.face)
        print()
        space = len(fiancee.face) + 9
        print(" " * space + data.speech_ballon_upper)
        print(" " * (space + 1) + "𝑊 𝑖𝑙𝑙 𝑦𝑜𝑢 𝑚 𝑎𝑟𝑟𝑦 𝑚 𝑒?")
        print(" " * space + data.speech_ballon_down)
        time.sleep(1)

        text = "고 민 중 . . .\n\n"
        for ch in text:
            print(ch, end="", flush = True)
            time.sleep(0.5)
        print()
        time.sleep(2)

        if (calculate.calculate_marriage(player, fiancee)): # 수락
            print(f'축하합니다! [{fiancee.name}](이)가 청혼을 수락했습니다')
            time.sleep(5)
            break
        else: # 거절
            reject_check[choice-1] = True
            print(f'[{fiancee.name}](이)가 청혼을 거절했습니다')
            print()
            time.sleep(2)
            print('다른 상대에게 다시 청혼해주세요\n')

    my_family.add_family(fiancee) # 가계도에 추가

    return descendant.make_descendant(player, fiancee, my_family) # 후손 만들기 
    


    
    

