'''
Aryan Singhal
CIS 41A   Winter 2024
Unit G, Problem G
'''

def read_states_file():
    highest_population = 0
    state_with_highest_population = ""
    with open('States.txt', 'r') as file:
        for line in file:
            state, region, population = line.strip().split()
            if region == "Midwest" and int(population) > highest_population:
                highest_population = int(population)
                state_with_highest_population = state
    print(f"Highest population state in the Midwest is: {state_with_highest_population} {highest_population}")

def read_presidents_file():
    presidents_by_state = {}
    with open('USPresidents.txt', 'r') as file:
        for line in file:
            state, president = line.strip().split(maxsplit=1)
            if state not in presidents_by_state:
                presidents_by_state[state] = []
            presidents_by_state[state].append(president)
    
    max_presidents = 0
    state_with_max_presidents = ""
    for state, presidents in presidents_by_state.items():
        if len(presidents) > max_presidents:
            max_presidents = len(presidents)
            state_with_max_presidents = state
    
    print(f"The state with the most presidents is {state_with_max_presidents} with {max_presidents} presidents:")
    for president in presidents_by_state[state_with_max_presidents]:
        print(president)

def analyze_president_counts():
    # Assuming presidents_by_state is available from read_presidents_file
    president_counts = {state: len(presidents) for state, presidents in presidents_by_state.items()}
    
    populous_states = {"CA", "TX", "FL", "NY", "IL", "PA", "OH", "GA", "NC", "MI"}
    states_with_presidents = set(president_counts.keys())
    
    populous_states_with_presidents = populous_states & states_with_presidents
    print(f"{len(populous_states_with_presidents)} of the 10 high population states have had presidents born in them:")
    for state in sorted(populous_states_with_presidents):
        print(f"{state} {president_counts[state]}")

def main():
    read_states_file()
    read_presidents_file()
    analyze_president_counts()

if __name__ == "__main__":
    main()



'''
Execution results:


'''