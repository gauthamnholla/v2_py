class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n=len(items)
        count=[0]*(n + 1)
        mini=float('inf')
        for i in range(n):
            count[items[i][0]]+=1
            if items[i][1]<mini:
                mini=items[i][1]
        temp=[0]*(n + 1)
        for i in range(1,n+1):
            if count[i]>0:
                m=-1
                for j in range(i,n+1,i):
                    m+=count[j]
                temp[i]=m
        deal=[0]*n
        dealcount=0
        limit=mini*2
        for i in range(n):
            first=items[i][0]
            second=items[i][1]
            if second<limit:
                m=temp[first]
                if m>0:
                    deal[dealcount]=(second<<32)|(m & 0xFFFFFFFF)
                    dealcount+=1
        deal[:dealcount]=sorted(deal[:dealcount])
        total = 0
        for i in range(dealcount):
            deals=deal[i]
            m=deals>>32
            counts=deals&0xFFFFFFFF
            if budget>=m:
                time=min(counts,budget//m)
                budget-=time * m
                total+=2*time
        total+=budget//mini
        return int(total)