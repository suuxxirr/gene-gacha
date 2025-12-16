def input_menu_123(prompt):
    while True:
        s = input(prompt).strip()

        # 빈 입력 예외 처리
        if s == "":
            print("입력이 비어 있습니다. 1, 2, 3 중 하나를 입력해주세요.")
            continue

        # 숫자 변환 예외 처리 
        try:
            n = int(s)
        except ValueError:
            print("숫자만 입력해주세요. (1, 2, 3)")
            continue

        # 허용 값 검증 
        if n not in (1, 2, 3):
            print("잘못된 번호입니다. 1, 2, 3 중 하나를 입력해주세요.")
            continue

        return n
    
def input_menu_12(prompt):
    while True:
        s = input(prompt).strip()

        # 빈 입력 예외 처리
        if s == "":
            print("입력이 비어 있습니다. 1, 2 중 하나를 입력해주세요.")
            continue

        # 숫자 변환 예외 처리 
        try:
            n = int(s)
        except ValueError:
            print("숫자만 입력해주세요. (1, 2)")
            continue

        # 허용 값 검증 
        if n not in (1, 2):
            print("잘못된 번호입니다. 1, 2 중 하나를 입력해주세요.")
            continue

        return n

def input_text(prompt, min_len, max_len):
    while True:
        s = input(prompt).strip()

        # 빈 입력 예외 처리
        if len(s) < min_len:
            print("입력이 비어 있거나 너무 짧습니다. 다시 입력해주세요.")
            continue

        # 길이 제한 
        if max_len is not None and len(s) > max_len:
            print(f"{max_len}글자 이하로 입력해주세요.")
            continue

        return s