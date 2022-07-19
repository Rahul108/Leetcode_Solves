class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people=sorted(people)
        no_of_boats=0
        left=0
        right=len(people)-1
        while left <= right:
            if left==right:
                no_of_boats += 1
                break
            elif people[left]+people[right] <= limit:
                no_of_boats+=1
                left += 1
                right -= 1
            else:
                no_of_boats += 1
                right -= 1
        return no_of_boats