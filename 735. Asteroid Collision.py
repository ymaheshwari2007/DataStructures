class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stackright = []
        stackleft = []
        for ass in asteroids:
            if ass > 0:
                stackright.append(ass)
            else:
                stackleft.append(ass)
            
            if ass < 0 and len(stackright) > 0:
                while len(stackright) > 0:
                    if abs(ass) > stackright[-1]:
                        stackright.pop()
                    elif abs(ass) == stackright[-1]:
                        stackright.pop()
                        stackleft.pop()
                        break
                    else:
                        stackleft.pop()
                        break
        return stackleft + stackright
