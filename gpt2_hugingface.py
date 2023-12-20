# api key:
API_Token = "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"

from huggingface_hub.inference_api import InferenceApi

inference = InferenceApi(repo_id="gpt2-large", token=API_Token)

#changing the topk and topp paramters:

top_p_params = {"max_length": 128, "top_p": 0.95, "do_sample":True} # top-p (nucleus sampling)
top_k_params = {"max_length": 128,  "top_k": 4, "do_sample":True} # top-k
contrastive_params = {"max_length": 128, "penalty_alpha": 0.6, "top_k": 4}

input_string = "Learn about AI because"
result = inference(input_string , top_k_params , top_p_params)
print(result)
print()
print()
result = inference(input_string , top_k_params)
print("Reslt for top_k: {}".format(result))

result = inference(input_string  , top_p_params)
print("Reslt for top_p: {}".format(result))

print()
result = inference(input_string  , contrastive_params)
print("Reslt for contrastive: {}".format(result))


