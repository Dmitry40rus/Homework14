import sqlite3


def get_one(query):
    with sqlite3.connect("netflix.db") as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute(query).fetchone()
        if res is None:
            return None
        else:
            return dict(res)


def get_all(query, str):
    with sqlite3.connect("netflix.db") as conn:
        conn.row_factory = sqlite3
        result = []
        for items in conn.execute(query).fetchall():
            s = dict
            result.append(s)
        return result


def search_by_cast(query_result, name1, name2):
    cast = []
    for item in query_result:
        cast += item['cast'].split(', ')
    all_actors = cast
    all_actors.remove(name1)
    all_actors.remove(name2)
    co_actors = []
    for actor in set(all_actors):
        if all_actors.count(actor) > 2:
            co_actors.append(actor)
    return co_actors
