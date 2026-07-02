class Solution:
    def judgeCircle(self, moves: str) -> bool:
        count1=0
        count2=0
        count3=0
        count4=0
        for i in moves:
            if i=="L":
                count1+=1
            elif i=="U":
                count2+=1
            elif i=="R":
                count3+=1
            elif i=="D":
                count4+=1
            
        if count1==count3 and count2==count4:
            return True
        return False