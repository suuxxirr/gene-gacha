import item

class Character:
    beauty = 0
    face = ""

    def __init__(self, eyes, mouth, acc, body): 
        self.eyes = eyes
        self.mouth = mouth
        self.acc = acc
        self.body = body

    def set_name(self, name):
        self.name = name

    def set_face(self): # 얼굴 생성
        l_acc, r_acc = self.acc.split()
        l_eye, r_eye = self.eyes.split()
        l_body, r_body = self.body.split()
        self.face = l_acc + l_body + " " +  l_eye + " " + self.mouth +" " + r_eye + " " + r_body + r_acc 

    def calculate_beauty(self): # 포인트 계산 
        eye_point = self.get_point(self.eyes, item.eyes_point)
        mouth_point = self.get_point(self.mouth, item.mouth_point)
        outside_acc_point = self.get_point(self.acc, item.outside_acc_point)
        
        self.beauty = eye_point + mouth_point + outside_acc_point

    # 딕셔너리에서 포인트 뽑아오기 
    def get_point(self, target, component_point):
        for point, component_lst in component_point.items():
            if target in component_lst:
                return point

        

    

    