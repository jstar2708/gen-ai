from langchain_core.tools import tool

# Step 1: create a function
# Step 2: add type hints
# Step 3 - add tool decorator
@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

result = multiply.invoke({"a": 3, "b": 5})
print(result)

print(multiply.name)
print(multiply.description)
print(multiply.args)