def numDuplicates(names, prices, weights):
    # 튜플로 제품의 이름, 가격, 무게를 묶어서 한 제품으로 표현
    products = list(zip(names, prices, weights))

    # 각 제품에 대한 개수를 세는 딕셔너리 생성
    product_count = {}

    # 각 제품에 대해 개수 세기
    for product in products:
        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1

    # 중복 제품 수 세기
    duplicate_count = 0
    for count in product_count.values():
        if count > 1:
            # 제품이 중복되는 경우, 중복 개수에서 1을 빼서 더하기
            duplicate_count += (count - 1)

    return duplicate_count