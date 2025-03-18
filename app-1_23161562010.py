from collections import deque

def bfs_shortest_path(city_map, start, goal):
    if start not in city_map or goal not in city_map:
        return f"Tidak ditemukan '{start}' atau '{goal}' dalam peta."

    queue, visited = deque([[start]]), set()

    while queue:
        path = queue.popleft()
        if path[-1] == goal:
            return path
        
        visited.add(path[-1])
        queue.extend(path + [n] for n in city_map[path[-1]] if n not in visited)

    return f"Tidak ada jalur dari '{start}' ke '{goal}'."

# Struktur peta kota
city_map = {
    'Home': ['Mall', 'School'], 'Mall': ['Gym', 'Hospital'],
    'School': ['Library'], 'Gym': ['Hospital'],
    'Library': ['Hospital'], 'Hospital': []
}

# Contoh penggunaan
print("Jalur Terpendek:", bfs_shortest_path(city_map, "Home", "Hospital"))
