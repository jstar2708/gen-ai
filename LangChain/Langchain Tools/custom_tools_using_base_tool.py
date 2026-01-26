from langchain_classic.tools import BaseTool
from pydantic import BaseModel, Field
from typing import Type

class MultiplyInput(BaseModel):
    a: int = Field(required = True, description = "The first number to multiply")
    b: int = Field(required = True, description = "The second number to multiply")

class MultiplyTool(BaseTool):
    name: str = "Multiply"
    description: str = "Multiply two numbers"
    args_schema: Type[BaseModel] = MultiplyInput

    def _run(self, a: int, b: int) -> int:
        return a * b
    
multiply_tool = MultiplyTool()
result = multiply_tool.invoke({"a": 3, "b": 3})
print(result)
print(multiply_tool.name)
print(multiply_tool.description)
