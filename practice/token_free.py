import tiktoken
enc=tiktoken.encoding_for_model("gpt-4")
text="hey my name is neha"
tokens=enc.encode(text)
print("tokens",tokens)
ans=enc.decode([48467, 922, 1308, 382, 453, 1716])
print(ans)