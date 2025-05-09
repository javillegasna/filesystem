from mcp.types import TextContent
from pydantic import BaseModel

from core.enums import FileSystemTools
from core.types import BaseTool


class WriteFileInput(BaseModel):
    path: str
    content: str


TOOL_DESCRIPTION = f"""
    Writes content to a file on the filesystem.
    @Input:
        path: The path to the file to write to.
    @Output:
        text: A message indicating the success of the operation.
    @Schema: {WriteFileInput.model_json_schema()}
"""

class WriteFileTool(BaseTool):

    def __init__(self):
        super().__init__(
            inputSchema=WriteFileInput.model_json_schema(),
            name=FileSystemTools.WRITE_FILE.value,
            description=TOOL_DESCRIPTION,
        )
    def _entrypoint(self, input: WriteFileInput) -> TextContent:
        with open(input.path, "w") as file:
            file.write(input.content)
        return TextContent(
            type="text", text=f"File written successfully to {input.path}"
        )
