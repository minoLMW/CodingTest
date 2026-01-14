def solution(original_edges, compare_edges):
    # original_edges, compare_edges: [(parent, child), ...] 형태라고 가정

    def build_parent_map(edges):
        parent = {}
        nodes = set()
        for p, c in edges:
            parent[c] = p
            nodes.add(p)
            nodes.add(c)
        return parent, nodes

    p1, nodes1 = build_parent_map(original_edges)
    p2, nodes2 = build_parent_map(compare_edges)
    all_nodes = nodes1 | nodes2  # 동일 ID라고 했지만 안전하게 합집합

    def build_path_func(parent_map):
        memo = {}  # node -> tuple(path from root to node)

        def get_path(x):
            if x in memo:
                return memo[x]

            stack = []
            cur = x
            # 아직 경로가 계산되지 않은 노드들을 스택에 쌓고 위로 올라감
            while cur is not None and cur not in memo:
                stack.append(cur)
                cur = parent_map.get(cur)  # 루트면 None

            # cur가 None(루트 위)거나 memo에 있는 노드
            base = memo[cur] if cur in memo else ()
            # base는 (root..cur) 경로, stack을 아래에서부터 붙임
            path = base
            for node in reversed(stack):
                path = path + (node,)
                memo[node] = path
            return memo[x]

        return get_path

    path1 = build_path_func(p1)
    path2 = build_path_func(p2)

    diff = []
    for node in all_nodes:
        if path1(node) != path2(node):
            diff.append(node)

    diff.sort()
    return diff


# 예시 테스트(문제 화면 예시 기준)
original = [(1,2),(1,3),(3,4),(3,5),(3,6)]
compare  = [(1,2),(1,5),(2,3),(3,4),(5,6)]
print(solution(original, compare))  # [3,4,5,6]
