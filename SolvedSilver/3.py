def ProgrammerStrings(s):
    target = list('programmer')
    s_list = list(s)
    left, right = [], []

    # 찾은 문자열을 pop으로 제거하면서 첫 번째 programmer 문자열을 찾음
    for i in range(len(s_list)):
        if s_list[i] in target:
            target.remove(s_list[i])
            if len(target) == 0:
                left = s_list[:i + 1]
                break

    target = list('programmer')  # 다시 target 초기화

    # 뒤에서부터 찾은 문자열을 pop으로 제거하면서 두 번째 programmer 문자열을 찾음
    for i in range(len(s_list) - 1, -1, -1):
        if s_list[i] in target:
            target.remove(s_list[i])
            if len(target) == 0:
                right = s_list[i:]
                break

    # 두 programmer 문자열 사이의 인덱스 수 반환
    return len(s_list) - len(left) - len(right)
