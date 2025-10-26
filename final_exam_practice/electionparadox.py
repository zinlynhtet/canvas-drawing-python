def solve_oddland():
    # Read input
    n = int(input())
    populations = list(map(int, input().split()))
    
    # To lose the election, a party must lose the majority of regions
    # That means losing at least (n+1)//2 regions
    regions_to_lose = (n + 1) // 2
    regions_to_win = n - regions_to_lose
    
    # Strategy to maximize votes while losing:
    # - Win the regions with LARGEST populations (get all p votes in each)
    # - Lose the regions with SMALLEST populations (get floor(p/2) votes in each)
    
    # Sort populations in ascending order
    sorted_pops = sorted(populations)
    
    total_votes = 0
    
    for i in range(regions_to_lose):
        # In a region with odd population, to lose we get floor(p/2) votes
        votes_in_region = sorted_pops[i] // 2
        total_votes += votes_in_region
    
    for i in range(regions_to_lose, n):
        total_votes += sorted_pops[i]
    
    print(total_votes)

if __name__ == "__main__":
    solve_oddland()
