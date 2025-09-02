from beaker import Application, external, Box, consts
from pyteal import Bytes, Expr, InnerTxnBuilder, TxnField, TxnType, TealType

# Define the box storage
class MyState:
    # This creates a box with a dynamic key, here we want a static key, so we use a Box directly
    github_box = Box(TealType.bytes, key_name="github")

# Create the application
class GitHubBoxContract(Application):
    def __init__(self):
        self.state = MyState()
        super().__init__()

    @external
    def deposit(self, github_handle: Bytes) -> Expr:
        # Create a box with the name 'github' and store the username
        # The size is determined by the length of the string
        return self.state.github_box.put(github_handle)

    # We need a method to create the box initially, which we can call with
    # our deployment script.
    @external(authorize=consts.CREATOR)
    def create_github_box(self) -> Expr:
        return self.state.github_box.create(Bytes(""), size=1)
