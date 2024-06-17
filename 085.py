import pandas as pd

def n_rectangles(m, n):
    return m * n * (m + 1) * (n + 1) // 4


if __name__ == '__main__':
    res = []
    res2 = []
    for i in range(100):
        for j in range(100):
            res.append(n_rectangles(i, j))
            res2.append((i, j, n_rectangles(i, j)))

            print(i, j, res[-1])

    # Find i, and j that gives the closest value to 2,000,000
    idx = res.index(min(res, key=lambda x: abs(x - 2000000)))

    print(idx)
    print(res2[idx])
    i, j, n_rect = res2[idx]

    print(i * j)

    # df = pd.DataFrame(res2)
    # df['diff'] = abs(df[2] - 2000000) 
    # df = df.sort_values(by='diff', ascending=True)
    # print(df.head(20))

    # print(df)

    # for i in range(10):
    #     print(i, n_rectangles(i, i))


