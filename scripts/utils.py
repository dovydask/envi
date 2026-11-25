import numpy as np

def original_datetime_converter(x):
    t = str(x)
    if len(t) != 8:
        split_date = t.split(" ")
        day_mul = int(split_date[0].split("-")[-1])
        new_t = split_date[-1].split(":")
        new_t[0] = str(int(new_t[0]) + 24*day_mul)
        t = ":".join(new_t)
    return t


def smoothen(xs, window):
    if window == 0:
        return xs
    else:
        return np.moveaxis(np.array([
            xs[..., t:t+window].sum(axis = len(xs.shape) - 1) / window
            for t in range(xs.shape[-1] - window+1)
        ]), 0, len(xs.shape) - 1)


def gram_angle(a, b, c):
    X_ab = np.column_stack([a, b])
    X_abc = np.column_stack([a, b, c])

    G_ab = X_ab.T @ X_ab
    G_abc = X_abc.T @ X_abc

    area_ab = np.sqrt(np.linalg.det(G_ab))
    volume_abc = np.sqrt(np.linalg.det(G_abc))

    sin_theta = volume_abc/(area_ab*np.linalg.norm(c))
    sin_theta = np.clip(sin_theta, 0.0, 1.0)

    return np.arcsin(sin_theta)


def vector_angle(a, b):
    a = np.asarray(a, dtype=float)
    b = np.asarray(b, dtype=float)

    G = np.column_stack([a, b]).T @ np.column_stack([a, b])

    cos_theta = G[0, 1]/np.sqrt(G[0, 0]*G[1, 1])
    cos_theta = np.clip(cos_theta, -1.0, 1.0)

    return np.arccos(cos_theta)