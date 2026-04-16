def value_iteration_step(values, transitions, rewards, gamma):
    """
    Perform one step of value iteration and return updated values.
    """
    
    n_states = len(values)
    n_actions = len(rewards[0])
    new_values = []
    
    for s in range(n_states) : 
        best_q = float('-inf')
        
        for a in range(n_actions):
            q = rewards[s][a]
            expected_future = 0
            
            for s_next in range(n_states):
                expected_future += transitions[s][a][s_next] * values[s_next]

            q += expected_future * gamma
            best_q = max(best_q, q)

        new_values.append(best_q)

    return new_values
        