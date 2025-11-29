import data, calculate, character
import time

def make_descendant(player, fiancee, my_family):
    print(data.divider)
    print(f'[{player.name}](이)와 [{fiancee.name}](은)는 행복합니다!')
    print()
    print(fiancee.face + "    ♥ ♡ ♥ ♡ ♥ ♡    " + player.face)

    text = "\n\n♥ ♡ ♥\n\n"
    for ch in text:
        print(ch, end="", flush = True)
        time.sleep(2)
    print()
    
    # 후손 생성
    while True:
        descendant_gene = calculate.calculate_gene(player, fiancee) # descendant_gene = [eyes, mouth, acc, body]
        descendant = character.Character(descendant_gene[0], descendant_gene[1], descendant_gene[2], descendant_gene[3])
        descendant.set_face()
        descendant.calculate_beauty()
        my_family.add_family(descendant)

        if descendant.face != player.face and descendant.face != fiancee.face: break # 부모의 얼굴과 100% 동일 방지

    print(f'[{player.name}](이)와 [{fiancee.name}]의 자손이 태어났습니다')
    print(data.divider)

    time.sleep(5)
    print("-----------------\n")
    print("  " + descendant.face)
    print("\n-----------------\n")
    name = input("이름을 정해주세요 => ")
    descendant.set_name(name)

    time.sleep(2)
    print(f"이름 [{name}](을)를 부여받았습니다!")

    return descendant





    