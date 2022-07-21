class Solution:
    def countPrimes(self, n: int) -> int:
        prime=self.sieveOfEratosthenes(n)
        ans=0
        for i in prime:
            if i==True:
                ans+=1
        return ans
    
    def sieveOfEratosthenes(self, n: int) -> int:
        if n<2:
            return []
        prime=[True for i in range(n)]
        prime[0]=prime[1]=False
        p=2
        while p*p<=n:
            if prime[p]==True:
                for i in range(p*p,n,p):
                    prime[i]=False
            p += 1
        return prime