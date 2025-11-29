import data
import time

class Family:
    def __init__(self, family_name):
        self.family_list = []
        self.family_name = family_name

    def add_family(self, character):
        self.family_list.append(character)

    def print_family_tree(self): # 가계도 출력 
        print(data.divider)
        text = "입 장 중 . . .\n"
        for ch in text:
            print(ch, end="", flush = True)
            time.sleep(0.5)

        print(data.divider)
        print()
        time.sleep(2)
        print(f'                <THE {self.family_name} FAMILY>\n\n           ')
        for index, member in enumerate(self.family_list, start=1):
            if index % 2 == 1: # 홀수
                print(member.face , "* * * * * * * * * ", end = '')
                face_len = len(member.face) # 얼굴 길이 기억
            elif index % 2 == 0: # 짝수
                print(member.face)
                if index < len(self.family_list):
                    space = face_len + 8
                    for i in range(6):
                        print(" " * space + "*")
        
        print(" ? ")
        print()
        time.sleep(2)
        return 
            