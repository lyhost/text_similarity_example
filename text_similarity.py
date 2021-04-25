import numpy as np

def intersection_similarity(nab, na, nb):
    if na == 0 or nb == 0:
        return 0.0
    return 2 * nab / (na + nb)

def max_same_subsequence_length(s1, s2):
    m = len(s1)
    n = len(s2)

    f = np.zeros((m + 1, n + 1), int)
    for i in range(m):
        for j in range(n):
            if s1[i] == s2[j]:
                f[i + 1][j + 1] = f[i][j] + 1
            else:
                f[i + 1][j + 1] = max(f[i + 1][j], f[i][j + 1])
    return f[m][n]

def ngram_sim(s1, s2, n=1):
    if (n == 1):
        g1 = s1
        g2 = s2
    else:
        g1 = [s1[i:(i+n)] for i in range(len(s1) + 1 - n)]
        g2 = [s2[i:(i+n)] for i in range(len(s2) + 1 - n)]

    return intersection_similarity(max_same_subsequence_length(g1, g2), len(g1), len(g2))


def text_similarity(s1, s2, ngram_weights=[0.5, 0.5]):
    s1 = [t for t in s1.split()]
    s2 = [t for t in s2.split()]
    if s1 == s2:
        return 1.0
    sims = [ngram_sim(s1, s2, i + 1) for i in range(len(ngram_weights))]
    return np.dot(sims, ngram_weights)

def test():
    s1 = '''The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you
    have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need
    to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the
    savings for you.'''

    s2 = '''The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have
    any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to
    cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings
    for you.'''

    s3 = '''We are always looking for opportunities for you to earn more points, which is why we also give you a
    selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular
    points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you
    the points whether or not you knew about the offer. We just think it is easier that way.'''

    print(text_similarity(s1, s2))
    print(text_similarity(s1, s3))


if __name__ == '__main__':
    test()
