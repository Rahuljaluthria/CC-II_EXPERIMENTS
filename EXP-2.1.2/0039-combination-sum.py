class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def dfs(i, current_combo, total):
            if total == target:
                res.append(current_combo.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            current_combo.append(candidates[i])
            dfs(i, current_combo, total + candidates[i])
            
            current_combo.pop()
            dfs(i + 1, current_combo, total)
            
        dfs(0, [], 0)
        return res