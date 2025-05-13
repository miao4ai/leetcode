from collections import defaultdict, deque

def numBusesToDestination(routes, source, target):
    if source == target:
        return 0

    # 建立站点 -> 路线 映射
    stop_to_routes = defaultdict(set)
    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)

    visited_routes = set()
    visited_stops = set()
    queue = deque()
    
    # 初始化：从source出发，加入所有包含source的路线
    for route_id in stop_to_routes[source]:
        queue.append((route_id, 1))
        visited_routes.add(route_id)

    while queue:
        route_id, bus_count = queue.popleft()
        route = routes[route_id]

        # 如果当前路线包含 target，直接返回bus_count
        if target in route:
            return bus_count

        # 遍历当前路线所有的站点，找到其他路线可以转乘
        for stop in route:
            if stop in visited_stops:
                continue
            visited_stops.add(stop)
            for next_route in stop_to_routes[stop]:
                if next_route not in visited_routes:
                    visited_routes.add(next_route)
                    queue.append((next_route, bus_count + 1))

    return -1  # 找不到路径
