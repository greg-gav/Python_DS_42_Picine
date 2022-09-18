num_of_steps = 5

template = f"Report\n\
We have made %count% observations from tossing a coin: \
%tails% of them were tails and %heads% of them were heads. \
The probabilities are %tails_f%% and %heads_f%%, respectively. \
Our forecast is that in the next {num_of_steps} observations we will have: \
%tails_p% tail and %heads_p% heads."

webhook_header = {"Content-type": "application/json"}
webhook_url = "https://hooks.slack.com/services/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"