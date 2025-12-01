# -*- coding: utf-8 -*-
import item
import random

# 청혼 승낙 여부 계산
def calculate_marriage(player, fiancee):

    beauty_differ = player.beauty - fiancee.beauty

    # 확률 계산
    if beauty_differ >= 20: # player가 20 이상으로 더 예쁠경우
        beauty_differ -= beauty_differ * 0.5 # 확률 높이기
    # if beauty_differ <= -20: # plaeyer가 20 이상으로 더 안 예쁠경우
        # beauty_differ += beauty_differ * 0.5 # 확률 낮추기

    accept_probability = 1 - (30 - beauty_differ) / 100

    r = random.random() # 0 이상 1 미만의 난수 생성
    return r < beauty_differ



# 자손 유전자 결정 
def calculate_gene(player, fiancee):
    gene_pool = [(player.eyes, fiancee.eyes, item.eyes_point), (player.mouth, fiancee.mouth, item.mouth_point), # 유전자 풀 
                  (player.acc, fiancee.acc, item.outside_acc_point)] 
    descendant_gene = [] # [eyes, mouth, acc, body]

    for ancester_1, ancester_2, component_point in gene_pool:
        weight_1 = 11 - get_point(ancester_1, component_point)
        weight_2 = 11 - get_point(ancester_2, component_point)
        total_weight = weight_1 + weight_2

        p_ancester_1 = weight_1 / total_weight # p_ancester_2 = 1 - p_ancester_1
         
        r = random.random()
        if r < p_ancester_1: 
             descendant_gene.append(ancester_1)
        else:
             descendant_gene.append(ancester_2)

    # body는 따로 주입
    descendant_gene.append(random.choice([player.body, fiancee.body]))
    
    return descendant_gene


# 딕셔너리에서 포인트 뽑아오기 
def get_point(target, component_point):
    for point, component_lst in component_point.items():
        if target in component_lst:
            return point





