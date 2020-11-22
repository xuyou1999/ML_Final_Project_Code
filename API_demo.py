from DoubanAPI import DoubanAPI
import pandas as pd

if __name__ == '__main__':
    columns = ("director", "screenwriter", "actor", "genre", "region", "date",
               "rating", "rating_count", "rating_weight")
    df = pd.DataFrame(columns=columns)
    d = DoubanAPI()
    for id in [4864908, 26607693, 26662193]:
        d.search(id)
        info = d.info()
        print(info)
        data = {"director": [info["director_id"]], "screenwriter": [info["screenwriter_id"]],
                "actor": [info["actor_id"]], "genre": [info["类型"]], "region": [info["制片国家/地区"]],
                "date": [info["上映日期"]], "rating": [info["rating"]], "rating_count": [info["rating_count"]],
                "rating_weight": [info["rating_weight"]]}
        new = pd.DataFrame(data, columns=columns)
        df = pd.concat([df, new], ignore_index=True)
    print(df.head())
