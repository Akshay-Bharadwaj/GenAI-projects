from utils.llm import get_llm

llm = get_llm()
res = llm.invoke("Say hello in one line")
print(res.content)