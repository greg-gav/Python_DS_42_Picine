num_of_steps = 5

template = f"Report\n\
We have made %count% observations from tossing a coin: \
%tails% of them were tails and %heads% of them were heads. \
The probabilities are %tails_f%% and %heads_f%%, respectively. \
Our forecast is that in the next {num_of_steps} observations we will have: \
%tails_p% tail and %heads_p% heads."