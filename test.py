import character, game_play, random, item

# 캐릭터 생성 테스트 
for i in range(20):
     # 생성
    eyes = random.choice(item.eyes)
    mouth = random.choice(item.mouth)
    acc = random.choice(item.outside_acc)
    body = random.choice(item.body)
    name = random.choice(item.names)
    
    char = character.character(eyes, mouth, acc, body)
    char.set_face()
    char.set_name(name)
    char.calculate_beauty()

    print(char.face + "\n")

# print("*\n*\n*\n*")
# print("|\n|\n|\n")
