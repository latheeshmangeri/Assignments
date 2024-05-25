import sys

prior_probs = {'h1': 0.10, 'h2': 0.20, 'h3': 0.40, 'h4': 0.20, 'h5': 0.10}

transition_probs = {
    'h1': {'C': 1.0, 'L': 0.0},
    'h2': {'C': 0.75, 'L': 0.25},
    'h3': {'C': 0.50, 'L': 0.50},
    'h4': {'C': 0.25, 'L': 0.75},
    'h5': {'C': 0.0, 'L': 1.0}
}

def compute_posterior_and_next(observation_sequence):
    result_text = []
    
    seq_length = len(observation_sequence)
    result_text.append(f"Observation sequence Q: {observation_sequence}\n")
    result_text.append(f"Length of Q: {seq_length}\n\n")

    posterior_probs = prior_probs.copy()
    next_candy_probs = {'C': 0.0, 'L': 0.0}

    for i, obs in enumerate(observation_sequence):
        result_text.append(f"After Observation {i+1} = {obs}:\n")
        total_prob_next_candy_C = 0
        total_prob_next_candy_L = 0

        normalization_constant = sum([posterior_probs[h] * transition_probs[h][obs] for h in posterior_probs])

        for hyp, prior_prob in posterior_probs.items():
            likelihood = transition_probs[hyp][obs]
            posterior_prob = (prior_prob * likelihood) / normalization_constant
            posterior_probs[hyp] = posterior_prob
            result_text.append(f"P({hyp} | Q) = {posterior_prob:.5f}\n")

            total_prob_next_candy_C += posterior_prob * transition_probs[hyp]['C']
            total_prob_next_candy_L += posterior_prob * transition_probs[hyp]['L']

        next_candy_probs['C'] = total_prob_next_candy_C
        next_candy_probs['L'] = total_prob_next_candy_L

        result_text.append(f"Probability that the next candy we pick will be C, given Q: {next_candy_probs['C']:.5f}\n")
        result_text.append(f"Probability that the next candy we pick will be L, given Q: {next_candy_probs['L']:.5f}\n\n")

    # Write the result to result.txt
    with open("result.txt", "w") as result_file:
        result_file.writelines(result_text)
        print('Results Stored in result.txt')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        observation_sequence = sys.argv[1]
        compute_posterior_and_next(observation_sequence)
    else:
        with open("result.txt", "w") as result_file:
            result_file.write("Observation sequence Q: \n")
            result_file.write("Length of Q: 0\n")