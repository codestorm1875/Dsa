# Problem: https://leetcode.com/problems/block-placement-queries/
# Time Complexity: O(n log M) 
# Space Complexity: O(M)

from array import array

class Solution:
    def getResults(self, queries):
        mx = 0
        for q in queries:
            if q[1] > mx: mx = q[1]
        N = mx + 1
        LG = N.bit_length()

        gap = array('i', bytes(4 * (N + 1)))
        cnt = array('i', bytes(4 * (N + 1)))
        prv = array('i', b'\xff\xff\xff\xff' * N)
        nxt = array('i', b'\xff\xff\xff\xff' * N)

        def gap_up(i, v):
            i += 1
            while i <= N:
                if v > gap[i]: gap[i] = v
                i += i & (-i)

        def gap_qr(i):
            r = 0; i += 1
            while i > 0:
                if gap[i] > r: r = gap[i]
                i -= i & (-i)
            return r

        def cnt_up(i, d):
            i += 1
            while i <= N:
                cnt[i] += d
                i += i & (-i)

        def pred(x):
            k = 0; j = x + 1
            while j > 0:
                k += cnt[j]; j -= j & (-j)
            pos = 0
            for i in range(LG, -1, -1):
                np = pos + (1 << i)
                if np <= N and cnt[np] < k:
                    k -= cnt[np]; pos = np
            return pos

        obs = sorted(set(q[1] for q in queries if q[0] == 1) | {0})

        for i, x in enumerate(obs):
            cnt_up(x, 1)
            if i > 0:
                gap_up(x, x - obs[i - 1])
                prv[x] = obs[i - 1]
                nxt[obs[i - 1]] = x

        results = []
        for q in reversed(queries):
            if q[0] == 1:
                x = q[1]
                p, s = prv[x], nxt[x]
                if s != -1:
                    gap_up(s, s - p)
                    prv[s] = p
                if p != -1:
                    nxt[p] = s
                cnt_up(x, -1)
            else:
                x, sz = q[1], q[2]
                px = pred(x)
                best = gap_qr(x)
                trail = x - px
                if trail > best: best = trail
                results.append(best >= sz)

        results.reverse()
        return results