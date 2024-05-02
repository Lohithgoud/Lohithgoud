class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count=Counter(tasks)
        max_freq=max(task_count.values())
        max_freq_tasks= sum(1 for value in task_count.values() if value == max_freq )
        i_needed=(max_freq-1)*(n+1)+max_freq_tasks
        return max(i_needed,len(tasks))
